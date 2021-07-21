import numpy as np


class Activation:
  @staticmethod
  def sigmoid(z: np.ndarray):
    return 1 / (1 + np.exp(-z))

  @staticmethod
  def sigmoid_derivation(z: np.ndarray):
    a = Activation.sigmoid(z)
    return a * (1 - a)

  @staticmethod
  def tanh(z: np.ndarray):
    return np.tanh(z)

  @staticmethod
  def tanh_derivation(z: np.ndarray):
    return 4 * Activation.sigmoid_derivation(2 * z)

  @staticmethod
  def ReLU(z: np.ndarray):
    return np.maximum(z, 0)

  @staticmethod
  def ReLU_derivation(z: np.ndarray):
    return np.where(z <= 0, 0, 1)

  @staticmethod
  def ELU(z: np.ndarray, alpha: float = 0.1):
    return np.where(z >= 0, z, alpha * (np.exp(z) - 1))

  @staticmethod
  def ELU_derivation(z: np.ndarray, alpha: float = 0.1):
    return np.where(z >= 0, 1, alpha * np.exp(z))

  @staticmethod
  def Leaky_ReLU(z: np.ndarray, alpha: float = 0.1):
    return np.where(z >= 0, z, z * alpha)

  @staticmethod
  def Leaky_ReLU_derivation(z: np.ndarray, alpha: float = 0.1):
    return np.where(z <= 0, alpha, 1)