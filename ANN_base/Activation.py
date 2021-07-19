import numpy as np


class Activation:
  def sigmoid(z: np.ndarray):
    return 1 / (1 + np.exp(-z))

  def sigmoid_derivation(z: np.ndarray):
    a = Activation.sigmoid(z)
    return a * (1 - a)

  def tanh(z: np.ndarray):
    # return 2 * self.sigmoid(2 * z) - 1
    return np.tanh(z)

  def tanh_derivation(z: np.ndarray):
    return 4 * Activation.sigmoid_derivation(2 * z)

  def ReLU(z: np.ndarray):
    return np.maximum(z, 0)

  def ReLU_derivation(z: np.ndarray):
    return 0 if z <= 0 else 1

  def ELU(alpha: int, z: np.ndarray):
    return z if z >= 0 else alpha * (np.exp(z) - 1)

  def ELU_derivation(alpha: int, z: np.ndarray):
    return 1 if z >= 0 else alpha * np.exp(z)

  def Leaky_ReLU(alpha, z: np.ndarray):
    return np.where(z >= 0, z, z * alpha)

  def Leaky_ReLU_derivation(alpha, z: np.ndarray):
    return alpha if z <= 0 else 1