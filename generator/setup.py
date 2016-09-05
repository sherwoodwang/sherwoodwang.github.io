#!/usr/bin/env python3

from setuptools import setup

setup(
    name='sherwoodwang.github.io-generator',
    version='0.1',
    packages=['sherwoodwang_github_io'],
    package_data={
        'sherwoodwang_github_io': ['**/*.pt']
    },
    include_package_data=True,
    url='',
    license='',
    author='Sherwood Wang',
    author_email='sherwood@wang.onl',
    description='Generator for sherwoodwang.github.io',
    entry_points={
        'console_scripts': [
            'generate = sherwoodwang_github_io.build:main'
        ]
    },
)
