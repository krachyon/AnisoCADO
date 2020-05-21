# -*- coding: utf-8 -*-
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    __readme__ = f.read()

with open('LICENSE') as f:
    __license__ = f.read()

__version__ = "0.1.rc1"

setup(
    name='anisocado',
    version=__version__,
    description='Generate off-axis SCAO PSFs for the ELT',
    long_description=__readme__,
    author='Eric Gendron, Kieran Leschinski',
    author_email='kieran.leschinski@univie.ac.at',
    url='https://github.com/astronomyk/anisocado',
    license=__license__,
    include_package_data=True,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['numpy', 'astropy', 'matplotlib']
    )
