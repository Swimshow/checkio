'''
Created on Feb 27, 2017

@author: Daniel
'''
from PIL import Image
import os

os.chdir('C:\wamp64\www\Testing\TwitterBot\Resources')
count =0

for f in os.listdir('.'):
    if(f.endswith('.jpg')):
        count=count+1
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save('ProperPics/{}.jpg'.format(count))
        
