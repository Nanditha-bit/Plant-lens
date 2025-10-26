from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Plant(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    scientific_name: str
    family: str
    description: str
    characteristics: List[str]
    medicinal_properties: List[str]
    uses: List[str]
    parts_used: List[str]
    images_base64: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class PlantCreate(BaseModel):
    name: str
    scientific_name: str
    family: str
    description: str
    characteristics: List[str]
    medicinal_properties: List[str]
    uses: List[str]
    parts_used: List[str]
    images_base64: List[str]

class ScanHistory(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    user_id: str
    scanned_image_base64: str
    identified_plant_name: str
    confidence: str
    ai_response: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class IdentifyPlantRequest(BaseModel):
    image_base64: str

class IdentifyPlantResponse(BaseModel):
    plant_name: str
    scientific_name: Optional[str]
    confidence: str
    characteristics: List[str]
    medicinal_properties: List[str]
    matches_database: bool
    database_plant_id: Optional[str]
    full_description: str