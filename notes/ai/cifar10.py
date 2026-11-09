from pathlib import Path

import numpy as np
from keras import Sequential, layers

data_path = Path(__file__).resolve().parent / "cifar10.npz"

with np.load(data_path) as data:
    train_data: np.ndarray = data["x_train"]
    train_labels: np.ndarray = data["y_train"]
    test_data: np.ndarray = data["x_test"]
    test_labels: np.ndarray = data["y_test"]


train_data = train_data.astype("float32") / 255.0

model = Sequential()
model.add(layers.Input(shape=(32, 32, 3)))

model.add(layers.Conv2D(32, (2, 2), padding="same"))
model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))

model.add(layers.Dropout(0.1))
model.add(layers.Conv2D(32, (2, 2), padding="same"))
model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))

# model.add(layers.Dropout(0.5))
model.add(layers.Conv2D(128, (4, 4), padding="same"))
model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))

model.add(layers.Flatten())
model.add(layers.BatchNormalization())
model.add(layers.Dense(128, "softmax"))

model.summary()
model.compile(
    loss="sparse_categorical_crossentropy", optimizer="Adam", metrics=["accuracy"]
)
history = model.fit(
    train_data, train_labels, epochs=10, validation_data=(test_data, test_labels)
)

# original - a: 0.8651 l: 0.3965 va: 0.2332 vl: 4315.0918

# added conv2d(32, 3x3) layer - a: 0.8447 l: 0.4401 va: 0.2313 vl: 2083
# added batchnormalization & activation layers - a: 0.9503 l: 0.01452 - va: 0.4114 - vl: 649.5790
# added dropout(0.25) layer -a: 0.9770 l: 0.3481 va: 0.3982 vl: 481.9232
# added dropout(0.5), conv2d(16, 4x4), batchnorml, activation(relu) - 0.759 l: 0.68 va: 21

BATCH_SIZE = 164
EPOCHS = 25

class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]
