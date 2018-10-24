# kicad
KiCad library used in our projects. Main parts are generated using python scripts and input data from csv tables. This should give a very flexible base to add new symbols, footprings and parts.

All dimension are in millimeters/degree, if not otherwise noted.

## Naming conventions

- Filenames are lowercase and separated with underscore (e.g. resistor_1k5_chip_0805, dip_8_narrow)
- Devicesnames are uppercase and separated with underscore (e.g. SOIC_8_WIDE, 74HC595)

### Datasheets

- For one time:
    BC557.pdf

For multiple devices not following numbers:
    BC557_BC560.pdf

For multiple devices with following numbers (BC546, BC547, BC548, BC549, BC550):
    BC546_550.pdf
## Symbol

### Configuration

* **SYMBOL_DIR**: $ROOT_DIR/library
* **SYMBOL_DOC_END**: "#
* **SYMBOL_DOC_START**: EESchema-DOCLIB  Version 2.0
* **SYMBOL_LIB_END**: "#
* **SYMBOL_LIB_START**: "EESchema-LIBRARY Version 2.3
* **SYMBOL_LINE_WIDTH**: 20.0
* **SYMBOL_MIN_WIDTH**: 250.0
* **SYMBOL_NAME_SIZE**: 60.0
* **SYMBOL_PIN_GRID**: 100.0
* **SYMBOL_PIN_LENGTH**: 100.0
* **SYMBOL_PIN_NAME_SIZE**: 40.0
* **SYMBOL_PIN_NUMBER_SIZE**: 40.0
* **SYMBOL_PIN_SPACE**: 100.0
* **SYMBOL_PIN_TEXT_OFFSET**: 50.0
* **SYMBOL_SPACE_WIDTH**: 10.0
* **SYMBOL_TABLE_EXTENSION**: .csv
* **SYMBOL_TEMPLATE_EXTENSION**: .lib
* **SYMBOL_TEMPLATE_PATH**: data/template/
* **SYMBOL_TEXT_SIZE**: 60.0
* **SYMBOL_TEXT_SPACE**: 500.0

### Generators


## Footprint


### Configuration

[Configuration](doc/configuration.md)

### Generators

[Footprint generators](doc/footprint.md)

# Tutorial

[How to add new parts to library](doc/tutorial.md)

# 2do

[2do list](doc/2do.md)
