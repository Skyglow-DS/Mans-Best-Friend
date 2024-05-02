from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import random
import os
from config import sample_img_loc, train_dir
from config import dog_groups

def sample_augmentation(static = False):
    try:
        img = load_img(sample_img_loc) #n02092339_14
    except:
        if static:
            random.seed(42)
        rand_group = random.choice([group for group in dog_groups if group not in ['foundation-stock-service', 'miscellaneous-class']])
        img_loc = train_dir + "/" + rand_group + '/'
        files = os.listdir(img_loc)
        random_file = random.choice(files)
        full_path = img_loc + random_file
        img = load_img(full_path)
    data = img_to_array(img)
    samples = expand_dims(data, 0)
    datagen = ImageDataGenerator(rotation_range=15,
                                width_shift_range=0.1,
                                height_shift_range=0.1,
                                shear_range=0.01,
                                zoom_range=[0.9, 1.25],
                                horizontal_flip=True,
                                fill_mode='nearest',
                                brightness_range=[0.5, 1.5])
    iter = datagen.flow(samples, batch_size=1)
    for i in range(9):
        plt.subplot(3, 3, i + 1)
        if i == 4:
            plt.imshow(data.astype('uint8'))
            plt.title('Original')
        else:
            plt.xticks([])
            plt.yticks([])
            batch = next(iter)
            image = batch[0].astype('uint8')
            plt.imshow(image)

    plt.tight_layout()
    plt.show()