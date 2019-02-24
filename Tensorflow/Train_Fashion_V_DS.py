import numpy
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
from tensorflow.keras.callbacks import TensorBoard
import time

tensorboard=TensorBoard(log_dir='/home/pritesh/Desktop/ML/python/Tensorflow/logs/Fashion_V')

f_mnist=tf.keras.datasets.fashion_mnist
(x_train,y_train),(x_test,y_test)=f_mnist.load_data()

plt.imshow(x_train[0],cmap=plt.cm.binary)   #Displays the Image under testing
plt.show()                                  #Outputsthe graphical Image
print(y_train[0])

x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1)
print(x_train.shape)

x_train=numpy.array(x_train).reshape(-1,28,28,1)
x_test=numpy.array(x_test).reshape(-1,28,28,1)

model=tf.keras.Sequential()
model.add(Conv2D(64,(3,3),input_shape=x_train.shape[1:],activation='relu'))
model.add(MaxPooling2D(pool_size=(3,3)))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(3,3)))

model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(32,activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(256,activation=tf.nn.relu))
model.add(Dense(128,activation=tf.nn.relu))
model.add(Dense(10,activation=tf.nn.softmax))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=5,callbacks=[tensorboard])
val_loss,val_acc=model.evaluate(x_train,y_train)
print("loss:"+str(val_loss),"Acc:"+str(val_acc))

model.save('Fashion_V.model')
