# Gaussian fit 

## Main features and I/O:

gaussianfit is a Python package that fits inputs data and returns the parameters of a gaussian curve which minimizes the error with respect to input data

Input arguments: two lists X and Y.
Output parameters correspond to : center, amplitude and sigma.

## Dependencies

Required python packages:
* [numpy](https://www.numpy.org/) >=1.16.0
* [scipy](https://www.scipy.org/) >=1.11.0
* [pytest]


### Build and install
Make sure to create a python virtual environement prior to installation. Then in base_gaussianfit directory run:

``python setup.py sdist bdist_wheel``

``pip install .``

### Tests using pytest:
In base_gaussianfit directory open cmd line and run:

``pytest tests``


### Import package:

``from gaussianfit import gaussianfit_code``

Then call the function as follows with your x, y data:

``gaussianfit_code.gaussianfit_fct(x,y)``
 
