import numpy as np


class Activation:

  def sigmoid(z: np.ndarray):
    # z = np.array(z, dtype=np.float128)
    return 1 / (1 + np.exp(-z))

  def sigmoid_derivation(z: np.ndarray):
    # z = np.array(z, dtype=np.float128)
    a = Activation.sigmoid(z)
    return a * (1 - a)

  def tanh(z: np.ndarray):
    return np.tanh(z)

  def tanh_derivation(z: np.ndarray):
    return 4 * Activation.sigmoid_derivation(2 * z)

  def ReLU(z: np.ndarray):
    return np.maximum(z, 0.0)

  def ReLU_derivation(z: np.ndarray):
    return np.where(z <= 0, 0, 1)

  def ELU(z: np.ndarray, alpha: float = 0.1):
    return np.where(z >= 0, z, alpha * (np.exp(z) - 1))

  def ELU_derivation(z: np.ndarray, alpha: float = 0.1):
    return np.where(z >= 0, 1, alpha * np.exp(z))

  def Leaky_ReLU(z: np.ndarray, alpha: float = 0.1):
    return np.where(z >= 0, z, z * alpha)

  def Leaky_ReLU_derivation(z: np.ndarray, alpha: float = 0.1):
    return np.where(z <= 0, alpha, 1)
