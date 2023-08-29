from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '1.0.0'
DESCRIPTION = 'Python library to interact with the API of the National Institute of Statistics (INE ) of Spain that ' \
              'offers the data Dissemination System of the Population and Housing Censuses 2021 (SDC21). '
PACKAGE_NAME = 'censosine21'
AUTHOR = 'Patricio Soriano @sigdeletras'
EMAIL = 'pasoriano@gmail.com'
GITHUB_URL = 'https://github.com/sigdeletras/censosine21'

setup(
    name = PACKAGE_NAME,
    packages = ['censosine21','censosine21.entities'],
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)