#!/usr/bin/env python3
"""
Comprehensive Ayurvedic Plants Database Seed Script
Includes detailed Ayurvedic properties, morphology, and therapeutic information
"""
from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/ayurvedic_plants")
client = MongoClient(MONGO_URL)
db = client.ayurvedic_plants
plants_collection = db.plants

# Comprehensive Ayurvedic plant data
ayurvedic_plants = [
    {
        "name": "Tulsi",
        "sanskrit_name": "तुलसी (Tulasi)",
        "scientific_name": "Ocimum sanctum L.",
        "botanical_synonyms": ["Ocimum tenuiflorum"],
        "family": "Lamiaceae (Labiatae)",
        "vernacular_names": {
            "Hindi": "तुलसी (Tulsi)",
            "English": "Holy Basil, Sacred Basil",
            "Telugu": "తులసి (Tulasi)",
            "Tamil": "துளசி (Tulasi)",
            "Kannada": "ತುಳಸಿ (Tulasi)",
            "Malayalam": "തുളസി (Thulasi)",
            "Bengali": "তুলসী (Tulsi)",
            "Marathi": "तुळस (Tulas)",
            "Gujarati": "તુલસી (Tulsi)"
        },
        "synonyms": [
            {"name": "Surasa", "reason": "सुरस - Having good/pleasant juice due to its aromatic taste"},
            {"name": "Devadundubhi", "reason": "देवदुन्दुभि - Auspicious like divine drum, sacred to gods"},
            {"name": "Sulabha", "reason": "सुलभा - Easily available everywhere"},
            {"name": "Bahumanjari", "reason": "बहुमञ्जरी - Having many flower clusters"},
            {"name": "Apetarakshasi", "reason": "अपेतराक्षसी - That which wards off evil spirits"}
        ],
        "gana": [
            {"author": "Charaka Samhita", "gana": "Shwasahara (Dyspnoea alleviating group)"},
            {"author": "Charaka Samhita", "gana": "Hikka Nigrahana (Hiccup relieving group)"},
            {"author": "Sushruta Samhita", "gana": "Eladi Gana"},
            {"author": "Bhavaprakasha", "gana": "Haritakyadi Varga"}
        ],
        "types": [
            "Krishna Tulsi (Black/Purple Tulsi - Ocimum sanctum)",
            "Shweta Tulsi (White/Green Tulsi - Ocimum basilicum)",
            "Vana Tulsi (Wild Tulsi - Ocimum gratissimum)",
            "Rama Tulsi (Bright leaf Tulsi)"
        ],
        "habit": "Small aromatic herb (30-60 cm tall), erect, much-branched",
        "habitat": "Native to Indian subcontinent, cultivated throughout India, found in tropical and subtropical regions",
        "morphology": {
            "root": "Tap root system with many lateral branches",
            "stem": "Quadrangular (four-sided), branched, pubescent, green or purple tinged, herbaceous when young becoming woody at base",
            "leaf": "Simple, opposite decussate, ovate to elliptic, 2-5 cm long, serrated margins, aromatic, green or purple, both surfaces pubescent, prominent veins",
            "flower": "Small, purplish or white, bilabiate (two-lipped), arranged in verticillasters along elongated spike-like racemes",
            "inflorescence": "Verticillaster arranged in elongated terminal and axillary racemes",
            "fruit": "Schizocarp splitting into 4 nutlets, small, ovoid, dark brown to black",
            "seeds": "Small, ovoid, mucilaginous when wet, yellowish-brown"
        },
        "description": "Sacred Basil or Tulsi is one of the most sacred plants in Hindu belief and Ayurveda. It is an aromatic, erect, much-branched herb with quadrangular stems and simple opposite leaves. The plant has been revered for thousands of years for its diverse healing properties and spiritual significance. Every part of the plant is used therapeutically.",
        "characteristics": [
            "Aromatic herb with distinct clove-like fragrance",
            "Quadrangular (square) stems",
            "Purple or green leaves with serrated margins",
            "Small purplish-white flowers in elongated spikes",
            "Strong aroma due to essential oils",
            "Sacred plant grown in Hindu households",
            "Adaptogenic properties"
        ],
        "rasa": ["Katu (Pungent)", "Tikta (Bitter)"],
        "guna": ["Laghu (Light)", "Ruksha (Dry)", "Tikshna (Sharp)"],
        "virya": "Ushna (Hot potency)",
        "vipaka": "Katu (Pungent)",
        "prabhava": "Has unique property to enhance immunity (Rasayana) and purify respiratory system",
        "dosha_karma": {
            "Vata": "Pacifies",
            "Pitta": "Slightly increases (due to Ushna Virya)",
            "Kapha": "Strongly pacifies"
        },
        "karma": [
            "Deepana (Appetizer)",
            "Pachana (Digestive)",
            "Krimighna (Anthelmintic)",
            "Shwasahara (Anti-asthmatic)",
            "Kasahara (Anti-tussive)",
            "Jwarahara (Antipyretic)",
            "Hridya (Cardiotonic)",
            "Kushthaghna (Anti-dermatosis)",
            "Vishaghna (Anti-toxic)",
            "Medohara (Anti-obesity)",
            "Raktashodhaka (Blood purifier)"
        ],
        "indication": [
            "Shwasa (Asthma, Dyspnoea)",
            "Kasa (Cough)",
            "Jwara (Fever)",
            "Hikka (Hiccough)",
            "Shoola (Colic pain)",
            "Aruchi (Anorexia)",
            "Krimi (Worm infestation)",
            "Kushtha (Skin diseases)",
            "Prameha (Diabetes)",
            "Hridroga (Heart diseases)",
            "Visha (Poisoning)"
        ],
        "medicinal_properties": [
            "Anti-inflammatory",
            "Antioxidant",
            "Immunomodulatory",
            "Adaptogenic",
            "Antimicrobial (antibacterial, antifungal, antiviral)",
            "Antipyretic",
            "Analgesic",
            "Hepatoprotective",
            "Cardioprotective",
            "Anti-stress",
            "Anti-carcinogenic",
            "Radioprotective",
            "Expectorant",
            "Diaphoretic"
        ],
        "uses": [
            "Treats respiratory disorders (cold, cough, asthma, bronchitis)",
            "Reduces stress, anxiety and mental fatigue",
            "Boosts immunity and general health",
            "Treats fever (especially malarial and dengue fever)",
            "Improves digestion and relieves gastric disorders",
            "Purifies blood and skin diseases",
            "Manages diabetes and metabolic disorders",
            "Treats cardiac disorders",
            "Relieves headache and stress-related disorders",
            "Used in treating insect bites and stings"
        ],
        "therapeutic_uses": {
            "internal": [
                "Fresh juice (5-10ml) with honey for cough and cold",
                "Decoction of leaves for fever and respiratory disorders",
                "Powder mixed with honey for asthma",
                "Tea/infusion for stress relief and immunity",
                "Seed decoction for urinary disorders",
                "Tulsi Ark (distillate) for fever and digestive issues"
            ],
            "external": [
                "Fresh juice applied on insect bites and skin infections",
                "Paste of leaves for ringworm and skin diseases",
                "Gargle with leaf decoction for oral infections and sore throat",
                "Essential oil for aromatherapy and stress relief",
                "Poultice of leaves for wound healing"
            ]
        },
        "parts_used": ["Panchanga (Whole plant)", "Patra (Leaves)", "Beeja (Seeds)", "Moola (Root)"],
        "dosage": {
            "Fresh juice (Swarasa)": "5-10 ml",
            "Powder (Churna)": "1-3 grams",
            "Decoction (Kwatha)": "50-100 ml",
            "Oil": "5-10 drops (external)",
            "Fresh leaves": "5-10 leaves can be chewed daily"
        },
        "chemical_constituents": [
            "Essential oil (0.7-1.0%): Eugenol, Methyl eugenol",
            "β-caryophyllene",
            "β-elemene",
            "Germacrene-D",
            "Ursolic acid",
            "Rosmarinic acid",
            "Apigenin",
            "Luteolin",
            "Orientin",
            "Molludistin"
        ],
        "phyto_constituents": [
            "Phenolic compounds",
            "Flavonoids",
            "Tannins",
            "Saponins",
            "Terpenoids",
            "Alkaloids (trace)"
        ],
        "modern_pharmacology": [
            "Immunomodulatory: Increases antibody production and T-cell count",
            "Adaptogenic: Helps body adapt to stress through HPA axis modulation",
            "Anti-inflammatory: Inhibits COX-2 enzyme and inflammatory mediators",
            "Antimicrobial: Effective against various bacteria, fungi, and viruses",
            "Antioxidant: Scavenges free radicals through phenolic compounds",
            "Hepatoprotective: Protects liver through antioxidant mechanisms",
            "Hypoglycemic: Reduces blood glucose through enhanced insulin secretion",
            "Cardioprotective: Reduces cholesterol and protects heart muscles",
            "Anticancer: Shows apoptotic effects on cancer cells",
            "Neuroprotective: Protects brain cells from oxidative stress"
        ],
        "research_updates": [
            "Recent studies show Tulsi effective in managing COVID-19 symptoms and boosting immunity",
            "Clinical trials demonstrate significant stress reduction and cognitive enhancement",
            "Research confirms hepatoprotective effects against drug-induced liver damage",
            "Studies show anti-diabetic properties comparable to standard drugs",
            "Essential oil shows strong antimicrobial activity against drug-resistant bacteria",
            "Adaptogenic properties validated through HPA axis modulation studies"
        ],
        "formulations": [
            "Tulsi Ark (Holy Basil Distillate)",
            "Sitopaladi Churna",
            "Talisadi Churna",
            "Lavangadi Vati",
            "Tribhuvan Kirti Rasa",
            "Chyawanprash (contains Tulsi)",
            "Tulsi Ghanvati (tablets)",
            "Tulsi drops",
            "Tulsi tea"
        ],
        "shodana": "Generally used fresh without purification. If dried, should be stored in airtight containers away from moisture.",
        "adulterants": [
            "Ocimum americanum (American Basil)",
            "Ocimum basilicum (Sweet Basil) - used as substitute but less potent",
            "Other Ocimum species with less medicinal value"
        ],
        "contraindications": [
            "Pregnancy and lactation (high doses)",
            "Bleeding disorders (due to blood-thinning properties)",
            "Hypoglycemia (may lower blood sugar further)",
            "Surgery (discontinue 2 weeks before due to blood-thinning effects)",
            "Hypothyroidism (may lower thyroid function)"
        ],
        "substitutes": [
            "Ajwain (Carom seeds) - for digestive issues",
            "Pudina (Mint) - for respiratory issues",
            "Vasa (Adhatoda vasica) - for cough and asthma"
        ],
        "references": [
            {
                "text": "तुलसी कटुका तिक्ता हृद्या दीपनपाचनी। कुष्ठकृमिकफश्वासविषमेहहरा लघु:॥",
                "verse": "Tulasi katuka tikta hridya deepana pachani, Kushthakrimi kapha shwasa visha meha hara laghu",
                "source": "Bhavaprakasha Nighantu, Haritakyadi Varga, Shloka 110"
            },
            {
                "text": "सुरसा बहुमञ्जरी देवदुन्दुभि सुलभा। ग्राम्या तुलसी तुलसी कृष्णा",
                "verse": "Properties and synonyms of Tulsi",
                "source": "Dhanvantari Nighantu"
            },
            {
                "text": "In the treatment of Shwasa (Asthma) and Kasa (Cough), Tulsi is mentioned",
                "verse": "Various shlokas",
                "source": "Charaka Samhita - Chikitsa Sthana"
            }
        ],
        "images_base64": []
    }
]

def seed_comprehensive_data():
    """Seed database with comprehensive Ayurvedic plant data"""
    try:
        print("Seeding comprehensive Ayurvedic plant data...")
        
        for plant_data in ayurvedic_plants:
            # Check if plant exists
            existing = plants_collection.find_one({"name": plant_data["name"]})
            
            if existing:
                # Update existing plant with comprehensive data
                result = plants_collection.update_one(
                    {"name": plant_data["name"]},
                    {"$set": plant_data}
                )
                if result.modified_count > 0:
                    print(f"✅ Updated {plant_data['name']} with comprehensive Ayurvedic data")
            else:
                # Insert new plant
                plants_collection.insert_one(plant_data)
                print(f"✅ Inserted {plant_data['name']} with comprehensive Ayurvedic data")
        
        print("\n✅ Comprehensive Ayurvedic data seeding complete!")
        print("\nData includes:")
        print("- Sanskrit names and synonyms with meanings")
        print("- Vernacular names in 9 Indian languages")
        print("- Gana classification (Charaka, Sushruta, Bhavaprakasha)")
        print("- Complete morphological description")
        print("- Rasapanchaka (Rasa, Guna, Virya, Vipaka, Prabhava)")
        print("- Dosha Karma and therapeutic actions")
        print("- Detailed indications and uses")
        print("- Chemical constituents and phytochemistry")
        print("- Modern pharmacology and research updates")
        print("- Formulations and dosages")
        print("- References with Sanskrit verses")
        print("- Adulterants and contraindications")
        
    except Exception as e:
        print(f"❌ Error seeding data: {e}")

if __name__ == "__main__":
    seed_comprehensive_data()
