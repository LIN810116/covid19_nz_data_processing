from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import io

SETUP_DIR = os.path.dirname(os.path.abspath(__file__))


# List all of your Python package dependencies in the
# requirements.txt file

def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\n")
        return stream.read()


readme = readfile("README.md", split=True)[2:]  # skip title
# For requirements not hosted on PyPi place listings
# into the 'requirements.txt' file.
requires = [
    # minimal requirements listing
    "beautifulsoup4",
    "pandas",
    "xlrd",
    "requests",
    "numpy",
    "matplotlib",
]
source_license = readfile("LICENSE")

setup(
    name="covid19_nz_data_processing",
    version="0.0.1",
    description="Simple script to automatically fetch, process, and plot the NZ covid-19 cases data",
    long_description="\n".join(readme) + source_license,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Medical Science Apps."
    ],
    author="Auckland Bioengineering Institute",
    author_email="m.osanlouy@auckland.ac.nz",
    url="https://github.com/mahyar-osn/covid19_nz_data_processing/",
    license="Apache Software License",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)

