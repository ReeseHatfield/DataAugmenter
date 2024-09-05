from tensorflow import keras
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
import sys
import os

def main():
    
    dir_name = sys.argv[1]
    print(dir_name)

    datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        vertical_flip = True, # check if this does what we think 
        brightness_range = (0.5, 1.5))
    
    files = os.listdir(dir_name)
    
    
    # only use image fields
    files = list(filter(lambda s: s.endswith((".jpg", ".jpeg", ".png")), files))
    
    
    


if __name__ == "__main__":
    main()