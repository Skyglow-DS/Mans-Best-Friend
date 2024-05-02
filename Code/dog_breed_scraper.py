import os
import json
import time
import git
import requests
from bs4 import BeautifulSoup
from config import akc_url_base, repo_url
from config import dog_groups
from config import data_folder
from utils import check_directory


def scrape_dog_breeds(logging = False):
    check_directory(data_folder)
    # Check if dog_breeds.json exists
    if os.path.exists("./data/dog_breeds.json"):
        # If the file exists, read in the groups
        with open("./data/dog_breeds.json", "r") as json_file:
            dog_breeds = json.load(json_file)
        print("Successfully read file dog_breeds.json\n")
    if os.path.exists("./dog_breeds.json"):
        # If the file exists, read in the groups
        with open("./dog_breeds.json", "r") as json_file:
            dog_breeds = json.load(json_file)
        print("Successfully read file dog_breeds.json\n")
    ## Todo: Add pulling existing file from repo
    else:
        # If the file doesn't exist, scrape AKC.org, and save it to dog_breeds.json
        print("dog_breeds.json file not found. Pulling dog breeds from akc.org ...\n")
        dog_breeds = {}
        for dog in dog_groups:
            dog_breeds[dog] = []
            for i in range(4):
                pages = '/page/{}/'.format(str(i+1))
                url = akc_url_base + dog + pages
                print(url)
                time.sleep(5)
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
                breed_cards = soup.find_all("div", class_="breed-type-card mla mra bpm-mx2 contents-filter")
                if breed_cards:
                    for index, _ in enumerate(breed_cards):
                        dog_breeds[dog].append(breed_cards[index]['data-title'])
                        print(breed_cards[index]['data-title'])
        with open("./data/dog_breeds.json", "w") as json_file:
            json.dump(dog_breeds, json_file)
        print("\nDog breeds saved to dog_breeds.json")

    if logging:
        return dog_breeds
    else:
        return