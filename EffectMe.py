'''
Created on Feb 27, 2017

@author: Daniel
'''
from PIL import Image,ImageFilter
import os
from numpy.random import random
from random import randint


os.chdir('C:\wamp64\www\Testing\TwitterBot\Resources\ProperPics')

count = randint(1,21)
print(count)

path = str(count)

image = Image.open(path+".jpg")
image.show()
os.chdir('C:\wamp64\www\Testing\TwitterBot\Resources\ProperPics\EffectedPics')
image.filter(ImageFilter.GaussianBlur(5)).save(path+"fx.jpg")

        
