import os
import zipfile
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop


#local_zip = '/tmp/horse-or-human.zip'
#zip_ref = zipfile.ZipFile(local_zip, 'r')
#zip_ref.extractall('/tmp/horse-or-human')
#zip_ref.close()
train_path = '../data_set/train/'
valid_path = '../data_set/validation/'

# Directory with our training horse pictures
train_pos_dir = os.path.join(train_path+'pos')
train_neg_dir = os.path.join(train_path+'neg')
train_pos_names = os.listdir(train_pos_dir)
train_neg_names = os.listdir(train_neg_dir)
train_total = len(train_pos_names) + len(train_neg_names)

valid_pos_dir = os.path.join(valid_path+'pos')
valid_neg_dir = os.path.join(valid_path+'neg')
valid_pos_names = os.listdir(valid_pos_dir)
valid_neg_names = os.listdir(valid_neg_dir)
valid_total = len(valid_pos_names) + len(valid_neg_names)



model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image 300x300 with 3 bytes color
    # This is the first convolution
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(800, 600, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    # The second convolution
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The third convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fourth convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fifth convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'),
    # Only 1 output neuron. It will contain a value from 0-1 where 0 for 1 class ('horses') and 1 for the other ('humans')
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()

model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(lr=0.001),
              metrics=['acc'])
# All images will be rescaled by 1./255
train_datagen = ImageDataGenerator(rescale=1/255)
valid_datagen = ImageDataGenerator(rescale=1/255)

# Flow training images in batches of 128 using train_datagen generator
train_generator = train_datagen.flow_from_directory(
        '../data_set/train',  # This is the source directory for training images
        target_size=(800, 600),  # All images will be resized to 150x150
        batch_size=8,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')
valid_generator = train_datagen.flow_from_directory(
        '../data_set/validation/',  # This is the source directory for training images
        target_size=(800, 600),  # All images will be resized to 150x150
        batch_size=8,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

history = model.fit_generator(
      train_generator,
      steps_per_epoch=train_total // 8,
      epochs=15,
      validation_data=valid_generator,
      validation_steps=valid_total // 8,
      verbose=1)
model.save_weights('../model/my_checkpoint-win')

