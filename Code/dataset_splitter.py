import os
import random
import shutil
from config import dog_group_folder, train_dir, test_dir, small_groups, image_folder
from utils import check_directory
from sklearn.model_selection import train_test_split

def _split_data(source, train, test, split_ratio=(0.85, 0.15)):
    files = os.listdir(source)
    num_files = len(files)
    num_train = int(num_files * split_ratio[0])

    random.seed(42)
    random.shuffle(files)
    for i, file in enumerate(files):
        filepath = os.path.join(source, file)
        if i < num_train:
            shutil.copy(filepath, os.path.join(train, file))
        else:
            shutil.copy(filepath, os.path.join(test, file))

def split_dataset(split_ratio=(0.85, 0.15)):
    for dog_group in os.listdir(dog_group_folder):
        source = os.path.join(dog_group_folder, dog_group)
        train = os.path.join(train_dir, dog_group)
        test = os.path.join(test_dir, dog_group)
        check_directory(train, remove=True)
        check_directory(test, remove=True)
        _split_data(source, train, test, split_ratio)

    print("Data splitting completed successfully.")

def remove_small_groups():
    locs = [train_dir, test_dir]
    for loc in locs:
        for group in small_groups:
            try:
                full_path = loc + "/" + group
                shutil.rmtree(full_path)
            except OSError as e:
                raise OSError(f"Failed to remove directory '{full_path}': {e}")

# def split_train_test(image_folder = dog_group_folder):
#     classes = os.listdir(image_folder)

#     os.makedirs(train_dir, exist_ok=True)
#     os.makedirs(test_dir, exist_ok=True)

#     # Splitting each class folder into train and test
#     for class_name in classes:
#         class_dir = os.path.join(image_folder, class_name)
#         images = os.listdir(class_dir)
#         train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)

#         for image in train_images:
#             src = os.path.join(class_dir, image)
#             dst = os.path.join(train_dir, class_name, image)
#             os.makedirs(os.path.dirname(dst), exist_ok=True)
#             shutil.copy(src, dst)

#         for image in test_images:
#             src = os.path.join(class_dir, image)
#             dst = os.path.join(test_dir, class_name, image)
#             os.makedirs(os.path.dirname(dst), exist_ok=True)
#             shutil.copy(src, dst)
#     return 

def split_train_test(image_folder=dog_group_folder):
    classes = os.listdir(image_folder)
    classes = [class_name for class_name in os.listdir(image_folder) if not class_name.startswith('.')]

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Splitting each class folder into train and test
    for class_name in classes:
        class_dir = os.path.join(image_folder, class_name)
        subgroups = os.listdir(class_dir)

        train_class_dir = os.path.join(train_dir, class_name)
        test_class_dir = os.path.join(test_dir, class_name)
        os.makedirs(train_class_dir, exist_ok=True)
        os.makedirs(test_class_dir, exist_ok=True)

        for subgroup in subgroups:
            subgroup_dir = os.path.join(class_dir, subgroup)
            images = os.listdir(subgroup_dir)
            train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)

            for image in train_images:
                src = os.path.join(subgroup_dir, image)
                dst = os.path.join(train_class_dir, subgroup, image)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy(src, dst)

            for image in test_images:
                src = os.path.join(subgroup_dir, image)
                dst = os.path.join(test_class_dir, subgroup, image)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy(src, dst)