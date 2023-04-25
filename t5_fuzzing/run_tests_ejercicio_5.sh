#!/bin/bash

# We set the following environment variable to zero to disable Python's hash randomization
# More info: https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED
export PYTHONHASHSEED=0

# We run the test cases in file test_ejercicio_5.py in module "test" using the Python interpreter in virtual environment "venv"
venv/bin/python -m unittest test.test_ejercicio_5
