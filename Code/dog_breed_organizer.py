import os
from fuzzywuzzy import process

from dog_breed_scraper import scrape_dog_breeds
from config import dog_groups, manual_dog_breeds
from config import image_folder, dog_group_folder
from utils import check_directory, move_files, move_directory, find_key

def create_groups(folder = True, logging = False, debugging = False):
    if len(os.listdir(image_folder)) < 100:
        print("Insufficient data. It's possible that the function has already been executed. Please verify the dataset location.")
        return (-1, -1)
    
    dog_breeds = scrape_dog_breeds(logging=True)
    dog_breeds_clean = {group: [breed.lower().replace(' ', '_') for breed in breeds] for group, breeds in dog_breeds.items()}

    check_directory(dog_group_folder)
    for group in dog_groups:
        group_folder = dog_group_folder + group
        check_directory(group_folder)

    not_found = []
    found = []

    for dog_image in os.listdir(image_folder):
        original_img_loc = os.path.join(image_folder, dog_image)
        group_found = False
        breed_name_parts = dog_image.split("-")[1:]  
        breed_name = "-".join(breed_name_parts).lower()

        print(f'\nSearching for {breed_name}')
        group = find_key(dog_breeds_clean, breed_name)

        if group:
            print("Found:", breed_name)
            group_folder = os.path.join(dog_group_folder, group)
            if debugging:
                print(f"Moved: {original_img_loc} to {group_folder}")
            else:
                if folder:
                    move_directory(original_img_loc, group_folder)
                else:
                    move_files(original_img_loc, group_folder)
            found.append(breed_name)
            group_found = True
            continue
        if not group_found:
            fuzzy_match = process.extractOne(breed_name, [item for sublist in dog_breeds_clean.values() for item in sublist])
            print(f"No exact match found for {breed_name}. Fuzzy match: {fuzzy_match[0]} (Score: {fuzzy_match[1]})")
            if fuzzy_match[1] > 80:
                group = find_key(dog_breeds_clean, fuzzy_match[0])
                group_folder = os.path.join(dog_group_folder, group)
                if debugging:
                    print(f"Fuzzy Moved: {original_img_loc} to {group_folder}")
                else:
                    if folder:
                        move_directory(original_img_loc, group_folder)
                    else:
                        move_files(original_img_loc, group_folder)
                found.append(breed_name)
                group_found = True
                continue
        if not group_found:
            manual_breed_name = manual_dog_breeds.get(breed_name)
            if manual_breed_name:
                group = find_key(dog_breeds_clean, manual_breed_name)
                group_folder = os.path.join(dog_group_folder, group)
                print(f"Failed fuzzy matching. Manual match: {breed_name} to {manual_breed_name}")
                if debugging:
                    print(f"Manual Moved: {original_img_loc} to {group_folder}")
                else:
                    if folder:
                        move_directory(original_img_loc, group_folder)
                    else:
                        move_files(original_img_loc, group_folder)
                    found.append(breed_name)
                group_found = True
                continue
        if not group_found:
            print(f"Not recognized by AKC: {breed_name}")
            not_found.append(breed_name)

        if not not_found:
            not_found = -1

    if logging:
        return found, not_found
    else:
        return