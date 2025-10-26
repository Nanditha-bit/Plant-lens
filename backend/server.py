from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from bson import ObjectId
from typing import List, Optional
import os
from dotenv import load_dotenv
from models import (
    UserCreate, UserLogin, User, Plant, PlantCreate,
    ScanHistory, IdentifyPlantRequest, IdentifyPlantResponse
)
from auth import (
    get_password_hash, verify_password, create_access_token, get_current_user
)
from plant_identifier import identify_plant_from_image
import re

load_dotenv()

app = FastAPI(title="Ayurvedic Plants API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/ayurvedic_plants")
client = MongoClient(MONGO_URL)
db = client.ayurvedic_plants

# Collections
users_collection = db.users
plants_collection = db.plants
scans_collection = db.scans

# Create indexes
users_collection.create_index("username", unique=True)
plants_collection.create_index("name")
plants_collection.create_index("scientific_name")

@app.get("/api")
async def root():
    return {"message": "Ayurvedic Plants API", "version": "1.0"}

# ============= AUTH ENDPOINTS =============

@app.post("/api/auth/register")
async def register(user: UserCreate):
    # Check if user exists
    existing_user = users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Create user
    user_dict = {
        "username": user.username,
        "password_hash": get_password_hash(user.password),
        "created_at": None
    }
    result = users_collection.insert_one(user_dict)
    
    # Create token
    access_token = create_access_token(
        data={"sub": user.username, "user_id": str(result.inserted_id)}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }

@app.post("/api/auth/login")
async def login(user: UserLogin):
    # Find user
    db_user = users_collection.find_one({"username": user.username})
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Verify password
    if not verify_password(user.password, db_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Create token
    access_token = create_access_token(
        data={"sub": user.username, "user_id": str(db_user["_id"])}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }

@app.get("/api/auth/me")
async def get_me(current_user: dict = Depends(get_current_user)):
    return current_user

# ============= PLANT ENDPOINTS =============

@app.get("/api/plants")
async def get_plants(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    search: Optional[str] = None
):
    query = {}
    if search:
        # Case-insensitive search
        regex = re.compile(search, re.IGNORECASE)
        query = {
            "$or": [
                {"name": regex},
                {"scientific_name": regex},
                {"family": regex}
            ]
        }
    
    plants = list(plants_collection.find(query).skip(skip).limit(limit))
    total = plants_collection.count_documents(query)
    
    # Convert ObjectId to string and handle images
    for plant in plants:
        plant["_id"] = str(plant["_id"])
        # Only send first image in list view for performance
        if "images_base64" in plant and len(plant["images_base64"]) > 0:
            plant["thumbnail"] = plant["images_base64"][0]
            del plant["images_base64"]  # Remove full images from list
    
    return {
        "plants": plants,
        "total": total,
        "skip": skip,
        "limit": limit
    }

@app.get("/api/plants/{plant_id}")
async def get_plant(plant_id: str):
    if not ObjectId.is_valid(plant_id):
        raise HTTPException(status_code=400, detail="Invalid plant ID")
    
    plant = plants_collection.find_one({"_id": ObjectId(plant_id)})
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    
    plant["_id"] = str(plant["_id"])
    return plant

@app.post("/api/plants")
async def create_plant(
    plant: PlantCreate,
    current_user: dict = Depends(get_current_user)
):
    plant_dict = plant.model_dump()
    result = plants_collection.insert_one(plant_dict)
    plant_dict["_id"] = str(result.inserted_id)
    return plant_dict

# ============= PLANT IDENTIFICATION =============

@app.post("/api/plants/identify")
async def identify_plant(
    request: IdentifyPlantRequest,
    current_user: dict = Depends(get_current_user)
):
    # Call OpenAI Vision API
    result = await identify_plant_from_image(request.image_base64)
    
    if not result["success"]:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to identify plant: {result.get('error', 'Unknown error')}"
        )
    
    plant_data = result["data"]
    
    # Check if plant exists in database
    db_plant = None
    database_plant_id = None
    if plant_data.get("plant_name"):
        # Search for matching plant
        regex = re.compile(plant_data["plant_name"], re.IGNORECASE)
        db_plant = plants_collection.find_one({"name": regex})
        if db_plant:
            database_plant_id = str(db_plant["_id"])
    
    # Save scan history
    scan_record = {
        "user_id": current_user["user_id"],
        "scanned_image_base64": request.image_base64,
        "identified_plant_name": plant_data.get("plant_name", "Unknown"),
        "confidence": plant_data.get("confidence", "low"),
        "ai_response": result["raw_response"],
        "timestamp": None
    }
    scan_result = scans_collection.insert_one(scan_record)
    
    return {
        "plant_name": plant_data.get("plant_name", "Unknown"),
        "scientific_name": plant_data.get("scientific_name"),
        "confidence": plant_data.get("confidence", "low"),
        "characteristics": plant_data.get("characteristics", []),
        "medicinal_properties": plant_data.get("medicinal_properties", []),
        "uses": plant_data.get("uses", []),
        "parts_used": plant_data.get("parts_used", []),
        "matches_database": db_plant is not None,
        "database_plant_id": database_plant_id,
        "full_description": plant_data.get("description", ""),
        "scan_id": str(scan_result.inserted_id)
    }

@app.get("/api/scans/history")
async def get_scan_history(
    current_user: dict = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=50)
):
    scans = list(
        scans_collection
        .find({"user_id": current_user["user_id"]})
        .sort("timestamp", -1)
        .skip(skip)
        .limit(limit)
    )
    
    for scan in scans:
        scan["_id"] = str(scan["_id"])
    
    return {"scans": scans, "total": len(scans)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)