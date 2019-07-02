#!/usr/bin/env python3
  
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
     long_description=fh.read()

setup(name='alcpack',
     version='1.1.1',
     description='Adaptive Local Complementation Package',
     long_description=long_description,
     long_description_content_type="text/markdown",
     classifiers=[
         "Programming Language :: Python :: 3.5",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ],
     keywords='network simple connected graph local complementation creation of an edge',
     author='Amit Kumar Pal',
     author_email='amitsweb@gmail.com',
     license='Apache 2',
     packages=find_packages(),
     download_url='https://github.com/amitkpal/alcpack/archive/master.zip',
     install_requires=[
         'networkx',
     ],
     include_package_data=True)
