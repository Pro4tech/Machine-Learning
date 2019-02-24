import tensorflow as tf
import cv2
import matplotlib as plt
from time import sleep  #Sleep Function is seletively being imported from the time Library
for i in range(5):
    print(i)
    sleep(5)   #delay of 5 seconds


print(tf.__version__)       #Version Check
print(cv2.__version__)       #Version Check
print(plt.__version__)       #Version Check
