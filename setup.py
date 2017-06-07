# Always prefer setuptools over distutils
from codecs import open
from os import path
from setuptools import setup


# To use a consistent encoding
here = path.abspath(path.dirname(__file__))



setup(
    name='gitleak',

    version='0.9.2.3',

    description='A tool library for searching your leaked sourcecode on github',

    long_description='A tool library for searching your leaked sourcecode on github',

    url='https://github.com/lfzark/gitleak',

    author='ark1ee',

    author_email='lfzlfz@126.com',

    # Choose your license
    license='MIT',


    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='github leak source code',
    
    packages=['gitleak'],

 
)
