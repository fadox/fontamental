#!/usr/bin/env python
from setuptools import setup, find_packages
from sys import version_info

install_requires=["fonttools>=3.17.0","defcon>=0.3.4"]

if not (version_info[0] == 3 and version_info[1] >= 4):
    install_requires.append("singledispatch")

#readme = open("README.md").read()
#history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="fontamental",
    version="0.6.0",
    description="Fontamental, build fonts from fundamintal glyphs",
    #long_description=readme + "\n\n" + history,
    author="Abbas Majeed",
    author_email="fadox@gmx.net",
    url="https://github.com/fadox/fontamental",
    license="Simplified BSD",
    package_dir={"": "Lib"},
    packages=find_packages("Lib"),
    install_requires=install_requires,
    test_suite="tests",
    setup_requires=[],
    zip_safe=False,
    keywords="fontamental",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: Qt",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5"
    ])