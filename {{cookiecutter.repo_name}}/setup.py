#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
import os


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


install_requires = read("requirements.txt")

setup(
    name="{{ cookiecutter.repo_name }}",
    author="{{ cookiecutter.author }}",
    author_email = "{{ cookiecutter.author_email }}"
    version=read(".version"),
    description="{{ cookiecutter.short_description }}",
    url="https://github.com/{{ cookiecutter.author }}/{{ cookiecutter.repo_name }}",
    long_description=read("README.md"),
    platforms=["Linux"],
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.repo_name }} = {{ cookiecutter.module_name }}.{{ cookiecutter.module_name }}:main"
        ]
    },
)
