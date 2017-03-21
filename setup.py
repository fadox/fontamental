#!/usr/bin/env python
from setuptools import setup
from sys import version_info


install_requires = ["defcon>=0.2.0"]

if not (version_info[0] == 3 and version_info[1] >= 4):
    install_requires.append("singledispatch")

#readme = open("README.md").read()
#history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="fontamental",
    version="0.5.0",
    description="Extract fundamental glyphs from a font, and expand the result to new font",
    #long_description=readme + "\n\n" + history,
    author="Abbas Majeed",
    author_email="fadox@gmx.net",
    url="https://github.com/fadox/fontamental",
    license="Simplified BSD",
    packages=["fontamental"],
    install_requires=install_requires,
    setup_requires=[],
    zip_safe=False,
    keywords="fontamental",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4"
    ])