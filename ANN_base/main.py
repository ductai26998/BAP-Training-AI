from Sequential import Sequential
from data import *

# Model

X, y = initial_data()
y = remap(y, 3)
model = Sequential()
model.add(layer_name='input', n_unit=2, activation=None)
model.add(layer_name='dense', n_unit=8, activation='sigmoid')
model.add(layer_name='dense', n_unit=7, activation='tanh')
model.add(layer_name='output', n_unit=3, activation='sigmoid')

# Summary model
model.summary()
# Training model
model.fit(X, y, epochs=2050, learning_rate=1.2)
model.plotloss()

# Validate
X_val, y_val = initial_data(200, 2, 3, 'validation_data.png')
y_val = remap(y_val, 3)
x_test = [[-0.692, -0.166], [0.718, 0.248]]
x_test_1 = [0.718, 0.248]
x_test_2 = [0.155, -0.623]
pre = model.predict(X_val)
print(pre)
print(model.accuracy(X_val, y_val))
