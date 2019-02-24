import cv2,numpy,os
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

img_array=cv2.imread('/home/pritesh/Desktop/ML/python/Tensorflow/train_img/t1.jpeg',cv2.IMREAD_GRAYSCALE)
img_array=cv2.resize(img_array,(70,70))

plt.imshow(img_array,cmap=plt.cm.binary)
plt.show()

img_array=numpy.array(img_array).reshape(-1,70,70,1)

model=load_model('/home/pritesh/Desktop/ML/python/Tensorflow/models/imagerec.model')
predict=model.predict([img_array])
category=['Dog','Cat']
print("The Image is a",category[numpy.argmax(predict)])
