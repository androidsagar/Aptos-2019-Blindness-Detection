from constants import *
import os
import keras
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Input, MaxPooling2D
from keras.models import Model
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
import pandas as pd
from main import get_data_frame

input_layer = Input(shape=(base_size, base_size, 3), name='input_layer')
layer = Conv2D(32, kernel_size=3, activation='relu', name='conv_1')(input_layer)
layer = MaxPooling2D(pool_size=(3, 3), name='max_pool_1')(layer)
layer = Conv2D(32, kernel_size=4, activation='tanh', name='conv_2')(layer)
layer = Dense(units=32, activation='relu', name='fc_1')(layer)
layer = Conv2D(64, kernel_size=4, activation='relu', name='conv_3')(layer)
layer = Flatten(name='flatten_1')(layer)
layer = Dense(64, activation='selu', name='fc2')(layer)
layer = Dense(32, activation='selu', name='fc3')(layer)
layer = Dense(8, activation='selu', name='fc4')(layer)
output = Dense(5, activation='softmax', name='output_layer')(layer)

model = Model(inputs=input_layer, outputs=output)

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

generator = ImageDataGenerator(validation_split=0.2)
csv = get_data_frame()
train_batches = generator.flow_from_dataframe(dataframe=csv, directory=train_images_final, x_col='name',
                                              y_col='code', target_size=(base_size, base_size), subset='training',
                                              batch_size=batch_size)
valid_batches = generator.flow_from_dataframe(dataframe=csv, directory=train_images_final, x_col='name',
                                              y_col='code', target_size=(base_size, base_size),
                                              subset='validation', batch_size=batch_size)

history = model.fit_generator(train_batches, steps_per_epoch=train_batches.samples / 32, validation_data=valid_batches,
                              validation_steps=valid_batches.samples / 32, epochs=100, verbose=1, shuffle=False,
                              workers=8)

# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('valid model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('valid model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
