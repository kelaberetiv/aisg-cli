from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name='aisg-cli',
    version='0.1.2',
    description='AISG CLI Tool',
    long_description='Command line interface to simplify machine learning workflows - data acquisition, modeling, deployment',
    url='https://github.com/kensoh/aisg-cli',
    author='AI Singapore',
    author_email='engineering@aisingapore.org',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
	'Intended Audience :: System Administrators',
	'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    scripts=[
	'aisg',
	'aisg.bat',
	'aisg.py',
    ],
)
