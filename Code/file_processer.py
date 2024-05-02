from download_dataset import download_dataset
from dog_breed_scraper import scrape_dog_breeds
from dog_breed_organizer import create_groups
from dataset_splitter import split_dataset

def run_all():
    print("Running download_dataset()\n")
    download_dataset()
    print("Running scrape_dog_breeds()\n")
    scrape_dog_breeds()
    print("Running create_groups()\n")
    create_groups()
    print("Running split_dataset()\n")
    split_dataset()