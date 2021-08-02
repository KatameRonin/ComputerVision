from keras.datasets import cifar10
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense,Activation,Dropout,Flatten
from keras.layers.convolutional import Conv2D,MaxPooling2D
from keras.optimizers import RMSprop,SGD,Adam
import matplotlib.pyplot as plt

#CIFAR 10 has 60k imgages, 32x32 and RGB

IMG_CHANNELS=3
IMG_ROWS=32
IMG_COLUMNS=32

#constants

BATCH = 128
epoch=20
classes=10
verbose=1
validation=0.2
optimiser=RMSprop()

#LoadDataset

(X_train,Y_train),(X_test,Y_test)=cifar10.load_data()
print("X_train size ",X_train.shape[0])
print("X_test size: ",X_test.shape[0])
# print("No of features: ",Y_train.shape[1])

#One hot encode

Y_train=np_utils.to_categorical(Y_train,classes)
Y_test=np_utils.to_categorical(Y_test,classes)

# print("The class labels: ",Y_train[0])

#Normalise the data
X_train=X_train.astype('float32')
X_test=X_test.astype('float32')
X_train/=255
X_test/=255

#Creating the neural network
model=Sequential()
model.add(Conv2D(32,(3,3),strides=1,padding='same',input_shape=(IMG_ROWS,IMG_COLUMNS,IMG_CHANNELS)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(classes))
model.add(Activation('softmax'))
model.summary()

#training the model

model.compile(loss='categorical_crossentropy',optimizer=optimiser,metrics=['accuracy'])
model.fit(X_train,Y_train,batch_size=BATCH,epochs=epoch,validation_split=validation,verbose=1)
score=model.evaluate(X_test,Y_test,batch_size=BATCH,verbose=0)
# print("Test accuracy: ",score[1])

import numpy as np
import cv2

imgs=cv2.imread('dog.jpg')
imgs=cv2.resize(imgs,(32,32))

# model.predict_classes(imgs.reshape(1,32,32,3),batch_size=128,verbose=1)
model.predict_proba(imgs.reshape(1,32,32,3),batch_size=10,verbose=1)
