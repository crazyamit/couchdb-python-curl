#!/usr/bin/env python

from distutils.core import setup
setup(name='couchdb-python-curl',
      version='1.0',
      description='CouchDB-python wrapper (using cURL library)',
      author='Alexey Loshkarev',
      author_email='elf2001@gmail.com',
      url='http://code.google.com/p/couchdb-python-curl/',
      packages=['couchdbcurl'],
      requires=['pycurl'],
      license='GPL',
      )
