# -*- coding: utf-8 -*-

# Learn more: https://github.com/fillet54/qroutes

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='qroutes',
    version='0.1.0',
    description='Compojure/Ring like WSGI library',
    long_description=readme,
    author='Phillip Gomez',
    author_email='fillet54@gmail.com',
    url='https://github.com/fillet54/qroutes',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

