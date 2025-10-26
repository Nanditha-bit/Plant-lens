#!/usr/bin/env python3
"""
Comprehensive Ayurvedic Plants Database - Major medicinal plants
"""
from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/ayurvedic_plants")
client = MongoClient(MONGO_URL)
db = client.ayurvedic_plants
plants_collection = db.plants

comprehensive_plants = [
    # TURMERIC - Updated
    {
        "name": "Turmeric",
        "sanskrit_name": "हरिद्रा (Haridra)",
        "scientific_name": "Curcuma longa L.",
        "botanical_synonyms": ["Curcuma domestica"],
        "family": "Zingiberaceae",
        "vernacular_names": {
            "Hindi": "हल्दी (Haldi)",
            "English": "Turmeric",
            "Telugu": "పసుపు (Pasupu)",
            "Tamil": "மஞ்சள் (Manjal)",
            "Kannada": "ಅರಿಶಿನ (Arishina)",
            "Malayalam": "മഞ്ഞൾ (Manjal)",
            "Bengali": "হলুদ (Holud)",
            "Marathi": "हळद (Halad)",
            "Gujarati": "હળદર (Haldar)"
        },
        "synonyms": [
            {"name": "Haridra", "reason": "हरिद्रा - Yellow colored (Harit means yellow)"},
            {"name": "Kanchani", "reason": "काञ्चनी - Golden colored like gold"},
            {"name": "Nisha", "reason": "निशा - Beautiful like night"},
            {"name": "Gauri", "reason": "गौरी - Fair, bright yellow color"}
        ],
        "gana": [
            {"author": "Charaka Samhita", "gana": "Lekhaniya (Scraping group)"},
            {"author": "Charaka Samhita", "gana": "Kusthaghna (Anti-dermatosis)"},
            {"author": "Sushruta Samhita", "gana": "Haridra Gana"},
            {"author": "Bhavaprakasha", "gana": "Haritakyadi Varga"}
        ],
        "types": [
            "Haridra (Yellow turmeric - common)",
            "Daruharidra (Tree turmeric - Berberis aristata)",
            "Kanchani (Wild turmeric - Curcuma aromatica)"
        ],
        "habit": "Herbaceous rhizomatous perennial, 60-100 cm tall",
        "habitat": "Native to Southeast Asia, cultivated throughout India, tropical regions",
        "morphology": {
            "root": "Rhizome, cylindrical, branched, orange-yellow inside",
            "stem": "Pseudo-stem formed by leaf sheaths",
            "leaf": "Large, oblong-lanceolate, 30-60 cm long, entire margin",
            "flower": "Yellow-white, in spikes, bracteates",
            "inflorescence": "Spike, terminal, 10-15 cm long",
            "fruit": "Capsule (rarely produced)",
            "seeds": "Rarely formed, propagated by rhizomes"
        },
        "description": "Turmeric is one of the most researched Ayurvedic herbs. Known for powerful anti-inflammatory and antioxidant properties.",
        "characteristics": ["Yellow-orange rhizome", "Large leaves", "Aromatic", "Bitter-pungent taste"],
        "rasa": ["Tikta (Bitter)", "Katu (Pungent)"],
        "guna": ["Laghu (Light)", "Ruksha (Dry)"],
        "virya": "Ushna (Hot potency)",
        "vipaka": "Katu (Pungent)",
        "prabhava": "Varnya (Complexion enhancing), Kusthahara (Anti-dermatosis)",
        "dosha_karma": {"Vata": "Increases slightly", "Pitta": "Neutral", "Kapha": "Strongly pacifies"},
        "karma": ["Kushthaghna", "Varnya", "Vranahara", "Krimighna", "Deepana", "Raktashodhaka"],
        "indication": ["Kushtha", "Prameha", "Vrana", "Shotha", "Jwara", "Kandu"],
        "medicinal_properties": ["Anti-inflammatory", "Antioxidant", "Antiseptic", "Hepatoprotective", "Anticancer"],
        "uses": ["Skin diseases", "Wound healing", "Diabetes", "Liver protection", "Joint pain"],
        "therapeutic_uses": {
            "internal": ["Powder 1-3g with milk", "Decoction for inflammation"],
            "external": ["Paste for wounds", "Face mask for complexion"]
        },
        "parts_used": ["Rhizome"],
        "dosage": {"Powder": "1-3 grams", "Decoction": "50-100 ml"},
        "chemical_constituents": ["Curcumin", "Turmerone", "Zingiberene"],
        "phyto_constituents": ["Curcuminoids", "Essential oils"],
        "modern_pharmacology": ["COX-2 inhibitor", "Antioxidant", "Neuroprotective"],
        "research_updates": ["Alzheimer's prevention", "Cancer research", "Anti-inflammatory studies"],
        "formulations": ["Haridra Khanda", "Haridra capsules"],
        "shodana": "Not required",
        "adulterants": ["Lead chromate for color"],
        "contraindications": ["Bile duct obstruction", "Pregnancy in excess"],
        "substitutes": ["Daruharidra"],
        "references": [{"text": "हरिद्रा कटुका तिक्ता", "verse": "Properties", "source": "Bhavaprakasha"}],
        "images_base64": []
    },
    
    # AMLA - Updated
    {
        "name": "Amla",
        "sanskrit_name": "आमलकी (Amalaki)",
        "scientific_name": "Phyllanthus emblica L.",
        "botanical_synonyms": ["Emblica officinalis"],
        "family": "Phyllanthaceae",
        "vernacular_names": {
            "Hindi": "आंवला (Amla)",
            "English": "Indian Gooseberry",
            "Telugu": "ఉసిరికాయ (Usirikaya)",
            "Tamil": "நெல்லிக்காய் (Nellikkai)",
            "Kannada": "ನೆಲ್ಲಿಕಾಯಿ (Nellikayi)",
            "Malayalam": "നെല്ലിക്ക (Nellika)",
            "Bengali": "আমলকী (Amlaki)",
            "Marathi": "आवळा (Avala)",
            "Gujarati": "આમલા (Amla)"
        },
        "synonyms": [
            {"name": "Amalaki", "reason": "आमलकी - Sour fruit (Amla means sour)"},
            {"name": "Dhatri", "reason": "धात्री - Sustains like a mother/nurse"},
            {"name": "Vayastha", "reason": "वयस्था - Maintains youth"},
            {"name": "Shiva", "reason": "शिवा - Auspicious and beneficial"}
        ],
        "gana": [
            {"author": "Charaka Samhita", "gana": "Jeevaniya (Vitality promoting)"},
            {"author": "Charaka Samhita", "gana": "Vayasthapana (Anti-aging)"},
            {"author": "Charaka Samhita", "gana": "Kasahara (Anti-tussive)"}
        ],
        "types": ["Common variety", "Large fruited variety"],
        "habit": "Small to medium deciduous tree, 8-18 meters",
        "habitat": "Throughout India, tropical and subtropical regions",
        "morphology": {
            "root": "Tap root with laterals",
            "stem": "Spreading branches, smooth bark",
            "leaf": "Simple, subsessile, linear-oblong",
            "flower": "Small, greenish-yellow",
            "inflorescence": "Axillary clusters",
            "fruit": "Fleshy drupe, globose, pale yellow",
            "seeds": "Six, trigonous"
        },
        "description": "Richest natural source of Vitamin C. Supreme Rasayana in Ayurveda.",
        "characteristics": ["Round pale fruits", "Extremely sour", "High Vitamin C", "All parts medicinal"],
        "rasa": ["All five except Lavana", "Amla predominant"],
        "guna": ["Guru (Heavy)", "Ruksha (Dry)", "Sheeta (Cold)"],
        "virya": "Sheeta (Cold potency)",
        "vipaka": "Madhura (Sweet)",
        "prabhava": "Tridosha shamaka, Rasayana",
        "dosha_karma": {"Vata": "Pacifies", "Pitta": "Pacifies", "Kapha": "Pacifies"},
        "karma": ["Rasayana", "Chakshushya", "Jeevaniya", "Vayasthapana", "Raktapittahara"],
        "indication": ["Prameha", "Pandu", "Raktapitta", "Netra roga", "Daurbalya"],
        "medicinal_properties": ["Richest Vitamin C", "Antioxidant", "Immunomodulator", "Cardioprotective"],
        "uses": ["Immunity booster", "Eye health", "Hair growth", "Anti-aging", "Diabetes"],
        "therapeutic_uses": {
            "internal": ["Fresh fruit", "Powder with honey", "Chyawanprash"],
            "external": ["Hair oil", "Face pack"]
        },
        "parts_used": ["Fruit", "Seeds", "Leaves", "Bark"],
        "dosage": {"Powder": "3-6 grams", "Juice": "10-20 ml"},
        "chemical_constituents": ["Vitamin C", "Tannins", "Phyllaemblicin", "Gallic acid"],
        "phyto_constituents": ["Polyphenols", "Tannins"],
        "modern_pharmacology": ["Immunomodulator", "Antioxidant", "Hepatoprotective"],
        "research_updates": ["Cancer prevention", "Diabetes management", "Cardioprotection"],
        "formulations": ["Chyawanprash", "Amalaki Rasayana", "Triphala"],
        "shodana": "Not required",
        "adulterants": ["Inferior quality fruits"],
        "contraindications": ["Acute diarrhea"],
        "substitutes": ["Dhatri (synonymous)"],
        "references": [{"text": "आमलकी त्रिदोषहरा", "verse": "Tridosha pacifying", "source": "Classical texts"}],
        "images_base64": []
    },
    
    # GILOY
    {
        "name": "Giloy",
        "sanskrit_name": "गुडूची (Guduchi)",
        "scientific_name": "Tinospora cordifolia (Willd.) Miers",
        "botanical_synonyms": ["Tinospora glabra"],
        "family": "Menispermaceae",
        "vernacular_names": {
            "Hindi": "गिलोय (Giloy)",
            "English": "Heart-leaved Moonseed, Guduchi",
            "Telugu": "తిప్పతీగ (Tippatiga)",
            "Tamil": "சீந்தில் (Seenthil)",
            "Kannada": "ಅಮೃತವಲ್ಲಿ (Amruthavalli)",
            "Malayalam": "അമൃത് (Amrith)",
            "Bengali": "গুলঞ্চ (Gulancha)",
            "Marathi": "गुलवेल (Gulvel)",
            "Gujarati": "ગલો (Galo)"
        },
        "synonyms": [
            {"name": "Guduchi", "reason": "गुडूची - Protects body like a shield"},
            {"name": "Amrita", "reason": "अमृता - Divine nectar, life-giving"},
            {"name": "Amritvalli", "reason": "अमृतवल्ली - Creeper of immortality"},
            {"name": "Chinnaruha", "reason": "छिन्नरुहा - Grows even when cut"}
        ],
        "gana": [
            {"author": "Charaka Samhita", "gana": "Triptighna (Anti-satiation)"},
            {"author": "Charaka Samhita", "gana": "Dahaprashamana (Burning relief)"},
            {"author": "Sushruta Samhita", "gana": "Guduchyadi Gana"}
        ],
        "types": ["Guduchi growing on Neem tree (most potent)"],
        "habit": "Large climbing shrub, glabrous",
        "habitat": "Throughout India, tropical forests",
        "morphology": {
            "root": "Aerial roots, fleshy",
            "stem": "Climbing, succulent, creeping, develops aerial roots",
            "leaf": "Simple, alternate, heart-shaped, 5-10 cm",
            "flower": "Small, yellow, unisexual",
            "inflorescence": "Racemes",
            "fruit": "Drupe, red when ripe, pea-sized",
            "seeds": "Curved, white"
        },
        "description": "Known as 'Amrita' - the divine nectar. Supreme immunomodulator and antipyretic.",
        "characteristics": ["Heart-shaped leaves", "Climbing shrub", "Aerial roots", "Bitter stem"],
        "rasa": ["Tikta (Bitter)", "Kashaya (Astringent)"],
        "guna": ["Laghu (Light)", "Snigdha (Unctuous)"],
        "virya": "Ushna (Hot potency)",
        "vipaka": "Madhura (Sweet)",
        "prabhava": "Tridosha shamaka, especially Vata-Pitta",
        "dosha_karma": {"Vata": "Pacifies", "Pitta": "Strongly pacifies", "Kapha": "Pacifies"},
        "karma": ["Jwarahara", "Deepana", "Raktashodhaka", "Rasayana", "Balya"],
        "indication": ["Jwara", "Kushtha", "Pandu", "Prameha", "Shotha", "Vata Rakta"],
        "medicinal_properties": ["Immunomodulator", "Antipyretic", "Anti-inflammatory", "Hepatoprotective"],
        "uses": ["Chronic fever", "Dengue", "COVID support", "Immunity", "Diabetes", "Arthritis"],
        "therapeutic_uses": {
            "internal": ["Stem juice 10-20ml", "Powder 3-6g", "Guduchi Satva"],
            "external": ["Paste for skin diseases"]
        },
        "parts_used": ["Stem", "Leaves", "Root"],
        "dosage": {"Powder": "3-6 grams", "Juice": "10-20 ml", "Satva": "1-2 grams"},
        "chemical_constituents": ["Berberine", "Giloin", "Giloinin", "Palmatine"],
        "phyto_constituents": ["Alkaloids", "Glycosides", "Steroids"],
        "modern_pharmacology": ["Immunostimulant", "Antipyretic", "Anti-diabetic", "Hepatoprotective"],
        "research_updates": ["COVID-19 adjuvant", "Cancer research", "Autoimmune diseases"],
        "formulations": ["Guduchi Satva", "Amritarishta", "Guduchyadi Kwatha"],
        "shodana": "Not required",
        "adulterants": ["Other Tinospora species"],
        "contraindications": ["Pregnancy", "Autoimmune conditions (in some cases)"],
        "substitutes": ["Tinosporia crispa"],
        "references": [{"text": "गुडूचीमृतवल्ली स्यात् छिन्नरुहा", "verse": "Names", "source": "Bhavaprakasha"}],
        "images_base64": []
    },
    
    # SHATAVARI
    {
        "name": "Shatavari",
        "sanskrit_name": "शतावरी (Shatavari)",
        "scientific_name": "Asparagus racemosus Willd.",
        "botanical_synonyms": [],
        "family": "Asparagaceae (Liliaceae)",
        "vernacular_names": {
            "Hindi": "शतावर (Shatavar)",
            "English": "Wild Asparagus, Hundred Roots",
            "Telugu": "పిల్లి పీచర (Pilli Peechara)",
            "Tamil": "தண்ணீர்விட்டான் கிழங்கு (Thanneer Vittan)",
            "Kannada": "ಅಶಾಧಿ (Asadhi)",
            "Malayalam": "ശതാവരി (Shatavari)",
            "Bengali": "শতমূলী (Shatomuli)",
            "Marathi": "शतावरी (Shatavari)",
            "Gujarati": "શતાવરી (Shatavari)"
        },
        "synonyms": [
            {"name": "Shatavari", "reason": "शतावरी - Having hundred roots (Shata=hundred, Vari=roots)"},
            {"name": "Bahusuta", "reason": "बहुसुता - Promotes fertility, gives many children"},
            {"name": "Narayana Priya", "reason": "नारायणप्रिया - Beloved of women"},
            {"name": "Vrishya", "reason": "वृष्या - Aphrodisiac"}
        ],
        "gana": [
            {"author": "Charaka Samhita", "gana": "Balya (Strength promoting)"},
            {"author": "Charaka Samhita", "gana": "Jivaniya (Vitality promoting)"},
            {"author": "Charaka Samhita", "gana": "Vayasthapana (Anti-aging)"}
        ],
        "types": ["Common variety"],
        "habit": "Climbing herb with thorny stems",
        "habitat": "Throughout India, dry forests, rocky areas",
        "morphology": {
            "root": "Tuberous roots in clusters, fleshy, white",
            "stem": "Climbing, woody, armed with thorns",
            "leaf": "Modified into spines, needle-like",
            "flower": "Small, white, fragrant",
            "inflorescence": "Racemes",
            "fruit": "Berry, globose, purple-black when ripe",
            "seeds": "Black"
        },
        "description": "Queen of herbs for women's health. Supreme female reproductive tonic and galactagogue.",
        "characteristics": ["Thorny climber", "Tuberous roots", "White flowers", "Needle-like leaves"],
        "rasa": ["Madhura (Sweet)", "Tikta (Bitter)"],
        "guna": ["Guru (Heavy)", "Snigdha (Unctuous)"],
        "virya": "Sheeta (Cold potency)",
        "vipaka": "Madhura (Sweet)",
        "prabhava": "Stanya Janana (Galactagogue), Garbhashaya Balya",
        "dosha_karma": {"Vata": "Strongly pacifies", "Pitta": "Pacifies", "Kapha": "Increases"},
        "karma": ["Balya", "Rasayana", "Stanyajanan", "Shukrala", "Chakshushya"],
        "indication": ["Stanya Kshaya", "Kshaya", "Yoni Roga", "Shukra Kshaya", "Raktapitta"],
        "medicinal_properties": ["Galactagogue", "Rejuvenating", "Adaptogenic", "Hormone balancing"],
        "uses": ["Lactation", "Fertility", "Menopause", "Hormone balance", "Stress", "Immunity"],
        "therapeutic_uses": {
            "internal": ["Powder 3-6g with milk", "Churna for lactation"],
            "external": ["Not commonly used externally"]
        },
        "parts_used": ["Root"],
        "dosage": {"Powder": "3-6 grams", "Decoction": "50-100 ml"},
        "chemical_constituents": ["Steroidal saponins", "Shatavarins", "Asparagamine"],
        "phyto_constituents": ["Saponins", "Flavonoids", "Alkaloids"],
        "modern_pharmacology": ["Galactagogue", "Immunomodulator", "Adaptogenic", "Hormone modulator"],
        "research_updates": ["PCOS management", "Fertility enhancement", "Menopausal symptoms"],
        "formulations": ["Shatavari Ghrita", "Shatavari Churna", "Shatavari capsules"],
        "shodana": "Not required",
        "adulterants": ["Other Asparagus species"],
        "contraindications": ["Kidney stones", "High estrogen conditions"],
        "substitutes": ["Vidari"],
        "references": [{"text": "शतावरी मधुरा तिक्ता", "verse": "Properties", "source": "Bhavaprakasha"}],
        "images_base64": []
    },
    
    # TRIPHALA (Combination)
    {
        "name": "Triphala",
        "sanskrit_name": "त्रिफला (Triphala)",
        "scientific_name": "Combination of three fruits",
        "botanical_synonyms": [],
        "family": "Combretaceae",
        "vernacular_names": {
            "Hindi": "त्रिफला (Triphala)",
            "English": "Three Fruits",
            "Telugu": "త్రిఫల (Triphala)",
            "Tamil": "திரிபலா (Triphala)",
            "Kannada": "ತ್ರಿಫಲ (Triphala)",
            "Malayalam": "ത്രിഫല (Triphala)",
            "Bengali": "ত্রিফলা (Triphala)",
            "Marathi": "त्रिफळा (Triphala)",
            "Gujarati": "ત્રિફળા (Triphala)"
        },
        "synonyms": [
            {"name": "Triphala", "reason": "त्रिफला - Combination of three fruits"},
            {"name": "Tridoshahara", "reason": "त्रिदोषहर - Balances all three doshas"}
        ],
        "gana": [
            {"author": "Classical texts", "gana": "Rasayana (Rejuvenating)"},
            {"author": "Classical texts", "gana": "Anulomana (Laxative)"}
        ],
        "types": ["Equal combination of Haritaki, Bibhitaki, Amalaki"],
        "habit": "Three different trees combined",
        "habitat": "Throughout India",
        "morphology": {
            "root": "From three different trees",
            "stem": "From three different trees",
            "leaf": "From three different trees",
            "flower": "From three different trees",
            "inflorescence": "From three different trees",
            "fruit": "Three fruits: Haritaki, Bibhitaki, Amalaki",
            "seeds": "From respective fruits"
        },
        "description": "Most famous Ayurvedic formulation. Combination of Haritaki, Bibhitaki, and Amalaki. Complete Rasayana.",
        "characteristics": ["Powder form", "Dark brown color", "All six tastes except Lavana"],
        "rasa": ["All except Lavana"],
        "guna": ["Laghu (Light)", "Ruksha (Dry)"],
        "virya": "Ushna (Hot potency)",
        "vipaka": "Madhura (Sweet)",
        "prabhava": "Tridosha shamaka, Chakshushya, Rasayana",
        "dosha_karma": {"Vata": "Pacifies", "Pitta": "Pacifies", "Kapha": "Pacifies"},
        "karma": ["Anulomana", "Deepana", "Chakshushya", "Rasayana", "Medhya"],
        "indication": ["Vibandha", "Netra Roga", "Prameha", "Kushtha", "Shotha"],
        "medicinal_properties": ["Mild laxative", "Antioxidant", "Rejuvenating", "Eye health"],
        "uses": ["Constipation", "Digestion", "Eye health", "Weight loss", "Detoxification", "Anti-aging"],
        "therapeutic_uses": {
            "internal": ["Powder 3-6g at bedtime", "Decoction", "Tablets"],
            "external": ["Eye wash (decoction)", "Gargle for oral health"]
        },
        "parts_used": ["Three fruits"],
        "dosage": {"Powder": "3-6 grams", "Decoction": "50-100 ml"},
        "chemical_constituents": ["Tannins", "Gallic acid", "Vitamin C", "Chebulinic acid"],
        "phyto_constituents": ["Polyphenols", "Flavonoids"],
        "modern_pharmacology": ["Antioxidant", "Anti-inflammatory", "Immunomodulator", "Radioprotective"],
        "research_updates": ["Cancer prevention", "Cardiovascular protection", "Metabolic syndrome"],
        "formulations": ["Triphala Churna", "Triphala Ghrita", "Triphala tablets"],
        "shodana": "Not required",
        "adulterants": ["Substitution with inferior fruits"],
        "contraindications": ["Diarrhea", "Pregnancy (in high doses)"],
        "substitutes": ["Individual fruits can be used separately"],
        "references": [{"text": "त्रिफला त्रिदोषहरा", "verse": "Tridosha pacifying", "source": "Classical formulations"}],
        "images_base64": []
    },
    
    # GUGGUL
    {
        "name": "Guggul",
        "sanskrit_name": "गुग्गुलु (Guggulu)",
        "scientific_name": "Commiphora wightii (Arn.) Bhandari",
        "botanical_synonyms": ["Commiphora mukul"],
        "family": "Burseraceae",
        "vernacular_names": {
            "Hindi": "गुग्गल (Guggal)",
            "English": "Indian Bdellium, Mukul Myrrh",
            "Telugu": "మహిషాక్ష (Mahishaksha)",
            "Tamil": "குக்குலு (Kukkulu)",
            "Kannada": "ಗುಗ್ಗುಳ (Guggulu)",
            "Malayalam": "ഗുഗ്ഗുല് (Guggul)",
            "Bengali": "গুগুল (Gugul)",
            "Marathi": "गुगुळ (Gugul)",
            "Gujarati": "ગુગળ (Gugal)"
        },
        "synonyms": [
            {"name": "Guggulu", "reason": "गुग्गुलु - Protects from diseases"},
            {"name": "Mahishaksha", "reason": "महिषाक्ष - Buffalo-eyed (resemblance)"},
            {"name": "Kaushika", "reason": "कौशिक - From specific region"},
            {"name": "Devadhu", "reason": "देवधु - Divine smoke, used in fumigation"}
        ],
        "gana": [
            {"author": "Charaka Samhita", "gana": "Shotha Hara (Anti-inflammatory)"},
            {"author": "Sushruta Samhita", "gana": "Eladi Gana"}
        ],
        "types": ["Mahishaksha Guggulu (best quality)"],
        "habit": "Small thorny shrub or tree, 3-4 meters",
        "habitat": "Arid regions of Rajasthan, Gujarat, Karnataka",
        "morphology": {
            "root": "Woody root system",
            "stem": "Thorny, rough bark, exudes resin",
            "leaf": "Trifoliate, small, alternate",
            "flower": "Small, red, polygamous",
            "inflorescence": "Fascicles",
            "fruit": "Drupe, ovoid, red",
            "seeds": "One per fruit"
        },
        "description": "Gum resin obtained from stem. Famous for cholesterol management and arthritis.",
        "characteristics": ["Thorny shrub", "Aromatic gum resin", "Red flowers", "Trifoliate leaves"],
        "rasa": ["Tikta (Bitter)", "Katu (Pungent)", "Kashaya (Astringent)"],
        "guna": ["Laghu (Light)", "Ruksha (Dry)", "Tikshna (Sharp)"],
        "virya": "Ushna (Hot potency)",
        "vipaka": "Katu (Pungent)",
        "prabhava": "Medohara (Anti-obesity), Lekhaniya (Scraping)",
        "dosha_karma": {"Vata": "Pacifies", "Pitta": "Slightly increases", "Kapha": "Strongly pacifies"},
        "karma": ["Medohara", "Lekhaniya", "Shothaghna", "Vedanasthapana", "Deepana"],
        "indication": ["Medoroga", "Vata Rakta", "Kushtha", "Prameha", "Shotha"],
        "medicinal_properties": ["Hypolipidemic", "Anti-inflammatory", "Anti-obesity", "Thyroid stimulating"],
        "uses": ["High cholesterol", "Arthritis", "Weight loss", "Hypothyroidism", "Atherosclerosis"],
        "therapeutic_uses": {
            "internal": ["Purified resin 1-3g", "With Triphala for cholesterol"],
            "external": ["Fumigation", "Paste for wounds"]
        },
        "parts_used": ["Gum resin (Niryasa)"],
        "dosage": {"Purified resin": "1-3 grams"},
        "chemical_constituents": ["Guggulsterones", "Myrrhanone", "Guggulipid"],
        "phyto_constituents": ["Steroids", "Essential oils"],
        "modern_pharmacology": ["Hypolipidemic", "Anti-atherosclerotic", "Anti-inflammatory", "Thyroid stimulant"],
        "research_updates": ["Cholesterol management", "Atherosclerosis prevention", "Weight loss"],
        "formulations": ["Yogaraja Guggulu", "Triphala Guggulu", "Kaishore Guggulu"],
        "shodana": "Required - purification with Triphala decoction",
        "adulterants": ["Inferior resin", "Artificial gum"],
        "contraindications": ["Pregnancy", "Bleeding disorders", "Hyperthyroidism"],
        "substitutes": ["Commiphora species"],
        "references": [{"text": "गुग्गुलु कटुतिक्तं", "verse": "Properties", "source": "Bhavaprakasha"}],
        "images_base64": []
    }
]

def update_plants():
    """Update existing plants with comprehensive data"""
    try:
        print("Updating plants with comprehensive Ayurvedic data...")
        
        for plant_data in comprehensive_plants:
            existing = plants_collection.find_one({"name": plant_data["name"]})
            
            if existing:
                result = plants_collection.update_one(
                    {"name": plant_data["name"]},
                    {"$set": plant_data}
                )
                if result.modified_count > 0:
                    print(f"✅ Updated {plant_data['name']}")
            else:
                plants_collection.insert_one(plant_data)
                print(f"✅ Inserted {plant_data['name']}")
        
        total = plants_collection.count_documents({})
        print(f"\n✅ Database now has {total} plants with comprehensive data!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_plants()
