import numpy as np

class Distortion:

    @classmethod
    def add_salt_and_pepper_noise(cls, pattern, amount=0.1):
      """
      Adds salt-and-pepper noise to an pattern.
      - pattern: 2D array (binary pattern).
      - amount: Proportion of pixels to be flipped.
      """
      noisy_pattern = pattern.copy()
      # Generate random indices for salt and pepper
      num_salt = int(amount * pattern.size / 2)
      salt_indices = tuple(np.random.randint(0, i, num_salt) for i in pattern.shape)
      num_pepper = int(amount * pattern.size / 2)
      pepper_indices = tuple(np.random.randint(0, i, num_pepper) for i in pattern.shape)
      
      # Apply salt and pepper noise
      noisy_pattern[salt_indices] = 1
      noisy_pattern[pepper_indices] = -1
      return noisy_pattern

    @classmethod
    def add_gaussian_noise(cls, pattern, mean=-0.01, std=0.1):
      """
      Adds Gaussian noise to an pattern.
      - pattern: 2D array (binary pattern).
      - mean: Mean of the Gaussian distribution.
      - std: Standard deviation of the Gaussian distribution.
      """
      noisy_pattern = pattern.copy()
      gaussian_noise = np.random.normal(mean, std, pattern.shape)
      noisy_pattern = noisy_pattern + gaussian_noise
      
      # Binarize again (optional)
      noisy_pattern = np.where(noisy_pattern > 0, 1, -1)
      return noisy_pattern

    @classmethod
    def invert_random_pixels(cls, pattern, amount=0.1):
      """
      Randomly inverts pixels in a binary pattern.
      - pattern: 2D array (binary pattern).
      - amount: Proportion of pixels to invert.
      """
      noisy_pattern = pattern.copy()
      num_pixels_to_invert = int(amount * pattern.size)
      indices = tuple(np.random.randint(0, i, num_pixels_to_invert) for i in pattern.shape)
      
      # Invert selected pixels
      noisy_pattern[indices] = -noisy_pattern[indices]
      return noisy_pattern