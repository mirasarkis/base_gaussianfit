from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'GaussianFit package'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="gaussianfit", 
        version=VERSION,
        author="Mira Sarkis",
        author_email="gne.mirasarkis@gmail.com",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        
        keywords=['python', 'GaussianFit '],
        classifiers= [
            "Development Status :: 1 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3"
        ]
)
