from keras import Sequential, datasets, layers

(train_data, train_labels), (test_data, test_labels) = datasets.mnist.load_data()

model = Sequential()
model.add(layers.Input((28, 28, 1)))
model.add(layers.Conv2D(32, (5, 5), padding="same"))
model.add(layers.Flatten())
model.add(layers.Dense(128))
model.add(layers.Dense(10, "softmax"))

model.summary()
model.compile(
    loss="sparse_categorical_crossentropy", optimizer="Adam", metrics=["accuracy"]
)

model.fit(train_data, train_labels, epochs=10, validation_data=(test_data, test_labels))
