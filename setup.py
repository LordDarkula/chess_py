#!/usr/bin/env python

from setuptools import setup
import setuptools

setup(name='chess_py',
      version='2.1',
      description='Python chess client',
      platforms='MacOS X',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 2.7',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
      ],
      author='Aubhro Sengupta',
      author_email='aubhrosengupta@gmail.com',
      url='https://github.com/LordDarkula/chess_py',
      license='MIT',
      packages=setuptools.find_packages(),
      )
