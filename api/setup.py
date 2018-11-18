#!/usr/bin/env python3
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as h:
    requires = [l for l in h.read().splitlines() if l.strip()]

setup(name='bitrated',
      version='0.0.1',
      description='simple application with rates from bitfinex exchange',
      author='Kirill Goldshtein',
      author_email='goldshtein.kirill@gmail.com',
      packages=['bitrate', 'bitrate/handlers', 'bitrate/handlers/v1'],
      install_requires=[requires],
      test_suite='tests',
      scripts=['bin/bitrated.py'],
      license='MIT',
      url='https://github.com/go1dshtein/bitrated',
      classifiers=['Intended Audience :: Developers',
                   'Environment :: Console',
                   'Programming Language :: Python :: 3.7',
                   'Natural Language :: English',
                   'Development Status :: 1 - Planning',
                   'Operating System :: Unix',
                   'Topic :: Utilities'])
