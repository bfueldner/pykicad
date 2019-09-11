#Symbol

`script/device.py` is a device generator, which generates devices based upon template symbols or table generated symbols. The date for the devices cames from a CSV formatted table.

**IMPORTANT:** This library does not support the $FPLIST (multiple footprints per device) entry. This makes it impossible to get a defined partnumber out of a generated BOM. So please avoid this keyword in static symbols!

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
