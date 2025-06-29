#!/usr/bin/env python3
"""
Setup script for Instagram Bot
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "Instagram Bot for educational purposes"

# Read requirements
def read_requirements():
    try:
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            return [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        return [
            "selenium>=4.15.0",
            "webdriver-manager>=4.0.0",
            "python-dotenv>=1.0.0",
            "requests>=2.31.0",
            "beautifulsoup4>=4.12.0",
            "lxml>=4.9.0"
        ]

# Get version
def get_version():
    version_file = "version.txt"
    if os.path.exists(version_file):
        with open(version_file, "r") as f:
            return f.read().strip()
    return "1.0.0"

setup(
    name="instagram-bot",
    version=get_version(),
    author="Educational Bot Developer",
    author_email="educational@example.com",
    description="An educational Instagram bot for learning web automation",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/instagram-bot",
    packages=find_packages(),
    py_modules=["instagram_bot", "run_bot", "test_setup"],
    classifiers=[
        "Development Status :: 4 - Beta",
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
        "Programming Language :: Python :: 3.13",
        "Topic :: Education",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "instagram-bot=instagram_bot:main",
            "run-instagram-bot=run_bot:main",
            "test-instagram-bot=test_setup:main",
        ],
    },
    keywords="instagram bot automation selenium education web scraping",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/instagram-bot/issues",
        "Source": "https://github.com/yourusername/instagram-bot",
        "Documentation": "https://github.com/yourusername/instagram-bot#readme",
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.env.example"],
    },
    zip_safe=False,
) 