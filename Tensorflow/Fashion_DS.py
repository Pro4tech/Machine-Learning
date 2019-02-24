import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import TensorBoard
import time

tensorboard=TensorBoard(log_dir='/home/pritesh/Desktop/ML/python/Tensorflow/logs/Fashion')

f_mnist=tf.keras.datasets.fashion_mnist
(x_train,y_train),(x_test,y_test)=f_mnist.load_data()

plt.imshow(x_train[0],cmap=plt.cm.binary)   #Displays the Image under testing
plt.show()                                  #Outputsthe graphical Image
print(y_train[0])

x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1)

model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))

model.add(tf.keras.layers.Dense(256,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(256,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=10,callbacks=[tensorboard])
val_loss,val_acc=model.evaluate(x_train,y_train)
print("loss:"+str(val_loss),"Acc:"+str(val_acc))

model.save('Fashion.model')
