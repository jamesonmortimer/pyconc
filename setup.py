#!/usr/bin/env python3
"""
Setup script for PyConc - Python Concurrency Examples
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pyconc",
    version="1.0.0",
    author="PyConc Contributors",
    author_email="contributors@pyconc.dev",
    description="Python Concurrency Examples - A comprehensive collection of concurrency problems, solutions, and patterns",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pyconc",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/pyconc/issues",
        "Source": "https://github.com/yourusername/pyconc",
        "Documentation": "https://github.com/yourusername/pyconc#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Distributed Computing",
        "Topic :: Education",
    ],
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.10.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.800",
        ],
        "test": [
            "pytest>=6.0.0",
            "pytest-cov>=2.10.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "pyconc=pyconc.py:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="concurrency, threading, deadlock, livelock, starvation, threadpool, examples, education",
) 