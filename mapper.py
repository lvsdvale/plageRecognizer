"""This file creates a map of each plague in the images database"""

import json
import os

# Path to the images database
base_path = "images_database"

# Final dictionary
plant_diseases = {}

# Iterate over the plants
for plant in os.listdir(base_path):
    plant_path = os.path.join(base_path, plant)

    if os.path.isdir(plant_path):
        # Collect all diseases of the plant
        diseases_set = set()
        for img in os.listdir(plant_path):
            if " - " in img:
                disease = img.split(" - ")[0].strip()
                diseases_set.add(disease)

        # Create a mapping from 0 to n_diseases for each plant
        disease_to_class = {
            disease: i for i, disease in enumerate(sorted(diseases_set))
        }

        # Add to the final dictionary
        plant_diseases[plant] = disease_to_class

# Display the final dictionary
print(json.dumps(plant_diseases, indent=4, ensure_ascii=False))

# Optional: save to JSON
with open("map_plant_disease.json", "w", encoding="utf-8") as f:
    json.dump(plant_diseases, f, indent=4, ensure_ascii=False)
