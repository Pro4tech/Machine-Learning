import numpy
import tensorflow as tf
from tensorflow.keras.layers import Dropout,Dense,LSTM,Flatten

mnist=tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test)=mnist.load_data()

x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1)

#x_train=numpy.array(x_train).reshape(-1,28,28,1)
#x_test=numpy.array(x_test).reshape(-1,28,28,1)

model=tf.keras.models.Sequential()

model.add(LSTM(64,input_shape=x_train.shape[1:],activation='relu',return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(64,activation='relu',return_sequences=True))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(50,activation='relu'))
model.add(Dense(10,activation='softmax'))
#opt=tf.keras.optimizer.Adam(le=1e-3)
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
print(x_train.shape)
model.fit(x_train,y_train,epochs=7)
val_loss,val_acc=model.evaluate(x_train,y_train)
print("loss:"+str(val_loss),"Acc:"+str(val_acc))

model.save('rnnTrial.model')
