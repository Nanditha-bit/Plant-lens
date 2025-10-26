#!/usr/bin/env python3
"""
Comprehensive Plant Database - ALL types of plants and trees
Including ornamental, fruit, vegetable, forest, aquatic, and common plants
"""
from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/ayurvedic_plants")
client = MongoClient(MONGO_URL)
db = client.ayurvedic_plants
plants_collection = db.plants

# Comprehensive list of all types of plants
all_plants = [
    # FRUIT TREES
    {"name": "Mango", "sanskrit_name": "आम्र (Amra)", "scientific_name": "Mangifera indica", "family": "Anacardiaceae", "type": "Fruit Tree", "uses": ["Edible fruit", "Timber", "Shade"]},
    {"name": "Apple", "sanskrit_name": "सेब (Seba)", "scientific_name": "Malus domestica", "family": "Rosaceae", "type": "Fruit Tree", "uses": ["Edible fruit", "Nutrition", "Juice"]},
    {"name": "Banana", "sanskrit_name": "कदली (Kadali)", "scientific_name": "Musa paradisiaca", "family": "Musaceae", "type": "Fruit Plant", "uses": ["Edible fruit", "Fiber", "Leaves for plates"]},
    {"name": "Papaya", "sanskrit_name": "एरण्डकर्कटी (Erandakarkati)", "scientific_name": "Carica papaya", "family": "Caricaceae", "type": "Fruit Tree", "uses": ["Edible fruit", "Digestive enzyme", "Latex"]},
    {"name": "Guava", "sanskrit_name": "अमरूद (Amrud)", "scientific_name": "Psidium guajava", "family": "Myrtaceae", "type": "Fruit Tree", "uses": ["Edible fruit", "Vitamin C", "Medicinal leaves"]},
    {"name": "Orange", "sanskrit_name": "नारङ्ग (Naranga)", "scientific_name": "Citrus sinensis", "family": "Rutaceae", "type": "Fruit Tree", "uses": ["Edible fruit", "Vitamin C", "Essential oil"]},
    {"name": "Pomegranate", "sanskrit_name": "दाडिम (Dadima)", "scientific_name": "Punica granatum", "family": "Lythraceae", "type": "Fruit Tree", "uses": ["Edible fruit", "Antioxidants", "Juice"]},
    {"name": "Coconut", "sanskrit_name": "नारिकेल (Narikela)", "scientific_name": "Cocos nucifera", "family": "Arecaceae", "type": "Palm Tree", "uses": ["Edible fruit", "Oil", "Water", "Fiber"]},
    {"name": "Jackfruit", "sanskrit_name": "पनस (Panasa)", "scientific_name": "Artocarpus heterophyllus", "family": "Moraceae", "type": "Fruit Tree", "uses": ["Edible fruit", "Timber", "Largest tree fruit"]},
    {"name": "Grapes", "sanskrit_name": "द्राक्षा (Draksha)", "scientific_name": "Vitis vinifera", "family": "Vitaceae", "type": "Vine", "uses": ["Edible fruit", "Wine", "Raisins"]},
    {"name": "Litchi", "sanskrit_name": "लीची (Lichi)", "scientific_name": "Litchi chinensis", "family": "Sapindaceae", "type": "Fruit Tree", "uses": ["Edible fruit", "Sweet taste"]},
    {"name": "Dragon Fruit", "sanskrit_name": "पिताया (Pitaya)", "scientific_name": "Hylocereus undatus", "family": "Cactaceae", "type": "Cactus", "uses": ["Edible fruit", "Ornamental"]},
    
    # VEGETABLES & CROPS
    {"name": "Tomato", "sanskrit_name": "टमाटर (Tamatar)", "scientific_name": "Solanum lycopersicum", "family": "Solanaceae", "type": "Vegetable", "uses": ["Edible fruit", "Cooking", "Nutrition"]},
    {"name": "Potato", "sanskrit_name": "आलू (Alu)", "scientific_name": "Solanum tuberosum", "family": "Solanaceae", "type": "Vegetable", "uses": ["Edible tuber", "Staple food"]},
    {"name": "Onion", "sanskrit_name": "पलाण्डु (Palandu)", "scientific_name": "Allium cepa", "family": "Amaryllidaceae", "type": "Vegetable", "uses": ["Edible bulb", "Flavoring"]},
    {"name": "Garlic", "sanskrit_name": "लशुन (Lashuna)", "scientific_name": "Allium sativum", "family": "Amaryllidaceae", "type": "Vegetable", "uses": ["Edible bulb", "Medicinal", "Flavoring"]},
    {"name": "Cabbage", "sanskrit_name": "पत्तागोभी (Pattagobhi)", "scientific_name": "Brassica oleracea", "family": "Brassicaceae", "type": "Vegetable", "uses": ["Edible leaves", "Nutrition"]},
    {"name": "Cauliflower", "sanskrit_name": "फूलगोभी (Phulgobhi)", "scientific_name": "Brassica oleracea var. botrytis", "family": "Brassicaceae", "type": "Vegetable", "uses": ["Edible flower", "Nutrition"]},
    {"name": "Brinjal", "sanskrit_name": "वृन्ताकी (Vrintaki)", "scientific_name": "Solanum melongena", "family": "Solanaceae", "type": "Vegetable", "uses": ["Edible fruit", "Cooking"]},
    {"name": "Spinach", "sanskrit_name": "पालक (Palak)", "scientific_name": "Spinacia oleracea", "family": "Amaranthaceae", "type": "Vegetable", "uses": ["Edible leaves", "Iron rich"]},
    {"name": "Carrot", "sanskrit_name": "गाजर (Gajar)", "scientific_name": "Daucus carota", "family": "Apiaceae", "type": "Vegetable", "uses": ["Edible root", "Vitamin A"]},
    {"name": "Radish", "sanskrit_name": "मूलक (Mulaka)", "scientific_name": "Raphanus sativus", "family": "Brassicaceae", "type": "Vegetable", "uses": ["Edible root", "Salad"]},
    {"name": "Pumpkin", "sanskrit_name": "कुष्माण्ड (Kushmanda)", "scientific_name": "Cucurbita maxima", "family": "Cucurbitaceae", "type": "Vegetable", "uses": ["Edible fruit", "Seeds"]},
    {"name": "Bottle Gourd", "sanskrit_name": "अलाबु (Alabu)", "scientific_name": "Lagenaria siceraria", "family": "Cucurbitaceae", "type": "Vegetable", "uses": ["Edible fruit", "Cooling"]},
    {"name": "Cucumber", "sanskrit_name": "त्रपुस (Trapusa)", "scientific_name": "Cucumis sativus", "family": "Cucurbitaceae", "type": "Vegetable", "uses": ["Edible fruit", "Salad", "Cooling"]},
    
    # FLOWERS & ORNAMENTAL
    {"name": "Rose", "sanskrit_name": "गुलाब (Gulab)", "scientific_name": "Rosa spp.", "family": "Rosaceae", "type": "Ornamental", "uses": ["Flowers", "Fragrance", "Rose water"]},
    {"name": "Jasmine", "sanskrit_name": "मल्लिका (Mallika)", "scientific_name": "Jasminum spp.", "family": "Oleaceae", "type": "Ornamental", "uses": ["Fragrant flowers", "Essential oil"]},
    {"name": "Marigold", "sanskrit_name": "गेंदा (Genda)", "scientific_name": "Tagetes erecta", "family": "Asteraceae", "type": "Ornamental", "uses": ["Flowers", "Decoration", "Natural dye"]},
    {"name": "Hibiscus", "sanskrit_name": "जपा (Japa)", "scientific_name": "Hibiscus rosa-sinensis", "family": "Malvaceae", "type": "Ornamental", "uses": ["Flowers", "Hair care", "Tea"]},
    {"name": "Lotus", "sanskrit_name": "पद्म (Padma)", "scientific_name": "Nelumbo nucifera", "family": "Nelumbonaceae", "type": "Aquatic", "uses": ["Sacred flower", "Edible seeds", "Beauty"]},
    {"name": "Sunflower", "sanskrit_name": "सूर्यमुखी (Suryamukhi)", "scientific_name": "Helianthus annuus", "family": "Asteraceae", "type": "Ornamental/Oil", "uses": ["Seeds", "Oil", "Ornamental"]},
    {"name": "Lily", "sanskrit_name": "कुमुद (Kumuda)", "scientific_name": "Lilium spp.", "family": "Liliaceae", "type": "Ornamental", "uses": ["Flowers", "Fragrance"]},
    {"name": "Orchid", "sanskrit_name": "वन्दा (Vanda)", "scientific_name": "Orchidaceae family", "family": "Orchidaceae", "type": "Ornamental", "uses": ["Exotic flowers", "Decoration"]},
    {"name": "Bougainvillea", "sanskrit_name": "बूगनवेल (Buganvel)", "scientific_name": "Bougainvillea spp.", "family": "Nyctaginaceae", "type": "Ornamental", "uses": ["Colorful bracts", "Hedge"]},
    {"name": "Chrysanthemum", "sanskrit_name": "शेवन्ती (Shevanti)", "scientific_name": "Chrysanthemum spp.", "family": "Asteraceae", "type": "Ornamental", "uses": ["Flowers", "Tea"]},
    
    # FOREST TREES & TIMBER
    {"name": "Teak", "sanskrit_name": "शाक (Shaka)", "scientific_name": "Tectona grandis", "family": "Lamiaceae", "type": "Timber Tree", "uses": ["Premium timber", "Furniture", "Ships"]},
    {"name": "Sal", "sanskrit_name": "शाल (Shala)", "scientific_name": "Shorea robusta", "family": "Dipterocarpaceae", "type": "Timber Tree", "uses": ["Timber", "Resin", "Sacred"]},
    {"name": "Sandalwood", "sanskrit_name": "चन्दन (Chandana)", "scientific_name": "Santalum album", "family": "Santalaceae", "type": "Aromatic Tree", "uses": ["Fragrance", "Sacred", "Essential oil"]},
    {"name": "Banyan", "sanskrit_name": "वट (Vata)", "scientific_name": "Ficus benghalensis", "family": "Moraceae", "type": "Fig Tree", "uses": ["Shade", "Sacred", "Aerial roots"]},
    {"name": "Peepal", "sanskrit_name": "अश्वत्थ (Ashvattha)", "scientific_name": "Ficus religiosa", "family": "Moraceae", "type": "Fig Tree", "uses": ["Sacred", "Oxygen", "Shade"]},
    {"name": "Oak", "sanskrit_name": "शिलीन्ध्र (Shilindhra)", "scientific_name": "Quercus spp.", "family": "Fagaceae", "type": "Timber Tree", "uses": ["Timber", "Acorns"]},
    {"name": "Pine", "sanskrit_name": "सरल (Sarala)", "scientific_name": "Pinus spp.", "family": "Pinaceae", "type": "Conifer", "uses": ["Timber", "Resin", "Turpentine"]},
    {"name": "Eucalyptus", "sanskrit_name": "नीलगिरी (Nilagiri)", "scientific_name": "Eucalyptus globulus", "family": "Myrtaceae", "type": "Tree", "uses": ["Essential oil", "Timber", "Medicinal"]},
    {"name": "Mahogany", "sanskrit_name": "महोगनी (Mahogani)", "scientific_name": "Swietenia mahagoni", "family": "Meliaceae", "type": "Timber Tree", "uses": ["Premium timber", "Furniture"]},
    {"name": "Bamboo", "sanskrit_name": "वंश (Vamsha)", "scientific_name": "Bambusa spp.", "family": "Poaceae", "type": "Grass", "uses": ["Construction", "Furniture", "Fast growing"]},
    
    # PALMS & ORNAMENTAL TREES
    {"name": "Date Palm", "sanskrit_name": "खर्जूर (Kharjura)", "scientific_name": "Phoenix dactylifera", "family": "Arecaceae", "type": "Palm", "uses": ["Dates", "Sugar", "Timber"]},
    {"name": "Areca Palm", "sanskrit_name": "पूग (Puga)", "scientific_name": "Areca catechu", "family": "Arecaceae", "type": "Palm", "uses": ["Betel nut", "Decorative"]},
    {"name": "Christmas Tree", "sanskrit_name": "क्रिसमस वृक्ष", "scientific_name": "Picea abies", "family": "Pinaceae", "type": "Conifer", "uses": ["Ornamental", "Christmas decoration"]},
    {"name": "Money Plant", "sanskrit_name": "धन वृक्ष", "scientific_name": "Epipremnum aureum", "family": "Araceae", "type": "Indoor Plant", "uses": ["Air purification", "Decoration"]},
    {"name": "Snake Plant", "sanskrit_name": "सर्प पौधा", "scientific_name": "Sansevieria trifasciata", "family": "Asparagaceae", "type": "Indoor Plant", "uses": ["Air purification", "Low maintenance"]},
    
    # AQUATIC & WETLAND
    {"name": "Water Lily", "sanskrit_name": "कुमुदिनी (Kumudini)", "scientific_name": "Nymphaea spp.", "family": "Nymphaeaceae", "type": "Aquatic", "uses": ["Ornamental", "Flowers"]},
    {"name": "Water Hyacinth", "sanskrit_name": "जल कुंभी", "scientific_name": "Eichhornia crassipes", "family": "Pontederiaceae", "type": "Aquatic", "uses": ["Phytoremediation", "Can be invasive"]},
    
    # CEREALS & GRAINS
    {"name": "Rice", "sanskrit_name": "धान्य (Dhanya)", "scientific_name": "Oryza sativa", "family": "Poaceae", "type": "Cereal", "uses": ["Staple food", "Grain"]},
    {"name": "Wheat", "sanskrit_name": "गोधूम (Godhuma)", "scientific_name": "Triticum aestivum", "family": "Poaceae", "type": "Cereal", "uses": ["Flour", "Bread", "Staple"]},
    {"name": "Corn", "sanskrit_name": "मक्का (Makka)", "scientific_name": "Zea mays", "family": "Poaceae", "type": "Cereal", "uses": ["Food", "Animal feed", "Oil"]},
    {"name": "Sugarcane", "sanskrit_name": "इक्षु (Ikshu)", "scientific_name": "Saccharum officinarum", "family": "Poaceae", "type": "Grass", "uses": ["Sugar", "Jaggery", "Juice"]},
    
    # LEGUMES & PULSES  
    {"name": "Chickpea", "sanskrit_name": "चणक (Chanaka)", "scientific_name": "Cicer arietinum", "family": "Fabaceae", "type": "Pulse", "uses": ["Protein", "Food"]},
    {"name": "Peanut", "sanskrit_name": "मूंगफली (Mungphali)", "scientific_name": "Arachis hypogaea", "family": "Fabaceae", "type": "Legume", "uses": ["Oil", "Protein", "Snack"]},
    {"name": "Soybean", "sanskrit_name": "सोया (Soya)", "scientific_name": "Glycine max", "family": "Fabaceae", "type": "Legume", "uses": ["Protein", "Oil", "Tofu"]},
    
    # MEDICINAL (NON-AYURVEDIC)
    {"name": "Aloe", "sanskrit_name": "घृतकुमारी", "scientific_name": "Aloe vera", "family": "Asphodelaceae", "type": "Succulent", "uses": ["Skin care", "Burns", "Cosmetics"]},
    {"name": "Basil", "sanskrit_name": "तुलसी", "scientific_name": "Ocimum basilicum", "family": "Lamiaceae", "type": "Herb", "uses": ["Culinary", "Medicinal"]},
    {"name": "Lavender", "sanskrit_name": "लैवेंडर", "scientific_name": "Lavandula angustifolia", "family": "Lamiaceae", "type": "Herb", "uses": ["Fragrance", "Essential oil", "Relaxation"]},
    {"name": "Chamomile", "sanskrit_name": "कैमोमाइल", "scientific_name": "Matricaria chamomilla", "family": "Asteraceae", "type": "Herb", "uses": ["Tea", "Relaxation", "Sleep"]},
    {"name": "Peppermint", "sanskrit_name": "पुदीना", "scientific_name": "Mentha piperita", "family": "Lamiaceae", "type": "Herb", "uses": ["Flavoring", "Digestion", "Tea"]},
    
    # SHRUBS & BUSHES
    {"name": "Henna", "sanskrit_name": "मेंहदी (Mehandi)", "scientific_name": "Lawsonia inermis", "family": "Lythraceae", "type": "Shrub", "uses": ["Dye", "Hair color", "Body art"]},
    {"name": "Oleander", "sanskrit_name": "कनेर (Kaner)", "scientific_name": "Nerium oleander", "family": "Apocynaceae", "type": "Ornamental Shrub", "uses": ["Flowers", "Hedge", "Toxic"]},
    
    # CLIMBERS & VINES
    {"name": "Betel Leaf", "sanskrit_name": "ताम्बूल (Tambula)", "scientific_name": "Piper betle", "family": "Piperaceae", "type": "Vine", "uses": ["Chewing", "Digestive", "Cultural"]},
    {"name": "Ivy", "sanskrit_name": "लता", "scientific_name": "Hedera helix", "family": "Araliaceae", "type": "Vine", "uses": ["Ornamental", "Ground cover"]},
    
    # CACTI & SUCCULENTS
    {"name": "Cactus", "sanskrit_name": "कैक्टस", "scientific_name": "Cactaceae family", "family": "Cactaceae", "type": "Succulent", "uses": ["Ornamental", "Desert plant"]},
    {"name": "Jade Plant", "sanskrit_name": "जेड पौधा", "scientific_name": "Crassula ovata", "family": "Crassulaceae", "type": "Succulent", "uses": ["Ornamental", "Lucky plant"]},
    
    # FERNS & MOSSES
    {"name": "Fern", "sanskrit_name": "फर्न", "scientific_name": "Pteridophyta", "family": "Various", "type": "Fern", "uses": ["Ornamental", "Air purification"]},
    {"name": "Moss", "sanskrit_name": "काई (Kai)", "scientific_name": "Bryophyta", "family": "Various", "type": "Moss", "uses": ["Ground cover", "Moisture indicator"]}
]

print(f"Adding {len(all_plants)} diverse plants to the database...")
print("=" * 70)

inserted = 0
updated = 0

for plant in all_plants:
    existing = plants_collection.find_one({"name": plant["name"]})
    
    # Add full structure
    plant_doc = {
        "name": plant["name"],
        "sanskrit_name": plant.get("sanskrit_name", plant["name"]),
        "scientific_name": plant["scientific_name"],
        "botanical_synonyms": [],
        "family": plant["family"],
        "vernacular_names": {"Hindi": plant["name"], "English": plant["name"]},
        "synonyms": [],
        "gana": [],
        "types": [plant.get("type", "Plant")],
        "habit": plant.get("type", "Plant"),
        "habitat": "Various regions",
        "morphology": {
            "root": "Various types",
            "stem": "Varies by species",
            "leaf": "Varies by species",
            "flower": "Varies by species",
            "inflorescence": "Varies",
            "fruit": "Varies by species",
            "seeds": "Varies"
        },
        "description": f"{plant['name']} ({plant['scientific_name']}) is a {plant.get('type', 'plant')}. {', '.join(plant['uses'])}",
        "characteristics": plant["uses"],
        "rasa": [],
        "guna": [],
        "virya": "",
        "vipaka": "",
        "prabhava": "",
        "dosha_karma": {},
        "karma": [],
        "indication": [],
        "medicinal_properties": plant["uses"],
        "uses": plant["uses"],
        "therapeutic_uses": {
            "internal": [use for use in plant["uses"] if "Edible" in use or "Food" in use],
            "external": [use for use in plant["uses"] if "Edible" not in use and "Food" not in use]
        },
        "parts_used": ["Various parts"],
        "dosage": {},
        "chemical_constituents": [],
        "phyto_constituents": [],
        "modern_pharmacology": [],
        "research_updates": [],
        "formulations": [],
        "shodana": "",
        "adulterants": [],
        "contraindications": [],
        "substitutes": [],
        "references": [],
        "images_base64": []
    }
    
    if not existing:
        plants_collection.insert_one(plant_doc)
        inserted += 1
        print(f"✅ Added: {plant['name']} ({plant.get('type', 'Plant')})")
    else:
        # Update if exists but keep existing data
        plants_collection.update_one(
            {"name": plant["name"]},
            {"$set": {"types": [plant.get("type", "Plant")], "habit": plant.get("type", "Plant")}}
        )
        updated += 1

total = plants_collection.count_documents({})

print("=" * 70)
print(f"\n🎉 DATABASE UPDATE COMPLETE!")
print(f"✅ Total plants in database: {total}")
print(f"➕ Newly added: {inserted}")
print(f"🔄 Updated: {updated}")
print("\n📊 Plant Categories Added:")
print("  🍎 Fruit Trees (Mango, Apple, Banana, etc.)")
print("  🥬 Vegetables & Crops (Tomato, Potato, Onion, etc.)")
print("  🌺 Flowers & Ornamental (Rose, Jasmine, Lotus, etc.)")
print("  🌲 Forest & Timber Trees (Teak, Sal, Sandalwood, etc.)")
print("  🌾 Cereals & Grains (Rice, Wheat, Corn, etc.)")
print("  🌿 Herbs & Spices (Already included)")
print("  🏝️ Palms (Coconut, Date, Areca)")
print("  💧 Aquatic Plants (Lotus, Water Lily)")
print("  🌵 Cacti & Succulents")
print("  🪴 Indoor Plants (Money Plant, Snake Plant)")
print("=" * 70)

EOF
