import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
mnist=tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test)=mnist.load_data()
x_test=tf.keras.utils.normalize(x_test,axis=1)

plt.imshow(x_test[67],cmap=plt.cm.binary)
plt.show()
print(y_test[67])
x_test=numpy.array(x_test).reshape(-1,28,28,1)

trainedModel=tf.keras.models.load_model('/home/pritesh/Desktop/ML/python/Tensorflow/Fashion_V.model')  #Loading the pre-Trained Model

predict=trainedModel.predict([x_test])
category=['top','Trouser','Pull-Over','Dress','Coat','Sandal','Shirt','Snicker','Bag','Ankle Boot']
print(numpy.argmax(predict[67]))
#print("The Image is a",category[numpy.argmax(predict)])
