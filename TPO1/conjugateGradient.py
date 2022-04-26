from scipy import optimize
from Calculator import get_error
import numpy as np

import time
start_time = time.time()

x0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print("Gradiente conjugado")
print(optimize.fmin_cg(get_error, x0))
print("Time = ", time.time() - start_time)