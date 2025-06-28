import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# ✅ Step 1: Define correct absolute paths to dataset
project_dir = os.getcwd()  # Should be "C:/Clean Tech"
train_dir = os.path.join(project_dir, 'dataset', 'train')
val_dir = os.path.join(project_dir, 'dataset', 'validation')

# ✅ Step 2: Preprocessing with Data Augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    zoom_range=0.2,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(rescale=1./255)

# ✅ Step 3: Load Data
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='sparse'  # for integer labels
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='sparse'
)

# ✅ Step 4: Load Pre-trained VGG16 (exclude top layers)
vgg_base = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
vgg_base.trainable = False  # freeze convolutional base

# ✅ Step 5: Add Custom Classifier
model = Sequential([
    vgg_base,
    Flatten(),
    Dropout(0.5),
    Dense(128, activation='relu'),
    Dense(3, activation='softmax')  # 3 output classes
])

# ✅ Step 6: Compile the Model
model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# ✅ Step 7: Define Training Callbacks
callbacks = [
    EarlyStopping(patience=5, restore_best_weights=True),
    ModelCheckpoint('healthy_vs_rotten.h5', save_best_only=True)
]

# ✅ Step 8: Train the Model
model.fit(
    train_generator,
    epochs=20,
    validation_data=val_generator,
    callbacks=callbacks
)

# ✅ Step 9: Save Final Model (just in case)
model.save('healthy_vs_rotten.h5')
print("✅ Model saved successfully as healthy_vs_rotten.h5")