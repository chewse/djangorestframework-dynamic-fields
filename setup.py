# -*- coding: utf-8 -*-

import os
import re
import setuptools

dirname = os.path.dirname(__file__)

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Determine version number automatically
version = ''
with open(os.path.join(dirname, 'dynamicfields.py')) as module_file:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        module_file.read(),
        re.MULTILINE
    ).group(1)

# Read in description info from files
with open(os.path.join(dirname, 'README.rst')) as readme_file:
    readme = readme_file.read()
with open(os.path.join(dirname, 'HISTORY.rst')) as history_file:
    history = history_file.read()

# Organize requirements
install_requires = [
    'django>=1.4',
    'djangorestframework',
]
tests_requires = [
    'pytest',
    'mock',
    'virtualenv',
]

# Main setup command
setuptools.setup(
    name='djangorestframework-dynamic-fields',
    version=version,
    description='Mixin to restrict the fields returned by your API',
    long_description=readme + '\n\n' + history,
    author='Chewse',
    author_email='dev@chewse.com',
    url='https://github.com/chewse/djangorestframework-dynamic-fields',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_requires,
    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
