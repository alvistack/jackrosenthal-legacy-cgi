# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='legacy-cgi',
    version='2.6.3',
    description='Fork of the standard library cgi and cgitb modules removed in Python 3.13',
    author_email='Guido van Rossum <guido@python.org>, Andreas Paepcke <paepcke@haddock.stanford.edu>, Steve Majewski <sdm7g@virginia.edu>, Michael McLay <mclay@eeel.nist.gov>',
    maintainer_email='Jack Rosenthal <jack@rosenth.al>',
    py_modules=['cgi', 'cgitb'],
)
