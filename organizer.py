"""This file organizes directories from the original images database"""

import os
import shutil

# Path to the images database
base_path = "images_database"

# List all folders within the images database
for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)

    # Check if it is a directory
    if os.path.isdir(folder_path):
        # Extract the name of the plant and the disease
        parts = folder.split(" - ")
        plant = parts[0].strip()  # Name of the plant
        disease = " - ".join(
            parts[1:]
        ).strip()  # Name of the disease (in case there are multiple "-")

        new_folder = os.path.join(base_path, plant)
        os.makedirs(new_folder, exist_ok=True)

        # Move and rename the images
        for img in os.listdir(folder_path):
            old_path = os.path.join(folder_path, img)

            # Create a new name with the disease at the beginning
            new_filename = f"{disease} - {img}"
            new_path = os.path.join(new_folder, new_filename)

            shutil.move(old_path, new_path)

        # Remove the empty folder
        shutil.rmtree(folder_path)

print("Reorganization completed!")
