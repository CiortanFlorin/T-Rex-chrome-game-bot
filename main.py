import time
import pyautogui
from PIL import ImageGrab
import cv2
import numpy as np

#Coordinates for the region in which the images is analised, varies for each screen size and game variant
bbox = (260,450,400,485)

#Start the game
time.sleep(2)
pyautogui.press('up')

#Function to press the down key
def hit(key):
    pyautogui.keyDown(key)
    return

#Function that detects incoming cactus
def isCollide(data):
    for i in range(size[0]):
        for j in range(size[1]):
            print(data[i, j])
            if data[i, j] < 100:
                hit("up")
                return
while True:
    im = ImageGrab.grab(bbox)
    size = im.size
    #This is used to see the part of the screen which is used to monitor the objects
    image = ImageGrab.grab(bbox)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imshow("in_memory_to_disk.png", image)
    cv2.waitKey(1)
    #Convert the iamge to greyscale
    LA_im = im.convert('L')
    data = LA_im.load()

    isCollide(data)