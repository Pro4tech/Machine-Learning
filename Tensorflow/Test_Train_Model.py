import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
mnist=tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test)=mnist.load_data()
x_test=tf.keras.utils.normalize(x_test,axis=1)

plt.imshow(x_test[67],cmap=plt.cm.binary)
plt.show()
print(y_test[67])

trainedModel=tf.keras.models.load_model('digitrec.model')  #Loading the pre-Trained Model

predict=trainedModel.predict([x_test])
print(numpy.argmax(predict[67]))    #numpy.argmax:It returns the location of the highest number in the Tuple
