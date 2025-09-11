# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hpylib",
    version="0.1.0",
    author="Tong Zhou",
    author_email="zt9465@gmail.com",
    description="A small Python library for simple parallel programming (spawn, finish, pmap).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tongzhou80/hpylib",  # optional
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
)
