# Fontamental

Fontamental, is a python library to extract the Fundamental glyphs of font, in a small abstract font, which can use in the re-production of the original font in new ways and weights.

The abstract font format and glyph names are inspired by the project of "Ali Uni font", and the "Mada" project by Khaled Hosni.

Goal in the first stage is to cover the entire Arabic glyphs range in the unicode standard.



## Getting started
### Installation
Fontamentals requires Python 3.5 (or later).

- **OS X**:  Install using Homebrew: brew install python3
- **Windows**:  Download installer from python.org/downloads
- **Linux**:  It's usually packaged with the OS.

Set up a new Python virtual environment. Although this is not required, it's highly recommended, since Fontamentals has some of dependencies, which may (or may not) conflict with other modules you installed globally.

To create a new virtual environment in ENV_DIR:
```sh
$ python3 -m venv ENV_DIR
```

This creates a new ENV_DIR folder (you can choose the name you want). 
The bin subfolder (or Scripts if you are on Windows) contains a new python executable, and the pip installer linked to that.

Activate the newly created environment:

**OS X or Linux**: 
```sh
$ source ENV_DIR/bin/activate
```

**Windows**: 
```sh
ENV_DIR\Scripts\activate.bat
```

This temporarily adds the virtual environment's scripts folder to your console's PATH, so you can access python, pip and the Fontamental script from anywhere.

Run deactivate when you wish to exit the virtual environment. This restores the default system PATH.

##### clone the repositroy:
git clone https://github.com/fadox/fontamental.git

from the root folder of the project install the requirements:

```sh
$ cd fontamental
$ pip install -r requriements.txt
```

Use pip to install Fontamentals in "editable" mode:
```sh
$ pip install --editable .
```
this will add two binary tools to your command line terminal **minify** & **maxify**

## Minify a Font
One of the main functions of this script, to extract the main Arabic glyphs shapes, into a minified font, which can used to generate a full functional font again later.
To do this, you need to save a font to UFO format, say to **base.ufo** as example.
to meinify this font, change to the folder where the font saved, and run this command
```sh
$ minify base.ufo
```
this will generate the minified version of the font named **_mini.ufo**

## Maxify a Font
You can to edit the _mini.ufo font in any font editor that supported this format.
After finishing with your changes, you will use it to generate the whole range of Arabic glyphs, using our **maxify** command
```sh
$ maxify _mini.ufo
```
this will generate an OTF font in the same folder, which containes all necessary OTF features to use the font directly in any text editing programm.

## configurations
As we are trying to include all necessary data to generate the fonts in Fontamental database, but it is alloways posible to include your indevedual changes in the font by setting a configurations file beside the **_mini.ufo** font. The structure of this config file, is showen in the example in the test folder.

