"""Setup."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Ghost Blog Data Sanitizer',
    version='1.0.0',
    description='Sanitize Ghost Blog SQL data to ensure content quality.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hackersandslackers/ghost-sql-sanitation',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Ghost Blog SQL Python Automation',
    packages=find_packages(),
    install_requires=['Flask',
                      'PyMySQL',
                      'SQLAlchemy',
                      'Loguru'],
    entry_points={
        'console_scripts': [
            'run = main:__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hackersandslackers/ghost-sql-sanitation/issues',
        'Source': 'https://github.com/hackersandslackers/ghost-sql-sanitation/',
    },
)
