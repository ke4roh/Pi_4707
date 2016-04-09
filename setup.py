# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rasPiNWR',
    version='0.1.0',
    description='Operate the Raspberry Pi NOAA Weather Radio Receiver and Decoder',
    long_description='This library provides basic operations and demonstration of features for the board',
    author='AIW Industries',
    author_email='aiwindustries@gmail.com',
    url='https://github.com/AIWIndustries/Pi_4707',
    license='GNU GPL',
    packages=find_packages(exclude=('tests', 'docs'))
)
