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

#### Adding the master component file to the Makefile ####
In our case, just for demonstration purpose, we’ll add a master component file name pic.csv. Before creating the file, open the Makefile in the root directory of the project and look for the line:

```
SYMBOL_LIBRARIES := $(LIBRARY_ROOT)/supply.lib \
    $(LIBRARY_ROOT)/led.lib \
    $(LIBRARY_ROOT)/transistor.lib \
    $(LIBRARY_ROOT)/logic.lib \
    $(LIBRARY_ROOT)/diode.lib \
    $(LIBRARY_ROOT)/driver.lib \
    $(LIBRARY_ROOT)/connector.lib \
    $(LIBRARY_ROOT)/mcu.lib \
    $(LIBRARY_ROOT)/resistor.lib \
    $(LIBRARY_ROOT)/inductor.lib \
    $(LIBRARY_ROOT)/capacitor.lib \
    $(LIBRARY_ROOT)/rf.lib

```

Now add $(LIBRARY_ROOT)/pic.lib to the `LIBRARY_SYMBOLS` variable. This will instruct the makefile to also process the pic.csv file.

#### Creating the master component file ####

Create a new file named pic.csv in the folder data/device, either as an empty file in which you can copy the header from above or by copying an existing table based master file such as mcu.csv or rf.csv.

Most MCUs have multiplexed pins, which means that a certain pin can be connected internally to different functional modules depending on the device configuration. To make clear which device functions are meant to be used in the schematic,
we choose to group the different device functions in kicad modules. This will make a single pin available through different modules which might seem unusual at first but has the advantage of identifying directly the functions really going to be used.
Should a single pin be referenced twice through two different functions, this will be detected while doing the layout. 

The first line of the PIC file below the header must be filed out completely as this is the line used to fill the contents of the different fields belonging to our new component.
The following lines only need to contain only the first for columns.

Column | Description
-----------------------------------------------------------
symbol|Path to the csv file describing the kicad unit
name|Name of the symbol the unit belongs to
section|Name of the unit (appears as legend in the symbol)
unit|index of the unit the data is to be assigned to
reference|Kicad symbol reference (usually IC)
footprint|name of the package template
alias|Other names of the chip which have the same pin out functions. (may be other temperature variants etc...)
description|Short description of the symbol. Used as quick reference in KiCad.
keywords|Keywords you would like to find your symbol under in KiCad.
document|Path to the components datasheet.

In the case of the PIC16F87XA, we can split the functionalities in the following units:

- CLOCK
- GPIO
- ADC
- COMP
- TIMER
- SPI
- DEBUG
- I2C
- USART
- POWER

If you look in the file data/device/pic.csv you will find the corresponding entries.

#### Creating the unit description files ####

The unit desciption files are lookup up under the data/symbol directory. So if you enter 
microchip/PIC16F874A/PORTA_PDIP as the symbol source path, the scripts will look for the file in the directory:
data/symbol/microchip/PIC16F874A/PORTA_PDIP.

Taking PORTA as example, let’s create the file in data/symbol/microchip/PORTA_PDIP.csv

The columns present in the file are the following:

Column|Description
-----------------------------------------
number| This is the index of the pin being specified
name|Name of the pin which is to appear in the schematic.
type|input, output, bidirectional, tristate, passive, powerInput, powerOutput, openCollector, openEmitter, notConnected
shape|line, invisible, clock, invertedClock, inputLow, clockLow, outputLow, fallingEdgeClock, nonLogic
direction|The pin orientation : left,   right,  up or down

Now this step is pretty straightforward but pretty tedious.

#### Regenerating the libraries ####

Last step to see your new symbol appear in KiCad, rebuild the library. Run make at the root of the library project.


### Kicad symbol template overlays ###
