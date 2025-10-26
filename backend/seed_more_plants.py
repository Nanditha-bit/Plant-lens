#!/usr/bin/env python3
"""
Add more comprehensive Ayurvedic plants to the database
"""
from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/ayurvedic_plants")
client = MongoClient(MONGO_URL)
db = client.ayurvedic_plants
plants_collection = db.plants

# Additional comprehensive Ayurvedic plant data
additional_plants = [
    {
        "name": "Ashwagandha",
        "sanskrit_name": "अश्वगन्धा (Ashvagandha)",
        "scientific_name": "Withania somnifera (L.) Dunal",
        "botanical_synonyms": ["Physalis somnifera"],
        "family": "Solanaceae",
        "vernacular_names": {
            "Hindi": "असगंध (Asgandh)",
            "English": "Indian Ginseng, Winter Cherry",
            "Telugu": "అశ్వగంధ (Ashwagandha)",
            "Tamil": "அமுக்கரா (Amukkara)",
            "Kannada": "ಅಶ್ವಗಂಧ (Ashwagandha)",
            "Malayalam": "അശ്വഗന്ധ (Ashwagandha)",
            "Bengali": "অশ্বগন্ধা (Ashwagandha)",
            "Marathi": "आसंध (Asandh)",
            "Gujarati": "અસંધ (Asandh)"
        },
        "synonyms": [
            {"name": "Ashvagandha", "reason": "अश्व-गन्धा - Smells like horse (Ashva), gives horse-like strength and vitality"},
            {"name": "Varahakarni", "reason": "वराहकर्णी - Leaves resemble pig's ear in shape"},
            {"name": "Vajigandha", "reason": "वाजीगन्धा - Vaji means horse, gives strength like a horse"},
            {"name": "Balya", "reason": "बल्या - Strength-giving, improves physical power"}
        ],
        "gana": [
            {"author": "Charaka Samhita", "gana": "Balya (Strength promoting group)"},
            {"author": "Charaka Samhita", "gana": "Brimhaniya (Nourishing group)"},
            {"author": "Sushruta Samhita", "gana": "Vatashamana (Vata pacifying)"},
            {"author": "Bhavaprakasha", "gana": "Guduchyadi Varga"}
        ],
        "types": [
            "Cultivated variety (larger roots, preferred)",
            "Wild variety (smaller, less potent)"
        ],
        "habit": "Small evergreen shrub, 35-75 cm tall, erect branching",
        "habitat": "Native to India, found in dry regions, wastelands, cultivated throughout India, Mediterranean to South Asia",
        "morphology": {
            "root": "Fleshy, tuberous, stout, unbranched taproot, 30-45 cm long, externally brownish, internally whitish-yellow",
            "stem": "Branched, cylindrical, woody at base, herbaceous above, densely stellate-hairy, greyish-green",
            "leaf": "Simple, alternate, ovate to elliptic, 5-12 cm long, entire margin, stellate-hairy on both surfaces, petiolate",
            "flower": "Small, greenish-yellow, bell-shaped, 5-lobed corolla, solitary or in axillary clusters of 2-4",
            "inflorescence": "Axillary clusters or solitary",
            "fruit": "Berry, globose, 6-8 mm diameter, enclosed in persistent calyx, orange-red when ripe",
            "seeds": "Small, numerous, yellowish, reniform (kidney-shaped)"
        },
        "description": "Ashwagandha, known as Indian Ginseng, is one of the most powerful herbs in Ayurveda. It is classified as a Rasayana (rejuvenator) and is known for its adaptogenic properties. The root has a characteristic horse-like odor, hence the name 'Ashwagandha'. It is extensively used to improve strength, vitality, and overall health.",
        "characteristics": [
            "Small shrub with greyish-green stellate-hairy stems",
            "Characteristic horse-like odor in roots",
            "Orange-red berries enclosed in papery calyx",
            "Fleshy tuberous roots (main medicinal part)",
            "Greenish-yellow bell-shaped flowers",
            "Grows in dry, arid regions"
        ],
        "rasa": ["Tikta (Bitter)", "Kashaya (Astringent)", "Madhura (Sweet)"],
        "guna": ["Laghu (Light)", "Snigdha (Unctuous)"],
        "virya": "Ushna (Hot potency)",
        "vipaka": "Madhura (Sweet)",
        "prabhava": "Balya (Strength promoting), Rasayana (Rejuvenating), Vajikarana (Aphrodisiac)",
        "dosha_karma": {
            "Vata": "Strongly pacifies",
            "Pitta": "Neutral",
            "Kapha": "Slightly increases in excess"
        },
        "karma": [
            "Balya (Strength promoting)",
            "Rasayana (Rejuvenating)",
            "Vajikarana (Aphrodisiac)",
            "Nidrajanan (Sleep inducing)",
            "Vedanasthapana (Analgesic)",
            "Shothahara (Anti-inflammatory)",
            "Bruhmana (Nourishing)",
            "Medhya (Intellect promoting)"
        ],
        "indication": [
            "Kshaya (Emaciation, weakness)",
            "Shwasa (Dyspnoea)",
            "Kasa (Cough)",
            "Shotha (Inflammation)",
            "Vatavyadhi (Neurological disorders)",
            "Kshudraroga (Minor skin diseases)",
            "Prameha (Diabetes)",
            "Klaibya (Impotence)",
            "Nidranasha (Insomnia)",
            "Manasika Vikara (Mental disorders)"
        ],
        "medicinal_properties": [
            "Adaptogenic",
            "Anti-stress",
            "Immunomodulatory",
            "Anti-inflammatory",
            "Antioxidant",
            "Neuroprotective",
            "Anxiolytic",
            "Sedative-hypnotic",
            "Cardioprotective",
            "Thyroid modulating",
            "Anabolic",
            "Anti-arthritic",
            "Anti-cancer potential"
        ],
        "uses": [
            "Reduces stress, anxiety and depression",
            "Improves physical strength, stamina and muscle mass",
            "Enhances memory, cognitive function and concentration",
            "Treats insomnia and sleep disorders",
            "Supports thyroid function",
            "Boosts testosterone and male fertility",
            "Reduces inflammation and arthritis pain",
            "Manages diabetes and blood sugar",
            "Supports immune system",
            "Anti-aging and longevity"
        ],
        "therapeutic_uses": {
            "internal": [
                "Root powder (3-6g) with milk for strength and vitality",
                "Decoction for Vata disorders and weakness",
                "With ghee for nourishment and mental health",
                "Ashwagandharishta for general debility",
                "Capsules/tablets for stress management",
                "With honey for respiratory issues"
            ],
            "external": [
                "Paste applied on swellings and inflammations",
                "Oil for massage in arthritis and joint pain",
                "Poultice for wound healing"
            ]
        },
        "parts_used": ["Moola (Root) - primary", "Patra (Leaves)", "Beeja (Seeds)"],
        "dosage": {
            "Root powder (Churna)": "3-6 grams",
            "Decoction (Kwatha)": "50-100 ml",
            "Ashwagandharishta": "15-30 ml",
            "Extract/Capsules": "300-500 mg (standardized)"
        },
        "chemical_constituents": [
            "Withanolides (withanolide A, withaferin A) - 1.5%",
            "Alkaloids (withanine, somniferine, anaferine)",
            "Steroidal lactones",
            "Saponins (sitoindosides)",
            "Iron",
            "Choline",
            "Amino acids",
            "Fatty acids"
        ],
        "phyto_constituents": [
            "Steroidal compounds",
            "Alkaloids",
            "Saponins",
            "Amino acids"
        ],
        "modern_pharmacology": [
            "Adaptogenic: Modulates HPA axis, reduces cortisol levels",
            "Neuroprotective: Promotes neurogenesis, protects from neurodegeneration",
            "Anti-stress: Reduces anxiety markers, improves stress resilience",
            "Immunomodulatory: Enhances immune cell activity, increases antibody production",
            "Anti-inflammatory: Inhibits COX enzymes and inflammatory cytokines",
            "Thyroid stimulating: Increases T3 and T4 levels in hypothyroidism",
            "Anabolic: Increases muscle mass and strength through testosterone",
            "Cognitive enhancement: Improves memory through acetylcholine modulation",
            "Cardioprotective: Reduces cholesterol, protects heart from ischemia",
            "Anti-cancer: Withanolides show apoptotic effects on cancer cells"
        ],
        "research_updates": [
            "Clinical trials confirm significant reduction in stress and anxiety (up to 44%)",
            "Studies show increased muscle mass and strength in resistance training",
            "Research validates testosterone boosting effects (up to 17% increase)",
            "Cognitive studies show improved memory and executive function",
            "Sleep studies confirm improved sleep quality and reduced insomnia",
            "Thyroid research shows normalization of TSH in hypothyroid patients",
            "Anti-cancer research shows promise in various cancer types",
            "Fertility studies show improved sperm quality and count"
        ],
        "formulations": [
            "Ashwagandhadi Churna",
            "Ashwagandharishta",
            "Ashwagandhadi Lehya",
            "Ashwagandha Ghrita",
            "Ashwagandha Taila",
            "Brihat Ashwagandha Ghrita",
            "Ashwagandha capsules/tablets",
            "KSM-66 (standardized extract)"
        ],
        "shodana": "Not required. Roots are cleaned, dried and powdered. Quality roots should be fleshy, white inside, with strong odor.",
        "adulterants": [
            "Roots of other Withania species",
            "Physalis species",
            "Old, dried inferior quality roots"
        ],
        "contraindications": [
            "Pregnancy (may cause miscarriage in high doses)",
            "Hyperthyroidism (may increase thyroid hormones)",
            "Autoimmune diseases (may stimulate immune system)",
            "Surgery (discontinue 2 weeks before)",
            "High Pitta conditions in excess doses"
        ],
        "substitutes": [
            "Bala (Sida cordifolia) - for strength",
            "Shatavari - for Vata pacification"
        ],
        "references": [
            {
                "text": "अश्वगन्धा बल्या रस्याना वाजीकरणी बलप्रदा। वातश्लेष्मविकारघ्नी शोथहारी रसायनी॥",
                "verse": "Ashwagandha balya rasayana vajikarani balaprada, Vata shleshma vikaraghni shothahāri rasayani",
                "source": "Bhavaprakasha Nighantu, Guduchyadi Varga"
            },
            {
                "text": "Ashwagandha is described in Balya Gana (strength promoting group)",
                "verse": "Charaka's classification",
                "source": "Charaka Samhita, Sutra Sthana 4/13"
            }
        ],
        "images_base64": []
    },
    {
        "name": "Neem",
        "sanskrit_name": "निम्ब (Nimba)",
        "scientific_name": "Azadirachta indica A. Juss",
        "botanical_synonyms": ["Melia azadirachta"],
        "family": "Meliaceae",
        "vernacular_names": {
            "Hindi": "नीम (Neem)",
            "English": "Neem, Margosa tree",
            "Telugu": "వేప (Vepa)",
            "Tamil": "வேம்பு (Vembu)",
            "Kannada": "ಬೇವು (Bevu)",
            "Malayalam": "ആര്യവേപ്പ് (Aryaveppu)",
            "Bengali": "নিম (Nim)",
            "Marathi": "कडुलिंब (Kadulimb)",
            "Gujarati": "લીંબડો (Limbdo)"
        },
        "synonyms": [
            {"name": "Nimba", "reason": "निम्ब - Gives health (Nimbate swasthyam dadati)"},
            {"name": "Arishta", "reason": "अरिष्ट - Destroyer of diseases, never affected by disease itself"},
            {"name": "Pichumanda", "reason": "पिचुमण्ड - Having soft inflorescence"},
            {"name": "Prabhadra", "reason": "प्रभद्र - Very auspicious, beneficial"},
            {"name": "Sarva Roga Nivarini", "reason": "सर्वरोगनिवारिणी - Curer of all ailments"}
        ],
        "gana": [
            {"author": "Charaka Samhita", "gana": "Tiktaskandha (Bitter tasted group)"},
            {"author": "Charaka Samhita", "gana": "Lekhaniya (Scraping/reducing group)"},
            {"author": "Sushruta Samhita", "gana": "Aragvadhadi Gana"},
            {"author": "Bhavaprakasha", "gana": "Vatadi Varga"}
        ],
        "types": [
            "Nimba (Common Neem - Azadirachta indica)",
            "Maha Nimba (Great Neem - larger variety)"
        ],
        "habit": "Large evergreen tree, 15-20 meters tall, fast-growing",
        "habitat": "Native to India and Myanmar, cultivated throughout tropical and subtropical regions, drought-resistant",
        "morphology": {
            "root": "Deep tap root system with extensive laterals",
            "stem": "Straight trunk, rough furrowed bark, greyish-brown, exudes gum",
            "leaf": "Compound, imparipinnate, 20-40 cm long, 9-17 leaflets, serrated margins, glabrous, dark green above, pale beneath",
            "flower": "Small, white, fragrant, bisexual, 5-petaled, numerous",
            "inflorescence": "Axillary drooping panicles, 15-25 cm long",
            "fruit": "Drupe, ovoid-ellipsoid, 1.5-2 cm long, smooth, yellow-green when ripe",
            "seeds": "1-3 per fruit, ellipsoid, brown, rich in oil"
        },
        "description": "Neem is known as 'Sarva Roga Nivarini' - the curer of all ailments. It is one of the most versatile medicinal plants in Ayurveda. Every part of the tree has therapeutic value. It is extensively used for skin diseases, blood purification, fever, and as a general health tonic. Neem is also famous for its pest-repellent properties.",
        "characteristics": [
            "Large evergreen tree with dense crown",
            "Bitter taste in all parts",
            "White fragrant flowers in drooping clusters",
            "Yellow-green drupes",
            "Compound leaves with serrated leaflets",
            "Rough grey bark",
            "Very hardy and drought-resistant"
        ],
        "rasa": ["Tikta (Bitter) - predominant", "Kashaya (Astringent)"],
        "guna": ["Laghu (Light)", "Ruksha (Dry)"],
        "virya": "Sheeta (Cold potency)",
        "vipaka": "Katu (Pungent)",
        "prabhava": "Kushthaghna (Anti-leprotic), Krimighna (Anti-parasitic), Jvaraghna (Antipyretic)",
        "dosha_karma": {
            "Vata": "Increases in excess",
            "Pitta": "Strongly pacifies",
            "Kapha": "Pacifies"
        },
        "karma": [
            "Krimighna (Anthelmintic, antiparasitic)",
            "Kushthaghna (Anti-leprotic, skin disease remedy)",
            "Jvaraghna (Antipyretic)",
            "Kandughna (Anti-pruritic)",
            "Vranahara (Wound healing)",
            "Raktashodhaka (Blood purifier)",
            "Vishaghna (Anti-toxic)",
            "Shotha hara (Anti-inflammatory)",
            "Medohara (Anti-obesity)",
            "Pramehaghna (Anti-diabetic)"
        ],
        "indication": [
            "Kushtha (Skin diseases including leprosy)",
            "Jwara (Fever)",
            "Krimi (Worm infestation, parasites)",
            "Vrana (Wounds, ulcers)",
            "Kandu (Itching)",
            "Prameha (Diabetes)",
            "Arsha (Piles)",
            "Visha (Poisoning)",
            "Netra roga (Eye diseases)",
            "Danta roga (Dental diseases)"
        ],
        "medicinal_properties": [
            "Antibacterial (broad spectrum)",
            "Antifungal",
            "Antiviral",
            "Antiparasitic",
            "Anti-inflammatory",
            "Antipyretic",
            "Blood purifier",
            "Immunomodulatory",
            "Antidiabetic",
            "Hepatoprotective",
            "Antiulcer",
            "Contraceptive (spermicidal)",
            "Insecticidal"
        ],
        "uses": [
            "Treats all types of skin diseases (eczema, psoriasis, acne)",
            "Purifies blood and removes toxins",
            "Controls diabetes and blood sugar",
            "Treats fever (especially malarial)",
            "Dental care - prevents cavities, gum disease",
            "Wound healing and antiseptic",
            "Treats eye disorders",
            "Natural pesticide and insect repellent",
            "Boosts immune system",
            "Treats intestinal worms"
        ],
        "therapeutic_uses": {
            "internal": [
                "Leaf juice (10-20ml) for blood purification",
                "Bark decoction for fever and malaria",
                "Seed oil (few drops) for worm infestation",
                "Neem water (soaked overnight) for diabetes",
                "Tender leaves (2-3) chewed daily for general health"
            ],
            "external": [
                "Leaf paste for skin diseases and wounds",
                "Oil for skin problems and hair care",
                "Leaf decoction bath for skin diseases",
                "Twigs for teeth cleaning (datun)",
                "Seed cake as fertilizer and pesticide",
                "Smoke fumigation for purification"
            ]
        },
        "parts_used": ["Patra (Leaves)", "Twak (Bark)", "Pushpa (Flowers)", "Phala (Fruits)", "Beeja (Seeds)", "Taila (Oil)"],
        "dosage": {
            "Leaf powder (Churna)": "1-3 grams",
            "Leaf juice (Swarasa)": "10-20 ml",
            "Bark decoction (Kwatha)": "50-100 ml",
            "Seed oil": "5-10 drops (external) or 1-2 drops (internal)"
        },
        "chemical_constituents": [
            "Azadirachtin (key compound in seeds)",
            "Nimbin, Nimbidin",
            "Nimbidol",
            "Quercetin",
            "Beta-sitosterol",
            "Limonoids",
            "Triterpenoids",
            "Flavonoids",
            "Carotenoids"
        ],
        "phyto_constituents": [
            "Limonoids",
            "Triterpenoids",
            "Flavonoids",
            "Tannins"
        ],
        "modern_pharmacology": [
            "Antibacterial: Effective against Gram+ and Gram- bacteria",
            "Antifungal: Active against Candida and dermatophytes",
            "Antiviral: Shows activity against various viruses",
            "Antimalarial: Effective against Plasmodium species",
            "Hypoglycemic: Reduces blood glucose through multiple mechanisms",
            "Immunomodulatory: Enhances cell-mediated and humoral immunity",
            "Anti-inflammatory: Inhibits prostaglandin synthesis",
            "Hepatoprotective: Protects liver from toxins",
            "Contraceptive: Spermicidal and implantation prevention",
            "Antioxidant: Scavenges free radicals"
        ],
        "research_updates": [
            "WHO recognizes Neem as 'Tree of the 21st century'",
            "Studies confirm effectiveness against drug-resistant bacteria",
            "Research shows anti-cancer properties in various cancer types",
            "Clinical trials validate anti-diabetic effects",
            "Dental studies confirm prevention of plaque and gingivitis",
            "Dermatological research validates efficacy in psoriasis and eczema",
            "Agricultural research confirms safe biopesticide properties",
            "Antiviral studies show promise against dengue and other viruses"
        ],
        "formulations": [
            "Nimbadi Churna",
            "Nimbamritadi Eranda Taila",
            "Pancha Nimbadi Churna",
            "Neem capsules/tablets",
            "Neem oil",
            "Neem soap",
            "Neem tooth powder"
        ],
        "shodana": "Not required for most uses. For internal consumption, tender leaves should be washed thoroughly. Seeds are processed to extract oil.",
        "adulterants": [
            "Leaves of Melia azedarach (Bakayan) - similar appearance but less potent",
            "Other Meliaceae family members"
        ],
        "contraindications": [
            "Pregnancy (may cause abortion in high doses)",
            "Trying to conceive (spermicidal properties)",
            "Infants and young children (internal use)",
            "Prolonged use in high doses (may cause infertility)",
            "Very weak patients (extreme Ruksha and Tikta)"
        ],
        "substitutes": [
            "Karanja (Pongamia pinnata) - for skin diseases",
            "Kutaja (Holarrhena antidysenterica) - for intestinal parasites"
        ],
        "references": [
            {
                "text": "निम्बो निम्बितरोगाणाम् आरिष्टो रोगनाशनात्। पिचुमण्डः सुमनःप्रियः प्रभद्रश्च हिताहितः॥",
                "verse": "Nimbo nimbitaroganam arishto roganashanat, Pichumandah sumanahpriyah prabhadrash ca hitahitah",
                "source": "Bhavaprakasha Nighantu, Vatadi Varga"
            },
            {
                "text": "निम्बो हिमः पिचुमण्डः प्रभद्रः तिक्तको लघुः। कटुपाकरसः स्वादुस्तिक्तकश्च विशेषतः॥",
                "verse": "Properties of Neem",
                "source": "Raja Nighantu"
            }
        ],
        "images_base64": []
    },
    {
        "name": "Brahmi",
        "sanskrit_name": "ब्राह्मी (Brahmi)",
        "scientific_name": "Bacopa monnieri (L.) Pennell",
        "botanical_synonyms": ["Herpestis monniera", "Moniera cuneifolia"],
        "family": "Plantaginaceae (formerly Scrophulariaceae)",
        "vernacular_names": {
            "Hindi": "ब्राह्मी (Brahmi)",
            "English": "Water Hyssop, Thyme-leaved Gratiola",
            "Telugu": "బ్రాహ్మి (Brahmi)",
            "Tamil": "நீர்ப்பிரம்மி (Neerbrahmi)",
            "Kannada": "ಬ್ರಾಹ್ಮಿ (Brahmi)",
            "Malayalam": "ബ്രാഹ്മി (Brahmi)",
            "Bengali": "ব্রাহ্মী শাক (Brahmi Shak)",
            "Marathi": "ब्राह्मी (Brahmi)",
            "Gujarati": "બ્રાહ્મી (Brahmi)"
        },
        "synonyms": [
            {"name": "Brahmi", "reason": "ब्राह्मी - Improves intelligence (Brahma), sacred to Brahma"},
            {"name": "Saraswati", "reason": "सरस्वती - Named after goddess of knowledge, enhances learning"},
            {"name": "Matsyakshi", "reason": "मत्स्याक्षी - Leaves resemble fish eyes"},
            {"name": "Medhya", "reason": "मेध्या - Improves intellect and memory"},
            {"name": "Aindri", "reason": "ऐन्द्री - Related to Indra, king of gods"}
        ],
        "gana": [
            {"author": "Charaka Samhita", "gana": "Medhya Rasayana (Intellect promoting)"},
            {"author": "Charaka Samhita", "gana": "Prajasthapana (Fertility promoting)"},
            {"author": "Sushruta Samhita", "gana": "Vachadi Gana"},
            {"author": "Bhavaprakasha", "gana": "Guduchyadi Varga"}
        ],
        "types": [
            "Jala Brahmi (Aquatic - preferred)",
            "Sthala Brahmi (Terrestrial)"
        ],
        "habit": "Small creeping herb, prostrate, rooting at nodes",
        "habitat": "Grows in wetlands, marshy areas, rice fields, along water bodies throughout India",
        "morphology": {
            "root": "Fibrous, thin, arising from nodes",
            "stem": "Creeping, succulent, green, glabrous, rooting at nodes, 10-30 cm long",
            "leaf": "Simple, opposite, sessile, oblong-obovate, 0.5-2 cm long, entire margin, thick, succulent, 5-7 veined",
            "flower": "Small, white or pale purple, solitary, axillary, tubular with 5 lobes",
            "inflorescence": "Solitary flowers in leaf axils",
            "fruit": "Capsule, ovoid, acute apex, contains numerous tiny seeds",
            "seeds": "Minute, ellipsoid, ribbed"
        },
        "description": "Brahmi is one of the most important Medhya Rasayanas (nootropics) in Ayurveda. It is particularly revered for enhancing memory, learning capacity, and overall cognitive function. The herb is named after Brahma (the creator) and Saraswati (goddess of knowledge), indicating its supreme position in treating mental disorders and improving intellect.",
        "characteristics": [
            "Small succulent creeping herb",
            "Rooting at nodes",
            "Small oblong fleshy leaves",
            "White or pale purple flowers",
            "Grows in or near water",
            "Slightly bitter taste",
            "Cooling in nature"
        ],
        "rasa": ["Tikta (Bitter)", "Kashaya (Astringent)", "Madhura (Sweet - mild)"],
        "guna": ["Laghu (Light)"],
        "virya": "Sheeta (Cold potency)",
        "vipaka": "Madhura (Sweet)",
        "prabhava": "Medhya (Intellect promoting), Smriti Vardhana (Memory enhancing)",
        "dosha_karma": {
            "Vata": "Pacifies",
            "Pitta": "Pacifies",
            "Kapha": "Neutral"
        },
        "karma": [
            "Medhya (Intellect promoting)",
            "Smriti Vardhana (Memory enhancing)",
            "Nidrajanan (Sleep inducing - mild)",
            "Anulomana (Carminative)",
            "Rasayana (Rejuvenating)",
            "Unmadaghna (Anti-psychotic)",
            "Apasmaraghna (Anti-epileptic)",
            "Ayushya (Longevity promoting)"
        ],
        "indication": [
            "Smriti Hrasa (Loss of memory)",
            "Medha Daurbalya (Weak intellect)",
            "Unmada (Insanity, psychosis)",
            "Apasmara (Epilepsy)",
            "Jwara (Fever)",
            "Shotha (Inflammation)",
            "Shwasa (Dyspnoea)",
            "Kasa (Cough)",
            "Badhirya (Deafness)",
            "Swarabheda (Hoarseness of voice)"
        ],
        "medicinal_properties": [
            "Nootropic (cognitive enhancer)",
            "Neuroprotective",
            "Anxiolytic (anti-anxiety)",
            "Antioxidant",
            "Anti-inflammatory",
            "Adaptogenic",
            "Anti-epileptic",
            "Cardioprotective",
            "Bronchodilator",
            "Mild diuretic",
            "Anti-depressant"
        ],
        "uses": [
            "Enhances memory, learning, and concentration",
            "Treats mental disorders (anxiety, depression, ADHD)",
            "Improves cognitive function in elderly",
            "Treats epilepsy and seizures",
            "Reduces stress and promotes calmness",
            "Improves speech and voice disorders",
            "Treats insomnia and sleep disorders",
            "Supports brain health and neurogenesis",
            "Treats respiratory disorders",
            "Anti-aging for brain"
        ],
        "therapeutic_uses": {
            "internal": [
                "Fresh juice (5-10ml) for memory enhancement",
                "Powder (3-5g) with milk or ghee for intellect",
                "Brahmi Ghrita for mental disorders",
                "Decoction for respiratory issues",
                "Brahmi tea for stress relief",
                "Syrup for children's brain development"
            ],
            "external": [
                "Hair oil for hair growth and mental calmness",
                "Paste for skin inflammation",
                "Oil massage on head for better sleep and memory"
            ]
        },
        "parts_used": ["Panchanga (Whole plant)", "Patra (Leaves) - primary"],
        "dosage": {
            "Fresh juice (Swarasa)": "10-20 ml",
            "Powder (Churna)": "3-5 grams",
            "Decoction (Kwatha)": "50-100 ml",
            "Extract": "300-450 mg"
        },
        "chemical_constituents": [
            "Bacosides (A and B) - major active compounds",
            "Bacopasides I-XII",
            "Hersaponin",
            "Monnierin",
            "Brahmine (alkaloid)",
            "Nicotine (trace)",
            "Stigmasterol",
            "Beta-sitosterol"
        ],
        "phyto_constituents": [
            "Triterpenoid saponins (Bacosides)",
            "Alkaloids",
            "Sterols",
            "Flavonoids"
        ],
        "modern_pharmacology": [
            "Cognitive enhancement: Improves memory acquisition and retention",
            "Neuroprotection: Prevents neuronal damage from oxidative stress",
            "Anxiolytic: Reduces anxiety through GABAergic modulation",
            "Antioxidant: Strong free radical scavenging activity",
            "Anti-inflammatory: Inhibits inflammatory enzymes in brain",
            "Cholinergic: Enhances acetylcholine levels in hippocampus",
            "Neuroplasticity: Promotes dendritic branching and neurogenesis",
            "Anti-epileptic: Modulates neurotransmitter levels",
            "Adaptogenic: Normalizes stress response",
            "Cardiovascular: Improves blood flow to brain"
        ],
        "research_updates": [
            "Multiple clinical trials confirm memory enhancement in healthy adults",
            "Studies show effectiveness in ADHD children",
            "Research validates anxiety reduction comparable to lorazepam",
            "Cognitive studies in elderly show improved information processing",
            "Alzheimer's research shows potential in slowing cognitive decline",
            "ADHD trials show improved attention and reduced hyperactivity",
            "Depression studies show significant mood improvement",
            "Safety studies confirm long-term use is safe"
        ],
        "formulations": [
            "Brahmi Ghrita",
            "Saraswatarishta",
            "Brahmi Vati",
            "Brahmi Taila",
            "Brahmi Rasayana",
            "Brahmi capsules",
            "Brahmi syrup",
            "BacoMind (standardized extract)"
        ],
        "shodana": "Not required. Fresh plant should be washed thoroughly. Dried herb should be clean and free from foreign matter.",
        "adulterants": [
            "Centella asiatica (Mandukparni/Gotu Kola) - often confused and substituted",
            "Other aquatic herbs"
        ],
        "contraindications": [
            "Bradycardia (may slow heart rate further)",
            "Urinary obstruction (diuretic effect)",
            "Ulcers (may increase gastric secretions)",
            "Thyroid disorders (may affect thyroid hormones)",
            "Surgery (discontinue 2 weeks before)"
        ],
        "substitutes": [
            "Mandukaparni (Centella asiatica) - for cognitive enhancement",
            "Shankhapushpi - for memory improvement",
            "Jyotishmati - for intellect"
        ],
        "references": [
            {
                "text": "ब्राह्मी सरस्वती मेध्या वयःस्थापनचक्षुषी। स्मृतिमती त्वग्दोषघ्नी कुष्ठपाण्डुज्वरापहा॥",
                "verse": "Brahmi saraswati medhya vayasthapana chakshushi, Smritimath tvagdoshaghni kushthandupandujvarapaha",
                "source": "Bhavaprakasha Nighantu, Guduchyadi Varga"
            },
            {
                "text": "Brahmi is mentioned in Medhya Rasayana for intellect promotion",
                "verse": "चतुर्विधं हि मेध्यानाम्",
                "source": "Charaka Samhita, Chikitsa Sthana 1/3"
            }
        ],
        "images_base64": []
    }
]

def seed_more_plants():
    """Seed database with additional plants"""
    try:
        print("Adding more comprehensive Ayurvedic plants...")
        
        for plant_data in additional_plants:
            # Check if plant exists
            existing = plants_collection.find_one({"name": plant_data["name"]})
            
            if existing:
                # Update existing plant
                result = plants_collection.update_one(
                    {"name": plant_data["name"]},
                    {"$set": plant_data}
                )
                if result.modified_count > 0:
                    print(f"✅ Updated {plant_data['name']} with comprehensive data")
            else:
                # Insert new plant
                plants_collection.insert_one(plant_data)
                print(f"✅ Inserted {plant_data['name']} with comprehensive data")
        
        # Count total plants
        total = plants_collection.count_documents({})
        print(f"\n✅ Database now contains {total} comprehensive Ayurvedic plants!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    seed_more_plants()
