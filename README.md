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

F#-Field usage:
* **F0**: Reference
* **F1**: Name
* **F2**: Footprint
* **F3**: Document
* **F4**: Manufacturer
* **F5**: Value
* **F6**: Tolerance
* **F7**: Temperature
* **F8**: Model (Spice)
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

* **FOOTPRINT_3D_DIR**: $FOOTPRINT_DIR/3d-package
* **FOOTPRINT_ANNULAR_RING**: 0.15
* **FOOTPRINT_BIG_DEVICE**: 100.0
* **FOOTPRINT_DATA_DIR**: $DATA_DIR/footprint
* **FOOTPRINT_DIR**: $ROOT_DIR/tmp/modules
* **FOOTPRINT_DRILL**: 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 1.0
* **FOOTPRINT_EXTENSION**: .kicad_mod
* **FOOTPRINT_FIELD**: 2.0
* **FOOTPRINT_MEDIUM_DEVICE**: 20.0
* **FOOTPRINT_NAME**: Footprint
* **FOOTPRINT_PACKAGE_LAYER**: F.SilkS
* **FOOTPRINT_PACKAGE_LINE_WIDTH**: 0.3
* **FOOTPRINT_PRECISION**: 3.0
* **FOOTPRINT_REFERENCE_FONT_SIZE**: 1.5
* **FOOTPRINT_REFERENCE_FONT_THICKNESS**: 0.15
* **FOOTPRINT_REFERENCE_LAYER**: F.SilkS
* **FOOTPRINT_SMALL_DEVICE**: 5.0
* **FOOTPRINT_SMD_LAYERS**: F.Cu F.Paste F.Mask
* **FOOTPRINT_THD_LAYERS**: *.Cu *.Mask F.SilkS
* **FOOTPRINT_VALUE_FONT_SIZE**: 1.5
* **FOOTPRINT_VALUE_FONT_THICKNESS**: 0.15
* **FOOTPRINT_VALUE_LAYER**: F.Fab

### Generators

