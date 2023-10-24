"""
    Setup file for tic_tac_toe.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.5.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
from setuptools import setup, find_packages

setup(
    name='tic_tac_toe',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['pyfiglet','sphinx-rtd-theme'],  # Add 'pyfiglet' here
    entry_points={},
    url='',
    license='MIT',
    author='Erin Akinjide',
    author_email='erinakinjide16@gmail.com',
    description='A simple Tic Tac Toe game package',
    html_theme='sphinx_rtd_theme'
)

