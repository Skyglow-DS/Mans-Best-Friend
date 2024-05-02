import wget
import os
import tarfile
from config import stanford_dataset_url
from config import data_folder
from utils import check_directory

def download_dataset(save_dir=data_folder):
    check_directory(save_dir)
    tar_file = os.path.join(save_dir, 'images.tar')

    if os.path.exists(tar_file):
        print(f"The file '{tar_file}' already exists.")
    else:
        print("Downloading Stanford Dogs Dataset...")
        wget.download(stanford_dataset_url, out=save_dir)
        print("\nDownload complete!")

    print("Extracting dataset...")
    with tarfile.open(tar_file, 'r') as tar:
        tar.extractall(save_dir)
    print(f"\nExtraction complete! Extracted to {save_dir}")

    return 