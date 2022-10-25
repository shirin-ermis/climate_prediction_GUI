#
# climpred setuptools script
#
from setuptools import setup, find_packages


def get_version():
    """
    Get version number from the pkmodel module.

    The easiest way would be to just ``import pkmodel ``, but note that this
    may fail if the dependencies have not been installed yet. Instead, we've
    put the version number in a simple version_info module, that we'll import
    here by temporarily adding the oxrse directory to the pythonpath
    using sys.path.
    """
    import os
    import sys

    sys.path.append(os.path.abspath('climpred'))
    from climpred.version_info import VERSION as version
    sys.path.pop()

    return version


def get_readme():
    """
    Load README.md text for use as description.
    """
    with open('README.md') as f:
        return f.read()


# Go!
setup(
    # Module name (lowercase)
    name='climpred',

    # Version
    version='0.0.1',

    description='A python library for calculating temperatures in a 2-layer \
        atmospheric model.',

    long_description=get_readme(),

    license='MIT license',

    # author='',

    # author_email='',

    maintainer='Shirin Ermis',

    maintainer_email='shirin.ermis@env-res.ox.ac.uk',

    url='https://sabs-r3.github.io/software-engineering-project2/\
        01-introduction/index.html',

    # Packages to include
    packages=find_packages(include=('climpred', 'climpred.*')),

    # List of dependencies
    install_requires=[
        # Dependencies go here!
        'numpy',
        'matplotlib',
        'scipy',
        'tkinter',
    ],
    extras_require={
        'docs': [
            # Sphinx for doc generation. Version 1.7.3 has a bug:
            'sphinx>=1.5, !=1.7.3',
            # Nice theme for docs
            'sphinx_rtd_theme',
        ],
        'dev': [
            # Flake8 for code style checking
            'flake8>=3',
        ],
    },
)
