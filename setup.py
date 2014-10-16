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
      package_dir={ 'Mud': 'Mud' },
      packages=[
          'Mud',
          'Mud.Adventure',
          'Mud.Parser',
          'Mud.Room'
      ],
      scripts=[
         'bin/mud'
      ]
)
