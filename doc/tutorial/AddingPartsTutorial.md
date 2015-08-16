# PiWARE Kicad Library Tutorial #
## Introduction ##
This tutorial will guide you through the steps necessary to add new parts to the PiWARE Kicad Library.
The parts are generated using a mixed template and table based approach which should make it rather simple to add parts to the library.

## Directory structure overview ##
Before we start adding parts, let’s start by looking at the directory structure of the library project.
The directory layout is summurized in the following table:

Directory|Descriptions
---------|------------
doc|Component data sheets
data|Input data for the kicad library
data/device| Master device defintion csv files
data/template| Kicad template files
data/symbol|csv files for the table based component definitions
template|kicad project file templates
script|Generation scripts

## Symbol generator ##

The symbol generation process is controlled through a central Makefile located in the project root.


## Generation strategies ##
There are two possible methodologies to produce KiCAD symbols, either using an overlay of KiCAD symbol files which are used as templates, or by completely defining a symbol through a table based definition.
The template overlays are meant to define symbols which have a more complex graphical representation with different characteristics such as value, packaging, tolerance etc...
The table based approach is meant to define symbols representing chips such as MCU or CPU modules. The following paragraphs will guide you through adding a new symbol with each methodology.

### Common steps ###
The generation of all symbols is controlled by a “master” component list csv file. This file is located in the ‘data/device’ folder and is referenced in the central Makefile.
A master component file has the following layout:

symbol|name|section|unit|reference|footprint|alias|description|keywords|document
--------------------------------------------------------------------------------
si/EZR32LG/PORTA|EZR32LG230FE55G|Port A|1|IC|qfn_64|EZR32LG230FF55G EZR32LG230FG55G EZR32LG230FE60G EZR32LG230FF60G EZR32LG230FG60G EZR32LG230FE61G EZR32LG230FF61G EZR32LG230FG61G EZR32LG230FE63G EZR32LG230FF63G EZR32LG230FG63G EZR32LG230FE67G EZR32LG230FF67G EZR32LG230FG67G EZR32LG230FE68G EZR32LG230FF68G EZR32LG230FG68G EZR32LG230FE69G EZR32LG230FF69G EZR32LG230FG69G|EZR32LG230 Wireless MCU family with ARM Cortex-M3 CPU and sub-GHz Radio|"rf| mcu| cortex-m3"|doc/rf/EZR32LG/EZR230LG.pdf
si/EZR32LG/PORTB|EZR32LG230FE55G|Port B|2||||||
si/EZR32LG/PORTC|EZR32LG230FE55G|Port C|3||||||
...|...|...|...|...|...|...|...|...|...

In this file we define the association of templates or tables used to create a symbol. Each line or set of lines are combined to produce a kicad symbol inside the component library of the same name as the master device file.
For example, the file rf.csv will produce a kicad library rd.lib containing the symbols listed in the csv.

The columns listed in the table below are common to the two generation strategies and are mandatory:
Column|Description
------------------
symbol|name relative to the data/template or data/symbol director of the source file to use for the symbol 
name|Name of the symbol in the kicad library
reference|kicad symbol reference ID. (Example : for a resistor, R)
footprint|Name of the footprint to associate to the component
keywords|kicad symbol keywords associated with the symbol. This is used to find parts quickly through the kicad symbol search.
description|Textual description of the symbol giving a quick idea of what the component is good for.

### CSV table module descriptions ###

Let’s add the PIC16F87XA to the kicad library together. This will hopefully give you a good enough overview of the tools to let you add any table based component you need.

1. Download the datasheet
2. Modify the Makefile to process the master component file
3. Create or extend the master component file
4. Create the symbol unit description files

#### Component documentation ####
First we will need to get a copy of the PIC16F87XA datasheet. The file should be stored here: doc/mcu/microchip/PIC16F87XA.pdf.

Step 1 - Datasheet

The first step is to download and store the datasheet to your symbol in the appropriate documentation directory.

Step 2 - Define symbol modules

Now open in the data/device directory the csv file corresponding to your symbol type. If no csv file exists corresponding to your device type, you can create one from an existing file
and you will need to add it to the Makefile in the root directory.

In our case we are looking for the mcu.csv file. You can edit this file in your favorite csv file editor (for example OpenOffice.org Calc).



For MCU or CPU modules some module functions are available through several pins which can be configured per software. In order to handle this elegantly and prevent layout mistakes, 
we prefer to split the functionalities accross kicad symbol modules. For example on one chip you will define the  

### Kicad symbol template overlays ###
