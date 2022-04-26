from scipy import optimize
import time
from Calculator import get_error
import numpy as np


start_time = time.time()
x0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
results = optimize.minimize(get_error, x0, args=(), method='L-BFGS-B',
                    options={'disp': None, 'maxcor': 10, 'ftol': 2.220446049250313e-09, 'gtol': 1e-05, 'eps': 1e-08,
                             'maxfun': 15000, 'maxiter': 15000, 'iprint': - 1, 'maxls': 20,
                             'finite_diff_rel_step': None})


print("Gradiente descendiente")
print("W = ", results.x[0:3])
print("w = " + str(results.x[3:6]) + "\n\t" + str(results.x[6:9]))
print("w0 = ", results.x[9:11])
print("Error = ", results.fun)
print("Time = ", time.time() - start_time)