import pytest
from gaussianfit import gaussianfit_code
import numpy as np


def gaussian_fct(x, amp, x0, sigma):
    return amp * np.exp(-((x - x0) ** 2) / (2 * sigma**2))


def test_gaussian_fit():
    x = np.linspace(0, 10, 10)
    center = 0
    sigma = 2
    amp = 1
    y = gaussian_fct(x, amp, center, sigma)

    params = gaussianfit_code.gaussianfit_fct(x, y)

    epsilon = 1e-8
    assert np.abs(params[0] - amp) < epsilon
    assert np.abs(params[1] - center) < 2 * epsilon
    assert np.abs(params[2] - sigma) < epsilon


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
        
def test_raises_size():
    x = []
    y = []
    with pytest.raises(Exception, match=r"input data of size 0"):
        gaussianfit_code.gaussianfit_fct(x, y)


def test_raises_size_2():
    x = [1]
    y = []
    with pytest.raises(Exception, match=r"input data of different size"):
        gaussianfit_code.gaussianfit_fct(x, y)



