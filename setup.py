#!/usr/bin/env python3
"""
Setup script for the Fun Higher Order Functions package.
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()

setup(
    name="fun-higher-order",
    version="1.0.0",
    author="Fun Higher Order Workshop",
    author_email="workshop@example.com",
    description="Higher-order functions toolkit for Python",
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/maxbmaapc/fun-higher-order-workshop-python",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    entry_points={
        "console_scripts": [
            "fun-higher-order=fun_higher_order.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)