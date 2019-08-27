from setuptools import setup, find_packages


setup(
    name='pycalc',
    description='pure command-line calculator',
    version='',
    author='Alexey Danilchyck',
    author_email='danilchyck@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['pycalc = calculator.pycalc:main']
    }
)
