import os
from setuptools import setup, find_packages

with open('README.md') as f:
    readme_data = f.read()

with open('LICENSE') as f:
    license_data = f.read()

setup(
    name='py_tenma_app',
    version='0.0.1',
    description='python 🐍 flask application for tenma power supply',
    long_description=readme_data,
    author='Chaitanya Reddy',
    author_email='chaitu.ycr@gmail.com',
    url='https://github.com/chaitu-ycr/py_tenma_app',
    license=license_data,
    packages=find_packages(exclude=['docs', 'scripts', 'site', 'tests'])
)
