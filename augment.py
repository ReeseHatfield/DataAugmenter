from tensorflow import keras
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from keras.utils import array_to_img, img_to_array, load_img
from keras._tf_keras.keras.utils import array_to_img, img_to_array, load_img

import sys
import os

def main():
    
    # path already resolved
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
    
    
    
    for file in files:
        cur_img = load_img(os.path.join(dir_name, file))
        
        data_arr = img_to_array(cur_img)
        
        # wtf is this?
        data_arr = data_arr.reshape((1, ) + data_arr.shape) 
        
        i = 0
        for batch in datagen.flow(data_arr, batch_size = 1,
                                save_to_dir ='out', 
                                save_prefix ='image', save_format ='jpeg'):
            i += 1
            if i > 10:
                break
    


if __name__ == "__main__":
    main()