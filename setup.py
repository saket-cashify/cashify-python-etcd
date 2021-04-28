import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='cashifypythonetcd',
    version='0.0.1',
    description='Get configurable values from ETCD',
    url='git@github.com:saket-cashify/cashify-python-etcd.git',
    author='Saket Agarwal',
    author_email='saket.a@cashify.in',
    license='unlicense',
    packages=['cashifypythonetcd'],
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=[
        'python-etcd',
    ],
    zip_safe=False
)
