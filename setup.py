#!/usr/bin/env python

from setuptools import setup
import setuptools

with open("README", 'r') as f:
    long_description = f.read()

setup(name='chess_py',
      version='2.7.1',
      description='Python chess client',
      long_description=long_description,
      platforms='MacOS X, Windows, Linux',
      classifiers=[
          'Development Status :: 5 - Stable',
          'Environment :: Console',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 2.7',
      ],
      author='Aubhro Sengupta',
      author_email='aubhrosengupta@gmail.com',
      url='https://github.com/LordDarkula/chess_py',
      license='MIT',
      packages=setuptools.find_packages()
      )
