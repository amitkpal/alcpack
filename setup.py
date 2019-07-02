#!/usr/bin/env python
  
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
     long_description=fh.read()

setup(name='alcpack',
     version='1.01',
     description='Adaptive Local Complementation Packages',
     long_description=long_description,
     long_description_content_type="text/markdown",
     classifiers=[
         "Programming Language :: Python :: 3.5",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ],
     keywords='nnetwork connected graph local complementation creationn of a link',
     author='David Amaro, Markus Mueller, Amit Kumar Pal',
     author_email='amitswe@gmail.com',
     license='Apache 2',
     packages=find_packages(),
     download_url='https://github.com/amitkpal/alcpack/archive/master.zip',
     install_requires=[
         'networkx',
     ],
     include_package_data=True)
