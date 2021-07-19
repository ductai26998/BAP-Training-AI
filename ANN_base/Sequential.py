import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
from Activation import *


class Sequential:
    def __init__(self):
        # Layer numbers
        self.L = 0

        # Input shape
        self.input_shape = 0

        # Activations
        self.activations = []

        # architecture of model: layer name, output shape, params
        self.model = [[], [], []]

        # feedforward
        self.a = []
        self.z = []
        self.W = []
        self.b = []

        # Backpropagation
        self.da = []
        self.dz = []
        self.dW = []
        self.db = []

    def _init_layer(self, shape1: int, shape2: int) -> tuple:
        """
        Initial new layer

        Parameters:
            shape1: int: The node numbers of this layer
            shape2: int: The node numbers of latest layer
        """
        np.random.seed(1)

        # Feedforward
        a_n = 0.1 * np.random.randn(1, shape1)
        z_n = 0.1 * np.random.randn(1, shape1)
        W_n = 0.1 * np.random.randn(shape1, shape2)
        b_n = 0.1 * np.random.randn(1, shape1)

        # Backpropagation
        da_n = 0.1 * np.random.randn(1, shape1)
        dz_n = 0.1 * np.random.randn(1, shape1)
        dW_n = 0.1 * np.random.randn(shape1, shape2)
        db_n = 0.1 * np.random.randn(1, shape1)

        return a_n, z_n, W_n, b_n, da_n, dz_n, dW_n, db_n

    def add_layer(self, shape1: int, shape2: int):
        """
        Add all element layer in model
        """
        a_n, z_n, W_n, b_n, da_n, dz_n, dW_n, db_n = self._init_layer(shape1, shape2)
        self.a.append(a_n)
        self.z.append(z_n)
        self.W.append(W_n)
        self.b.append(b_n)

        self.da.append(da_n)
        self.dz.append(dz_n)
        self.dW.append(dW_n)
        self.db.append(db_n)

    def activstion_func(self, activation: str) -> object:
        """
        Get activation of layer

        Parameters:
            activation: str: The name of activation function
        """
        try:
            switcher = {
                'sigmoid': Activation.sigmoid,
                'tanh': Activation.tanh,
                'ReLU': Activation.ReLU,
                'ELU': Activation.ELU,
                'Leaky_ReLU': Activation.Leaky_ReLU
            }
            func = switcher.get(activation)
            if func == None:
                raise
            return func
        except:
            print("Can not use this activation!")

    def derivation_func(self, activation: str) -> object:
        """
        Get the derivation of activation layer

        Parameters:
            activation: str: The name of activation function
        """
        try:
            switcher = {
                'sigmoid': Activation.sigmoid_derivation,
                'tanh': Activation.tanh_derivation,
                'ReLU': Activation.ReLU_derivation,
                'ELU': Activation.ELU_derivation,
                'Leaky_ReLU': Activation.Leaky_ReLU_derivation
            }
            func = switcher.get(activation)
            if func == None:
                raise
            return func
        except:
            print("Can not use this activation!")

    def add(self, layer_name: str, n_unit: int, activation: str = None):
        """
        Add new layer in model

        Parameters:
            layer_name: str: The name of new layer
            n_unit: int: The node numbers of new layer
            activation: str: The activation name of new layer
        """
        # add layer name in architecture
        self.model[0].append(layer_name)

        if layer_name == 'input':
            self.input_shape = n_unit
            self.add_layer(self.input_shape, 0)

            # add layer shape in architecture
            self.model[1].append((self.input_shape, len(self.a[self.L - 1])))
            # add layer weight params in architecture
            self.model[2].append(0)
        else:
            n_unit_latest = self.a[self.L - 1].shape[1]
            self.add_layer(n_unit, n_unit_latest)
            self.activations.append(activation)

            # add layer shape in architecture
            self.model[1].append((len(self.W[self.L]), len(self.a[self.L - 1])))
            # add layer weight params in architecture
            self.model[2].append(n_unit * (self.model[1][self.L - 1][0] + 1))

        self.L = self.L + 1

    def feedforward(self, X: np.ndarray):
        """
        Compute the values of model with feedforward

        Parameters:
            X: np.ndarray: The input of model
        """
        self.a[0] = X
        for l in range(1, self.L):
            self.z[l] = self.a[l-1] @ self.W[l].T + self.b[l]
            activation = self.activations[l - 1]
            self.a[l] = self.activstion_func(activation)(self.z[l])

    def cost_function(self, y: np.ndarray, h: np.ndarray) -> float:
        """
        Compute the cost function of model

        Parameters:
            y: np.ndarray: The real output
            h: np.ndarray: The hypothesis output
        """
        m = y.shape[0]
        cost = np.sum(-y * np.log(h) - (1 - y) * np.log(1 - h))
        return (1 / m) * cost

    def backpropagation(self, y: np.ndarray, h: np.ndarray):
        """
        Compute the values of model with backpropagation

        Parameters:

        """
        m = y.shape[0]
        self.da[self.L - 1] = -np.divide(y, h) + np.divide(1 - y, 1 - h)
        for l in reversed(range(1, self.L)):
            activation = self.activations[l - 1]
            self.dz[l] = self.da[l] * self.derivation_func(activation)(self.z[l])
            self.dW[l] = (1 / m) * (self.dz[l].T @ self.a[l - 1])
            self.db[l] = (1 / m) * np.sum(self.dz[l], axis=0)
            self.da[l - 1] = self.dz[l] @ self.W[l]

    def update_model(self, alpha: float):
        """
        Update weights and biases of model

        Parameters:
            alpha: float: learning rate
        """
        for l in range(1, self.L):
            self.W[l] = self.W[l] - alpha * self.dW[l]
            self.b[l] = self.b[l] - alpha * self.db[l]

    def summary(self):
        """
        Show the table summary model
        """
        print("\n SUMMARY:")
        string = "{0:<20}{1:<20}{2:<20}".format("Layer", "Output shape", "Param")
        print(string)
        for i in range(self.L):
            layer_info = "{0:<20}{1:<20}{2:<20}".format(str(self.model[0][i]), str(self.model[1][i]), self.model[2][i])
            print(layer_info)
        print("Total params: " + str(sum(self.model[2])))

    def fit(self, X_train, y_train, epochs, learning_rate):
        """
        Train model
        """
        cost_history = []
        for i in range(epochs):
            self.feedforward(X_train)
            cost_func = self.cost_function(y_train, self.a[self.L - 1])
            cost_history.append(cost_func)
            self.backpropagation(y_train, self.a[self.L - 1])
            self.update_model(learning_rate)
            print("Training time: ", i + 1, " with loss: ", cost_func)

        self.loss = cost_history

    def predict(self, x_test: np.ndarray):
        """
        Compute output with input = x_test

        Parameters:
            x_test: np.ndarray: The input need to predict
        """

        self.feedforward(x_test)
        return np.where(self.a[self.L - 1] >= 0.5, 1, 0)

    def get_loss(self):
        """
        get loss value after training

        """
        return self.loss

    def plotloss(self):
        """
        Visualize the loss line
        """
        fig = plt.figure(1)
        plt.plot(self.loss)
        plt.xlabel('train times')
        plt.ylabel('Loss')
        fig.show()
        fig.savefig("loss.png")

    def accuracy(self, x_val: np.ndarray, y_val: np.ndarray):
        """
        Get accuracy of model

        Parameters:
            x_val: np.ndarray: The input of validation data
            y_val: np.ndarray: The real output of validation data
        """
        prediction = self.predict(x_val)
        return np.mean(prediction == y_val) * 100
