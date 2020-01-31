import os, shutil
from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator


base_dir = 'C:/Users\Hp\Desktop/intersection'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')
train_cats_dir = os.path.join(train_dir, 'intersection')
train_dogs_dir = os.path.join(train_dir, 'non_intersection')
validation_cats_dir = os.path.join(validation_dir, 'intersection')
validation_dogs_dir = os.path.join(validation_dir, 'non_intersection')
test_cats_dir = os.path.join(test_dir, 'intersection')
test_dogs_dir = os.path.join(test_dir, 'non_intersection')

train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(train_dir,target_size=(500, 500),batch_size=20,class_mode='binary')
validation_generator = test_datagen.flow_from_directory(validation_dir,target_size=(500, 500),batch_size=20,class_mode='binary')


#train_datagen = ImageDataGenerator(rescale=1./255,rotation_range=40,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,)
#test_datagen = ImageDataGenerator(rescale=1./255)
#train_generator = train_datagen.flow_from_directory(train_dir,target_size=(15000, 15000),batch_size=32,class_mode='binary')
#validation_generator = test_datagen.flow_from_directory(validation_dir,target_size=(15000, 15000),batch_size=32,class_mode='binary')



model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu',input_shape=(500, 500, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(256, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(512, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))


model.add(layers.Flatten())
model.add(layers.Dropout(0.5))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer=optimizers.RMSprop(lr=1e-4),metrics=['acc'])
for data_batch, labels_batch in train_generator:
    print('data batch shape:', data_batch.shape)
    print('labels batch shape:', labels_batch.shape,labels_batch)
    break
history = model.fit_generator(train_generator,steps_per_epoch=500,epochs=30,validation_data=validation_generator,validation_steps=50)
#history = model.fit_generator(train_generator,steps_per_epoch=500,epochs=100,validation_data=validation_generator,validation_steps=50)
model.save('itersection_data_augmetatio_1.h5')

import matplotlib.pyplot as plt
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()