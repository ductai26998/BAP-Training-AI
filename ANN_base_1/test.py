import pandas as pd
import numpy as np
from Sequential import *

def remap(y, K):
    m = len(y)
    out = np.zeros((m, K))
    for index in range(m):
        out[index][y[index]] = 1
    return out

df = pd.read_csv("./data/archive/mnist_train.csv")

data_train = df.values
y_train = data_train[:2000, 0]
y_train_mapped = remap(y_train, 10)
x_train = data_train[:2000, 1:]

# Model
model = Sequential()
model.add(layer_name='input', n_unit=784, activation=None)
model.add(layer_name='dense', n_unit=200, activation='sigmoid')
model.add(layer_name='dense', n_unit=100, activation='sigmoid')
model.add(layer_name='output', n_unit=10, activation='sigmoid')

# Summary model
model.summary()
# Training model
model.fit(x_train, y_train_mapped, epochs=200, learning_rate=5)
model.plotloss()

# Validate
df = pd.read_csv("./data/archive/mnist_test.csv")

data_test = df.values
y_test = data_test[:100, 0]
y_test_mapped = remap(y_test, 10)
x_test = data_test[:100, 1:] / 255

pre = model.predict(x_test[1:10])
print(pre)
print(model.accuracy(x_test, y_test_mapped))

