import cv2
# import  PIL 
# from PIL import Image
import numpy as np


def collage_maker(image1, image2, name):
    i1 = cv2.imread(image1)
    i2 = cv2.imread(image2)
    img1 = cv2.resize(i1,(400,400),interpolation = cv2.INTER_LINEAR)
    img2 = cv2.resize(i2,(400,400),interpolation = cv2.INTER_LINEAR)
    collage = np.vstack((img1, img2))
    cv2.imwrite(name,collage)


# To Run The Above Function
collage_maker("image1.jpg", "image2.jpg", "new.jpg")
