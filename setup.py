from setuptools import find_packages, setup

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Nithin',
    author_email='cherukumallinithin2003@gmail.com',
    install_requires=[
        "scikit-learn",
        "pandas",
        "numpy"
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
