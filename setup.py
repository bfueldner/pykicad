import setuptools
import unittest

exec(open('pykicad/version.py').read())

with open("README.rst", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="pykicad",
    version=__version__,
    description="KiCAD symbol and footprint parser/generator",
    long_description=long_description,
    keywords="KiCAD symbol footprint device PCB",
    license="MIT",
    author="Benjamin Füldner",
    author_email="benjamin@fueldner.net",
    url="https://code.fueldner.net/opensource/pykicad",
    project_urls={
        'Source': 'https://github.com/bfueldner/pykicad',
        'Bug Reports': 'https://github.com/bfueldner/pykicad/issues',
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Hardware",
        "Topic :: Software Development",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "Topic :: Home Automation",
    ],
    python_requires='>=3.5',
#    entry_points={
#        'console_scripts': [
#            'svd2rst = scripts.svd2rst:main',
#        ],
#    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
