#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension

# gcc shmmodule.c -I/usr/include/python2.2  -lpython2.2 -lc

setup(name="Distutils",
	version="1.0",
	description="Python's Shared Memory Module",
	author="Vladimir Marangozov",
	author_email="Vladimir.Marangozov@inrialpes.fr",
	url="http://gigue.peabody.jhu.edu/~mdboom/omi/source/shm_source/shm.html",
	ext_modules=[Extension("shm", ["shmmodule.c"])]
	)

 