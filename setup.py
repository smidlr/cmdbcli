#!/usr/bin/env python

PROJECT = 'cmdbcli'
VERSION = '0.1.0'

from setuptools import setup, find_packages

setup(
    name=PROJECT,
    version=VERSION,

    description='CLI for CMDB',
    long_description='CLI tool for interacting with GDC CMDB application.',

    author='Radek Smidl',
    author_email='radek.smidl@gooddata.com',

    url='https://github.com/smidlr/cmdbcli',
    download_url='https://github.com/smidlr/cmdbcli/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Environment :: Console',
                 'Intended Audience :: System Administrators',
                 'License :: OSI Approved :: BSD License',
                 'Natural Language :: English',
                 'Operating System :: POSIX',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff', 'requests'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'cmdb = cmdbcli.__main__:main'
        ],
        'cmdbcli': [
            'simple = cmdbcli.simple:Simple',
            'list files = cmdbcli.list:Files',
            'files = cmdbcli.list:Files',
            'file = cmdbcli.show:File',
            'show file = cmdbcli.show:File',
            'unicode = cmdbcli.encoding:Encoding',
        ],
    },

    zip_safe=False,
)
