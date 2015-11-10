import os
import sys
import imp
import multiprocessing
from setuptools import setup, find_packages


version = imp.load_source('version', os.path.join('addon_demo', 'version.py'))

def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)

def read(fname):
    return open(fpath(fname)).read()

def desc():
    return read('README.rst')

setup(
    name='Flask-AppBuilder-AddOn-Demo',
    version=version.VERSION_STRING,
    url='https://github.com/dpgaspar/flask-appbuilder/',
    license='BSD',
    author='Daniel Vaz Gaspar',
    author_email='danielvazgaspar@gmail.com',
    description='Simple and rapid application development framework, built on top of Flask. includes detailed security, auto CRUD generation for your models, google charts and much more.',
    long_description=desc(),
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    entry_points={'console_scripts': [
          'fabmanager = flask_appbuilder.console:cli',
      ]},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask-AppBuilder>=1.5.0',
    ],
    tests_require=[
        'nose>=1.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='nose.collector'
)
