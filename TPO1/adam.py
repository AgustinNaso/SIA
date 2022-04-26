from tensorflow import keras
from keras import layers
from keras import Sequential
import tensorflow as tf
from Calculator import g, xi, zeta
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score


import time
start_time = time.time()
x = xi
X = tf.convert_to_tensor(x[0:1].astype("float32"))
y = zeta
y = tf.convert_to_tensor(y[0:1].astype("float32"))

model = Sequential()
model.add(layers.Dense(3, input_dim=3, activation='sigmoid')) #hidden layer  | inputdim es la primer cada
model.add(layers.Dense(1, activation='sigmoid')) # output layer
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) # hay distintos tipos de metricas

history = model.fit(X, y, epochs=1)

y_pred = model.predict(tf.convert_to_tensor(x[2:].astype("float32")))
# Converting predictions to label
pred = list()
for i in range(len(y_pred)):
    pred.append(np.argmax(y_pred[i]))
# Converting one hot encoded test label to label
test = list()
for i in range(len(y)):
    test.append(np.argmax(y[i]))

a = accuracy_score(pred, test)
print('Accuracy is:', a * 100)
print("Time = ", time.time() - start_time)

# La idea es que el validatio data sea otro data set
# history = model.fit(X, y, validation_data=(X, y), epochs=100, batch_size=64)
#
# plt.plot(history.history['accuracy'])
# plt.plot(history.history['val_accuracy'])
# plt.title('Model accuracy')
# plt.ylabel('Accuracy')
# plt.xlabel('Epoch')
# plt.legend(['Train', 'Test'], loc='upper left')
# plt.show()
#
# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.title('Model loss')
# plt.ylabel('Loss')
# plt.xlabel('Epoch')
# plt.legend(['Train', 'Test'], loc='upper left')
# plt.show()