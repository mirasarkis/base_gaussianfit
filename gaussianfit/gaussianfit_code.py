import numpy as np
from scipy.optimize import curve_fit

def gaussianfit_fct(x_data, y_data):
    if len(x_data) != len(y_data):
        raise Exception("input data of different size")
    if not len(x_data) or not len(y_data):
        raise Exception("input data of size 0")
    Gauss_lbd = lambda x, amp, x0, sigma: amp * np.exp(
        -1 * (x - x0) ** 2 / (2 * sigma**2))
    params, cov = curve_fit(Gauss_lbd, x_data, y_data)
    return dict(enumerate(params))
