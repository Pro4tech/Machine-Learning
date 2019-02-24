import pickle
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
from tensorflow.keras.callbacks import TensorBoard
import time

tensorboard=TensorBoard(log_dir='/home/pritesh/Desktop/ML/python/Tensorflow/logs/Cat_Dog')

x=pickle.load(open('/home/pritesh/Desktop/ML/python/Tensorflow/pickle/x.pickle','rb'))
y=pickle.load(open('/home/pritesh/Desktop/ML/python/Tensorflow/pickle/y.pickle','rb'))

print(x.shape)

x=x/255

model=Sequential()

model.add(Conv2D(64,(3,3),input_shape=x.shape[1:],activation='relu'))
model.add(MaxPooling2D(pool_size=(3,3),))
model.add(Conv2D(64,(3,3),input_shape=x.shape[1:],activation='relu'))
model.add(MaxPooling2D(pool_size=(3,3),))

model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(32,activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(2,activation='softmax'))    #other option 'Sigmod'

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x,y,epochs=5,callbacks=[tensorboard])
model.save('imagerec.model')
