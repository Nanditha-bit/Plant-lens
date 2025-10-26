#!/usr/bin/env python3
"""
Script to download and add real plant images to the database
"""
import requests
import base64
from pymongo import MongoClient
import os

# Image URLs from vision expert
plant_images = {
    "Tulsi": "https://images.pexels.com/photos/1684990/pexels-photo-1684990.jpeg?w=400",
    "Ashwagandha": "https://images.unsplash.com/photo-1708361272696-df086f5d6d0e?w=400&q=80",
    "Neem": "https://images.unsplash.com/photo-1610643084001-0dac29ca151a?w=400&q=80",
    "Turmeric": "https://images.unsplash.com/photo-1701138161189-ef3bba4bf88a?w=400&q=80",
    "Brahmi": "https://images.unsplash.com/photo-1650306198616-f1bbb63de630?w=400&q=80",
    "Amla": "https://images.unsplash.com/photo-1610643084001-0dac29ca151a?w=400&q=80",
    "Giloy": "https://images.unsplash.com/photo-1588292126144-22f882c80648?w=400&q=80",
    "Shatavari": "https://images.unsplash.com/photo-1648987708175-8f64138c9223?w=400&q=80",
    "Guggul": "https://images.unsplash.com/photo-1711941340664-f07709e4f8a1?w=400&q=80",
    "Triphala": "https://images.pexels.com/photos/1684990/pexels-photo-1684990.jpeg?w=400"
}

def download_and_convert_to_base64(url):
    """Download image and convert to base64"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, timeout=15, headers=headers)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode('utf-8')
    except Exception as e:
        print(f"Error downloading {url}: {e}")
    return None

# Connect to MongoDB
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/ayurvedic_plants")
client = MongoClient(MONGO_URL)
db = client.ayurvedic_plants
plants_collection = db.plants

print("Downloading and adding plant images...")
updated_count = 0

for plant_name, image_url in plant_images.items():
    print(f"Processing {plant_name}...")
    base64_image = download_and_convert_to_base64(image_url)
    
    if base64_image:
        # Update plant in database
        result = plants_collection.update_one(
            {"name": plant_name},
            {"$set": {"images_base64": [base64_image]}}
        )
        if result.modified_count > 0:
            updated_count += 1
            print(f"  ✅ Updated {plant_name} with image ({len(base64_image)} chars)")
        else:
            print(f"  ⚠️ {plant_name} not found in database")
    else:
        print(f"  ❌ Failed to download image for {plant_name}")

print(f"\n✅ Successfully updated {updated_count} plants with images!")
