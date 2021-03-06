# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    # Application name:
    name="corpussearch",

    # Version number (initial):
    version="0.0.16",

    # Application author details:
    author="Malte Vogl",
    author_email="mvogl@mpiwg-berlin.mpg.de",

    # Packages
    packages=find_packages(exclude=('tests', 'example')),

    # Include additional files into the package
    include_package_data=True,

    url='https://github.com/computational-antiquity/corpussearch/',

    # Details

    license='GPLv3',
    description="Tools for loading and analyzing large text corpora.",

    long_description=long_description,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],

    project_urls={
        'Home': 'https://github.com/computational-antiquity/corpussearch/',
        'Tracker': 'https://github.com/computational-antiquity/corpussearch/issues',
        'Download': 'https://github.com/computational-antiquity/corpussearch/archive/0.0.16.tar.gz',
    },

    python_requires='>=3',

    # Dependent packages (distributions)
    install_requires=[
        "pandas",
        "numpy",
        "xlrd",
        "citableclass",
        "ipywidgets",
        "Ipython",
        "gensim",
        "cltk",
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
