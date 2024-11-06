import numpy as np
from hopefield import HopfieldNetwork
from minst import minst_dataset
from distortion import Distortion
import random

class Hopfield_interface:
    def __init__(self):
        self.hopfield_network = HopfieldNetwork()
        self.minst_dataset = minst_dataset()
        self.pattern_index = []

    def train_network(self, first_digit=0, second_digit=2):
        """ trains the network on the given patterns """
        patterns = [self.minst_dataset.train_dict[first_digit],  self.minst_dataset.train_dict[second_digit]]
        self.pattern_index = [first_digit, second_digit]
        self.hopfield_network.train_pattern(patterns)

    def generate_test_pattern(self, number=0, distortion="salt_and_paper"):
      """ retrives a patter to test the hopefiled network on returns a 28*28 pattern"""
      if number not in range(10):
          Exception("Number must be between 0 and 9")
      pattern = self.minst_dataset.pick_pattern(number)
      threshold = np.mean(pattern)
      pattern = np.where(pattern > threshold, 1 ,-1)
      pattern = self.distort_pattern(pattern, distortion)
      return pattern

    def pattern_match(self, pattern):
      return self.hopfield_network.recall(pattern)

    def distort_pattern(self, pattern, distortion="invert_pixels"):
      """ applies salt_and_pepper noise to the pattern returns 28 * 28 array """
      distortions = {
        "gaussian_noise": Distortion.add_gaussian_noise,
        "invert_pixels": Distortion.invert_random_pixels,
        "salt_and_pepper": Distortion.add_salt_and_pepper_noise
      }

      if distortion in distortions:
          pattern = distortions[distortion](pattern)
      else:
         Exception('Invalid distortion provided')
      return pattern

    def pick_pattern(self):
        """ returns a random pattern from the minst training set"""
        number = random.choice(self.pattern_index)
        return random.choice(self.minst_dataset.x_test[self.minst_dataset.y_test == number])