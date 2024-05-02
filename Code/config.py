# Directory

data_folder = "./data/"
image_folder = "./data/Images/"
dog_group_folder = "./data/dog_groups/"

train_dir = 'data/train'
test_dir = 'data/test'
val_dir = 'data/validation'

model_train_dir = './data/train/working/'
model_test_dir = './data/test/working'

modeling_dir = [train_dir, test_dir, val_dir]
sample_img_loc = r'./data/train/sporting/n02099601_146.jpg'

small_groups = ['foundation-stock-service', 'miscellaneous-class']

# URLS

akc_url_base = "https://www.akc.org/dog-breeds/"
stanford_dataset_url = 'http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar'
repo_url = 'https://github.com/example/repository.git' ## Todo Add pulling from repo for scraper


# Global Variables

dog_groups = ['sporting'
              , 'toy'
              , 'hound'
              , 'working'
              , 'herding'
              , 'terrier'
              , 'non-sporting'
              , 'foundation-stock-service'
              , 'miscellaneous-class']

manual_dog_breeds = {
    'japanese_spaniel' : 'japanese_chin'
    , 'blenheim_spaniel' : 'cavalier_king_charles_spaniel'
    , 'walker_hound' : 'treeing_walker_coonhound'
    , 'boston_bull' : 'boston_terrier'
    , 'groenendael' : 'belgian_sheepdog'
    , 'brabancon_griffon' : 'brussels_griffon'
    , 'toy_poodle' : 'poodle_(toy)'
    , 'standard_poodle' : 'poodle_(standard)'
    }