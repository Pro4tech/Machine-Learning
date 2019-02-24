#import of libraries
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import TensorBoard
import time

tensorboard=TensorBoard(log_dir='/home/pritesh/Desktop/ML/python/Tensorflow/logs/digitrec')

#Setting up of the Training and Testing Models
mnist=tf.keras.datasets.mnist      #Import of Datasets
(x_train,y_train),(x_test,y_test)=mnist.load_data() #Loading of Datasets

#The actual Image and Label passed to The code
"""
plt.imshow(x_train[9],cmap=plt.cm.binary)   #Displays the Image under testing
plt.show()                                  #Outputsthe graphical Image
print(y_train[9])                           #outputs the Label associatedwith that Image
"""
#Data Being Normalized(Made into a simplier)
"print(x_train)"  #The testing Tuple is being print
x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1)
"x_train=x_train/255.0"    #Data is being normalize #y_train is the set of label of images for training

#Setting up of Input Layers
model=tf.keras.models.Sequential() #Initialization of The Model Type-Flow
model.add(tf.keras.layers.Flatten(input_shape=(28,28))) #Flatten Allows to provide a linear Input data-stream

#Setting up of Hidden Layers
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))#Setting up the Hidden Layer:Enable the process of NN
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))#In tensorflow2.0 :tf.nn.relu is given as "relu" anf tf.nn.softmax is given as "softmax"
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))#Setting up of Hidden layer:Enable the Probability of Outputs

#Setting up of training Process
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])#Setting up the entire System
model.fit(x_train,y_train,epochs=10,callbacks=[tensorboard])#This is setting the training sysytem

#Evaluation of Trained Data
val_loss,val_acc=model.evaluate(x_test,y_test)
print("Loss:"+str(val_loss),"Acc:"+str(val_acc))

#Saving the Trained Model
model.save('digitrec.model')
