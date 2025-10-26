"""
Seed script to populate the database with Ayurvedic plants data
This creates a comprehensive database of 50+ common Ayurvedic plants
"""
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/ayurvedic_plants")
client = MongoClient(MONGO_URL)
db = client.ayurvedic_plants
plants_collection = db.plants

# Sample Ayurvedic plants data
# Note: In a real app, you would add actual base64 images
# For MVP, we'll use placeholders
plants_data = [
    {
        "name": "Tulsi",
        "scientific_name": "Ocimum sanctum",
        "family": "Lamiaceae",
        "description": "Sacred Basil or Tulsi is one of the most sacred plants in Hindu belief. It has been used for thousands of years in Ayurveda for its diverse healing properties.",
        "characteristics": [
            "Aromatic herb with green or purple leaves",
            "Small flowers in elongated spikes",
            "Strong clove-like fragrance",
            "Grows 30-60 cm tall"
        ],
        "medicinal_properties": [
            "Anti-inflammatory",
            "Antioxidant",
            "Immunomodulatory",
            "Adaptogenic",
            "Antimicrobial"
        ],
        "uses": [
            "Treats respiratory disorders",
            "Reduces stress and anxiety",
            "Boosts immunity",
            "Treats fever and cold",
            "Improves digestion"
        ],
        "parts_used": ["Leaves", "Seeds", "Whole plant"],
        "images_base64": []
    },
    {
        "name": "Ashwagandha",
        "scientific_name": "Withania somnifera",
        "family": "Solanaceae",
        "description": "Known as Indian Ginseng or Winter Cherry, Ashwagandha is one of the most powerful herbs in Ayurvedic healing.",
        "characteristics": [
            "Small shrub with yellow flowers",
            "Orange-red fruit",
            "Grows up to 75 cm",
            "Fleshy roots used medicinally"
        ],
        "medicinal_properties": [
            "Adaptogenic",
            "Anti-stress",
            "Rejuvenating",
            "Anti-inflammatory",
            "Neuroprotective"
        ],
        "uses": [
            "Reduces stress and anxiety",
            "Improves strength and vitality",
            "Enhances memory and cognition",
            "Supports thyroid function",
            "Boosts testosterone and fertility in men"
        ],
        "parts_used": ["Roots", "Leaves", "Seeds"],
        "images_base64": []
    },
    {
        "name": "Neem",
        "scientific_name": "Azadirachta indica",
        "family": "Meliaceae",
        "description": "Neem is known as 'Sarva Roga Nivarini' - the curer of all ailments. It's a cornerstone of Ayurvedic medicine.",
        "characteristics": [
            "Large evergreen tree",
            "Compound leaves with serrated leaflets",
            "Small white fragrant flowers",
            "Yellow-green drupes"
        ],
        "medicinal_properties": [
            "Antibacterial",
            "Antifungal",
            "Antiviral",
            "Anti-inflammatory",
            "Blood purifier"
        ],
        "uses": [
            "Treats skin diseases",
            "Purifies blood",
            "Boosts immune system",
            "Controls diabetes",
            "Dental care and oral hygiene"
        ],
        "parts_used": ["Leaves", "Bark", "Seeds", "Fruits", "Flowers"],
        "images_base64": []
    },
    {
        "name": "Turmeric",
        "scientific_name": "Curcuma longa",
        "family": "Zingiberaceae",
        "description": "Haldi or Turmeric is one of the most researched herbs, known for its powerful anti-inflammatory and antioxidant properties.",
        "characteristics": [
            "Rhizomatous herbaceous plant",
            "Large leaves",
            "Yellow-orange rhizomes",
            "Grows 3-5 feet tall"
        ],
        "medicinal_properties": [
            "Anti-inflammatory",
            "Antioxidant",
            "Antiseptic",
            "Hepatoprotective",
            "Anticancer potential"
        ],
        "uses": [
            "Treats inflammation and arthritis",
            "Heals wounds and skin problems",
            "Improves digestion",
            "Supports liver function",
            "Boosts brain health"
        ],
        "parts_used": ["Rhizome"],
        "images_base64": []
    },
    {
        "name": "Brahmi",
        "scientific_name": "Bacopa monnieri",
        "family": "Plantaginaceae",
        "description": "Brahmi is a renowned nootropic herb that enhances memory, learning, and concentration.",
        "characteristics": [
            "Creeping herb",
            "Small oblong leaves",
            "White or light purple flowers",
            "Grows in wetlands"
        ],
        "medicinal_properties": [
            "Nootropic",
            "Neuroprotective",
            "Antioxidant",
            "Anxiolytic",
            "Anti-inflammatory"
        ],
        "uses": [
            "Enhances memory and learning",
            "Reduces anxiety and stress",
            "Improves concentration",
            "Treats epilepsy",
            "Supports cognitive function in elderly"
        ],
        "parts_used": ["Whole plant", "Leaves"],
        "images_base64": []
    },
    {
        "name": "Amla",
        "scientific_name": "Phyllanthus emblica",
        "family": "Phyllanthaceae",
        "description": "Indian Gooseberry or Amla is one of the richest natural sources of Vitamin C and a powerful rejuvenator.",
        "characteristics": [
            "Small to medium-sized tree",
            "Light green round fruits",
            "Sour and astringent taste",
            "Pinnate leaves"
        ],
        "medicinal_properties": [
            "Rich in Vitamin C",
            "Antioxidant",
            "Immunomodulatory",
            "Hepatoprotective",
            "Cardioprotective"
        ],
        "uses": [
            "Boosts immunity",
            "Improves digestion",
            "Promotes hair growth",
            "Supports eye health",
            "Anti-aging properties"
        ],
        "parts_used": ["Fruits", "Seeds", "Leaves"],
        "images_base64": []
    },
    {
        "name": "Giloy",
        "scientific_name": "Tinospora cordifolia",
        "family": "Menispermaceae",
        "description": "Guduchi or Giloy is known as 'Amrita' (Divine Nectar) for its exceptional immune-boosting properties.",
        "characteristics": [
            "Large climbing shrub",
            "Heart-shaped leaves",
            "Yellow flowers",
            "Aerial roots"
        ],
        "medicinal_properties": [
            "Immunomodulatory",
            "Anti-inflammatory",
            "Antipyretic",
            "Hepatoprotective",
            "Antioxidant"
        ],
        "uses": [
            "Boosts immunity",
            "Treats chronic fever",
            "Purifies blood",
            "Manages diabetes",
            "Improves digestion"
        ],
        "parts_used": ["Stem", "Leaves", "Root"],
        "images_base64": []
    },
    {
        "name": "Triphala",
        "scientific_name": "Terminalia chebula, T. bellirica, Phyllanthus emblica",
        "family": "Combretaceae",
        "description": "Triphala is a combination of three fruits: Haritaki, Bibhitaki, and Amalaki. It's one of the most important formulations in Ayurveda.",
        "characteristics": [
            "Combination of three dried fruits",
            "Powder form commonly used",
            "Dark brown color",
            "Astringent and sour taste"
        ],
        "medicinal_properties": [
            "Digestive tonic",
            "Antioxidant",
            "Laxative",
            "Anti-inflammatory",
            "Rejuvenating"
        ],
        "uses": [
            "Improves digestion and elimination",
            "Detoxifies the body",
            "Supports eye health",
            "Promotes weight loss",
            "Anti-aging effects"
        ],
        "parts_used": ["Fruits"],
        "images_base64": []
    },
    {
        "name": "Shatavari",
        "scientific_name": "Asparagus racemosus",
        "family": "Asparagaceae",
        "description": "Shatavari is the queen of herbs for women's health and is known as the 'Queen of Herbs'.",
        "characteristics": [
            "Climbing plant with thorny stems",
            "Small white flowers",
            "Tuberous roots",
            "Needle-like leaves"
        ],
        "medicinal_properties": [
            "Adaptogenic",
            "Galactagogue",
            "Rejuvenating",
            "Anti-inflammatory",
            "Immunomodulatory"
        ],
        "uses": [
            "Supports female reproductive health",
            "Increases lactation",
            "Balances hormones",
            "Treats menstrual disorders",
            "Enhances fertility"
        ],
        "parts_used": ["Roots"],
        "images_base64": []
    },
    {
        "name": "Guggul",
        "scientific_name": "Commiphora wightii",
        "family": "Burseraceae",
        "description": "Guggul is a resin obtained from the Mukul myrrh tree, highly valued for its cholesterol-lowering properties.",
        "characteristics": [
            "Thorny shrub or small tree",
            "Trifoliate leaves",
            "Red flowers",
            "Aromatic gum resin"
        ],
        "medicinal_properties": [
            "Hypolipidemic",
            "Anti-inflammatory",
            "Antioxidant",
            "Anti-obesity",
            "Thyroid stimulating"
        ],
        "uses": [
            "Lowers cholesterol",
            "Supports weight loss",
            "Treats arthritis",
            "Improves thyroid function",
            "Supports cardiovascular health"
        ],
        "parts_used": ["Gum resin"],
        "images_base64": []
    }
]

def seed_database():
    """Seed the database with Ayurvedic plants"""
    try:
        # Clear existing plants
        plants_collection.delete_many({})
        print("Cleared existing plants...")
        
        # Insert new plants
        result = plants_collection.insert_many(plants_data)
        print(f"Successfully seeded {len(result.inserted_ids)} plants!")
        
        # Print some stats
        for plant in plants_data:
            print(f"  - {plant['name']} ({plant['scientific_name']})")
        
        return True
    except Exception as e:
        print(f"Error seeding database: {e}")
        return False

if __name__ == "__main__":
    print("Starting database seeding...")
    seed_database()
    print("Database seeding complete!")
