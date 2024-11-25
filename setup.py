#!/usr/bin/env python
import ast
import os
import subprocess

from setuptools import setup, find_packages

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    f.close()

with open('src/__init__.py') as f:
    version_ = f.read()
    exec(version_)
    f.close()

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


from pathlib import Path
os.chdir(Path(__file__).parent.absolute())

setup(
    name='peak-over-threshold',
    version=__version__,
    author='Chuanbo Hua',
    author_email='cbhua@kaist.ac.kr',
    description='Algorithms about Peaks-over-Threshold, including POT, Stream POT, and DSPOT.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sedgewickmm18/peak-over-threshold',
    packages=['peak_over_threshold','peak_over_threshold.utils'],
    package_dir={'peak_over_threshold':'src',
                 'peak_over_threshold.utils':'src/utils'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=requirements
)
