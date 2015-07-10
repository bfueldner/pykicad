#Symbol

`script/device.py` is a device generator, which generates devices based upon template symbols or table generated symbols. The date for the devices cames from a CSV formatted table.

##CSV

Required fields for every line:
- symbol
- name
- unit

Required fields only for first line of device:
- reference

Optional fields (only usefull on first line of device):
- footprint
- alias
- description
- keywords
- document
- section (only table based symbols)
- _any_alpha_numeric_name_ (only in template based symbols)

## Template symbol

## Table symbols

[Link](README.md)
