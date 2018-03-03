#!/usr/bin/env python

from setuptools import setup
import setuptools

setup(name='chess_py',
      version='2.7.1',
      description='Python chess client',
      platforms='MacOS X, Windows',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 2.7',
      ],
      author='Aubhro Sengupta',
      author_email='aubhrosengupta@gmail.com',
      url='https://github.com/LordDarkula/chess_py',
      license='MIT',
      packages=setuptools.find_packages(),
      )
