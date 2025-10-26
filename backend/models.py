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
    sanskrit_name: str
    scientific_name: str
    botanical_synonyms: List[str] = []
    family: str
    vernacular_names: dict = {}  # {"Hindi": "name", "Telugu": "name", etc}
    synonyms: List[dict] = []  # [{"name": "synonym", "reason": "description"}]
    gana: List[dict] = []  # [{"author": "Charaka", "gana": "Deepaniya"}]
    types: List[str] = []
    
    # Morphology
    habit: str  # tree, shrub, herb
    habitat: str
    morphology: dict = {
        "leaf": "",
        "stem": "",
        "flower": "",
        "fruit": "",
        "inflorescence": "",
        "seeds": "",
        "root": ""
    }
    
    description: str
    characteristics: List[str]
    
    # Ayurvedic Properties (Rasapanchaka)
    rasa: List[str] = []  # Madhura, Amla, Lavana, Katu, Tikta, Kashaya
    guna: List[str] = []  # Guru, Laghu, Snigdha, Ruksha, Ushna, Shita
    virya: str = ""  # Ushna or Shita
    vipaka: str = ""  # Madhura, Amla, or Katu
    prabhava: str = ""  # Specific action
    
    # Therapeutic properties
    dosha_karma: dict = {}  # {"Vata": "pacifies", "Pitta": "increases", "Kapha": "pacifies"}
    karma: List[str] = []  # Deepana, Pachana, etc
    indication: List[str] = []
    
    medicinal_properties: List[str]
    uses: List[str]
    therapeutic_uses: dict = {"internal": [], "external": []}
    
    # Parts and dosage
    parts_used: List[str]
    dosage: dict = {}  # {"powder": "3-6g", "decoction": "50-100ml"}
    
    # Chemical and modern
    chemical_constituents: List[str] = []
    phyto_constituents: List[str] = []
    modern_pharmacology: List[str] = []
    research_updates: List[str] = []
    
    # Formulations and processing
    formulations: List[str] = []
    shodana: str = ""  # purification process if any
    
    # Safety
    adulterants: List[str] = []
    contraindications: List[str] = []
    substitutes: List[str] = []
    
    # References
    references: List[dict] = []  # [{"text": "text", "verse": "verse", "source": "source"}]
    
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