# Fontamental

Fontamental, is a python library to extract the Fundamental glyphs of font, in a small abstract font, which can use in the re-production of the original font in new ways and weights.

The abstract font format and glyph names are inspired by the project of "Ali Uni font", and the "Mada" project by Khaled Hosni.

Goal in the first stage is to cover the entire Arabic glyphs range in the unicode standard.



Getting started

Install Python 3.5 (or later).

OS X: Install using Homebrew: brew install python3
Windows: Download installer from python.org/downloads
Linux: It's usually packaged with the OS.
Set up a new Python virtual environment. Although this is not required, it's highly recommended, since TruFont has lots of dependencies, which may (or may not) conflict with other modules you installed globally.

To create a new virtual environment in ENV_DIR:

python3 -m venv ENV_DIR

This creates a new ENV_DIR folder (you can choose the name you want). The bin subfolder (or Scripts if you are on Windows) contains a new python executable, and the pip installer linked to that.

Activate the newly created environment:

OS X or Linux: source ENV_DIR/bin/activate
Windows: ENV_DIR\Scripts\activate.bat
This temporarily adds the virtual environment's scripts folder to your console's PATH, so you can access python, pip and the trufont script from anywhere.

Run deactivate when you wish to exit the virtual environment. This restores the default system PATH.

clone the repositroy:
git clone https://github.com/<YOUR_USERNAME>/fontamentals

from the root folder of the project install the requirements:
pip install -r requriements.txt


Use pip to install Fontamentals in "editable" mode:

pip install --editable .

this will add two binary tools to the command line minify & maxify

