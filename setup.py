"""KiCAD setuptools configuration."""

import setuptools
import pykicadlib.version

with open("README.rst", "r") as file:
    LONG_DESCRIPTION = file.read()

setuptools.setup(
    name="pykicadlib",
    version=pykicadlib.__version__,
    description="Python KiCAD library parser/generator",
    long_description=LONG_DESCRIPTION,
    keywords="KiCAD symbol footprint device PCB schematic",
    license="MIT",
    author="Benjamin Füldner",
    author_email="benjamin@fueldner.net",
    url="https://code.fueldner.net/opensource/pykicadlib",
    project_urls={
        'Source': 'https://github.com/bfueldner/pykicadlib',
        'Bug Reports': 'https://github.com/bfueldner/pykicadlib/issues',
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
    entry_points={
        'console_scripts': [
            'kicadlib-symbols = scripts.symbols:main',
        ],
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
