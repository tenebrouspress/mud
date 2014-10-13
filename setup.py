#!/usr/bin/env python
import os
import sys

from distutils.core import setup

setup(name='mud',
      version='0.0.1',
      description='MUD',
      maintainer='Andrew Butcher',
      maintainer_email='abutcher@redhat.com',
      license='GPLv3+',
      package_dir={ 'mud': 'mud' },
      packages=[
          'mud',
          'mud.adventure',
          'mud.parser',
          'mud.room'
      ],
      scripts=[
         'bin/mud'
      ]
)
