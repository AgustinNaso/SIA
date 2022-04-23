from scipy import optimize
from Calculator import get_error
import numpy as np

x0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(optimize.fmin_cg(get_error, x0))
