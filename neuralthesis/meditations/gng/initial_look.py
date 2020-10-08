import numpy as np
from keras import Sequential
from keras.layers import Dense
from keras.datasets import mnist
import keras



(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1]*X_train.shape[2])
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1]*X_test.shape[2])

X_train = X_train / 255.0

Y_train, Y_test = keras.utils.to_categorical(y_train, 10), keras.utils.to_categorical(y_test, 10)
X_test = X_test / 255.0

X_train, Y_train = X_train[:4000], Y_train[:4000]
EPOCH = 5
HIDDEN_DIM = 10

model = Sequential()
model.add(Dense(HIDDEN_DIM, input_dim=784, activation='sigmoid'))
model.add(Dense(10, input_dim=10, activation='softmax'))
model.compile(optimizer='sgd', loss='categorical_crossentropy')
model.summary()

# callback = keras.callbacks.LearningRateScheduler()

history = model.fit(X_train, Y_train, batch_size=10, epochs=EPOCH, validation_data=(X_test, Y_test))
loss = history.history['loss']

epoch_list = [[i] for i in range(0, len(loss))]
import matplotlib.pyplot as plt

plt.scatter(epoch_list, loss)
plt.title('Paramters = {}'.format(20))
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()





