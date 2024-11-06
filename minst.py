from tensorflow.keras.dataset import mnist
from numpy import np
import random

class minst_dataset:

      def __init__(self):
        (x_train, y_train, x_test, y_test) = self.load_minst_data()
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.train_dict = self.consturct_train_dict()

      def load_minst_data(self) -> tuple:
        """ Loads the training and testing data from minst"""
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        return (x_train, y_train, x_test, y_test)

      def consturct_train_dict(self) -> dict:
        """ Returns a dict with digits as index and coresponding training images as values """
        train_dict = {}
        for i in range(10):
            train_dict[i] = self.x_train[self.y_train == i]

        for i in train_dict.keys():
            train_dict[i] = random.choice(train_dict[i])
            threshold = np.mean(train_dict[i])
            train_dict[i] = np.where(train_dict[i] > threshold, 1 ,-1)
        return train_dict
