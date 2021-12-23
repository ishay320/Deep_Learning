from PIL import Image 
import numpy as np
import glob

SIZE_X = 360
SIZE_Y = 240

RATIO = SIZE_X / SIZE_Y

file_array = glob.glob("./data/*.jpg")
for pos in file_array:
    saving_pos = './data/train/'+pos.split("\\", 2)[1]

    image = np.array(Image.open(pos))

    # print("Before trimming:",im.shape)

    x = image.shape[0]
    y = image.shape[1]
    if(x<y/RATIO):
        length = int(x*RATIO)
    else:
        length = y

    # print(f"shape: {int(length/1.5)} {length}")
    im_trim = image[:int(length/RATIO), :length]
    # print("After trimming:",im_trim.shape)
    image_resize = Image.fromarray(im_trim).resize((SIZE_X,SIZE_Y))
    image_resize.save(saving_pos)
