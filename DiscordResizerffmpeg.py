from time import sleep
import ffmpeg
from pathlib import Path
import time
from PIL import Image
import math
import random
from natsort import os_sorted
import numpy

# frame by frame command ffmpeg -i file.mp4 image%2d.png
# compile ffmpeg -f concat -i images.txt  -c copy finalvideo.webm
# sound ffmpeg -f concat -i images.txt  -i rock.ogg -c copy finalvideo.webm

# frame by frame
rock = ffmpeg.input(r"E:/PythonScripts/zigar.mp4")
out = ffmpeg.output(rock, r"./.frames/image%2d.jpeg")
out.run()

# resize
a = random.randrange(150, 870)
b = random.randrange(150, 870)
i = 0
image_list = []
resized_images = []

myframes = Path("E:/PythonScripts/save/.frames")
for file in os_sorted(myframes.glob("*.jpeg")):
    imageopen = Image.open(file)
    image_list.append(imageopen)


for image in image_list:
    time = numpy.arange(0,2*math.pi,math.pi/20)
    i = i+1
    new_image = image.resize((time, time))
    resized_images.append(new_image)
    new_image.save('E:/PythonScripts/save/.resized/image0' + str(i)+'.jpeg')

# convert jpeg to webm
i = 0
my_path = Path('./.resized/')
for file in os_sorted(my_path.glob('*.jpeg')):
    i = i+1
    jpeg = ffmpeg.input(file)  
    out1 = ffmpeg.output(jpeg ,r"./.webmframes/rock"+str(i)+".webm")
    out1 = out1.run()

sleep(0.5)
text = ffmpeg.input("E:/PythonScripts/save/.webmframes/images.txt", f='concat' ,safe='0')
# audio = ffmpeg.input("E:/PythonScripts/save/zigggar.ogg")
textout = ffmpeg.output(text, "./rockout.webm", c='copy')
textout.run()
