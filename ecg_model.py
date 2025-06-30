import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.callbacks import ReduceLROnPlateau
import random, numpy as np, tensorflow as tf, os

seed = 42
os.environ['PYTHONHASHSEED'] = str(seed)
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)
#early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',      # What to monitor
    factor=0.5,              # Reduce LR by this factor (e.g., 0.001 → 0.0005)
    patience=5,              # Wait this many epochs with no improvement
    min_lr=1e-6,             # Don't reduce LR below this value
    verbose=1                # Print messages when LR changes
)

# ---------- Load Data ----------
def load_data(path, label_dict):
    data = []
    label = []
    for cat, label_value in label_dict.items():
        pic_list = os.path.join(path, cat)
        for img in os.listdir(pic_list):
            image_path = os.path.join(pic_list, img)
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (224, 224))
            data.append(image)
            label.append(label_value)
    return np.array(data), np.array(label)

# ---------- Label Mapping ----------
label_dict = {
    'ECG Images of Myocardial Infarction Patients (240x12=2880)': 0,
    'ECG Images of Patient that have History of MI (172x12=2064)': 1,
    'ECG Images of Patient that have abnormal heartbeat (233x12=2796)': 2,
    'Normal Person ECG Images (284x12=3408)': 3
}

# ---------- Load Training Data ----------
path = os.path.join(os.getcwd(), "train")
data, label = load_data(path, label_dict)
data = data.astype('float32') / 255.0
num_classes = len(label_dict)
label = keras.utils.to_categorical(label, num_classes)

# ---------- Train-Validation Split ----------
X_train, X_val, y_train, y_val = train_test_split(data, label, test_size=0.2, random_state=42)

# ---------- CNN Model ----------
model = Sequential()

# Block 1
model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(224, 224, 3)))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))

# Block 2
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))

# Block 3
model.add(Conv2D(64, (3, 3), activation='relu', padding='same', kernel_regularizer=l2(0.001)))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))

# Classifier
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))  # for 4 classes

# Compile
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# ---------- Train Model ----------
history = model.fit(
    X_train, y_train,
    epochs=35,
    batch_size=16,
    validation_data=(X_val, y_val),
    callbacks=[reduce_lr]
)

# ---------- Load Test Data ----------
test_path = os.path.join(os.getcwd(), "test")
test_data, test_label = load_data(test_path, label_dict)
test_data = test_data.astype('float32') / 255.0
test_label = keras.utils.to_categorical(test_label, num_classes)

# ---------- Evaluate Model ----------
test_loss, test_accuracy = model.evaluate(test_data, test_label)
print("CNN Accuracy:", test_accuracy)

model.save(os.path.join(os.getcwd(), "ecg_model.h5"))