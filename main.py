from hopefield import HopfieldNetwork
from tensorflow.keras.dataset import minst
from interface import Hopfield_interface
import matplotlib.pyplot as plt

interface = Hopfield_interface()

interface.train_network() # defaults to 0 and 2 but can accept any two digits

pattern = interface.pick_pattern() # picks a pattern from the digits network was trained on
plt.imshow(pattern, cmap='gray')

distorted_pattern = interface.distort_pattern(pattern) # distorts pciked pattern can take string arugment to use different distortions
plt.imshow(distorted_pattern, cmap='gray')

retrived_pattern = interface.pattern_match(distorted_pattern) # the stable pattern from the network
plt.imshow(retrived_pattern, cmap='gray')