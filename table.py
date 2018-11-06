#!/usr/bin/env python3

import os
import glob
import csv
import argparse
import configparser

import kicad.config
import kicad.footprint.type

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Configuration generator for KiCAD.')
    parser.add_argument('--type', metavar = 'action', choices = ['modules', 'symbols'], help = 'CSV formatted input table', required = True)
    parser.add_argument('--library', metavar = 'path', type = str, help = 'Path for library', required = True)
    parser.add_argument('--csv', metavar = 'file', type = str, help = 'CSV table with name/description mapping', required = True)
    parser.add_argument('--output', metavar = 'file', type = str, help = 'Generated output file', required = True)
    args = parser.parse_args()

    mapping = {}
    with open(args.csv, 'r') as csvfile:
        table = csv.reader(csvfile, delimiter = ',', quotechar = '\"')

        first_row = True
        last_name = ''
        for row in table:
            # Take first row for dict keys
            if first_row == True:
                header = row
                first_row = False
            else:
                # Create dict and load mapping
                data = dict(zip(header, row))
                mapping[data['name']] = data['description']

    # Generate modules table
    if args.type == 'modules':
        lib = []
        for dir in glob.glob(os.path.join(args.library, '*' + kicad.config.footprint.FOLDER_EXTENSION)):
            uri = os.path.join(kicad.config.footprint.ROOT, os.path.relpath(dir, args.library))
            name = os.path.splitext(os.path.basename(dir))[0]
            if name not in mapping:
                print("Warning: No description found for module '{}'".format(name))

            lib.append(str(
                kicad.footprint.type.key_data('lib', [
                    kicad.footprint.type.key_data('name', name),
                    kicad.footprint.type.key_data('type', 'KiCad'),
                    kicad.footprint.type.key_data('uri', uri),
                    kicad.footprint.type.key_data('options', '""'),
                    kicad.footprint.type.key_data('descr', '"{}"'.format(mapping[name] if name in mapping else ''))
                ])
            ) + "\n")

        fp_lib_table = kicad.footprint.type.key_data('fp_lib_table\n', lib)

        output = open(args.output, "w")
        output.write(str(fp_lib_table) + "\n")
        output.close()
    # Generate symbols table
    elif args.type == 'symbols':
        lib = []
        for file in glob.glob(os.path.join(args.library, '*' + kicad.config.symbols.LIBRARY_EXTENSION)):
            uri = os.path.join(kicad.config.symbols.ROOT, os.path.relpath(file, args.library))
            name = os.path.splitext(os.path.basename(file))[0]
            if name not in mapping:
                print("Warning: No description found for symbols '{}'".format(name))

            lib.append(str(
                kicad.footprint.type.key_data('lib', [
                    kicad.footprint.type.key_data('name', name),
                    kicad.footprint.type.key_data('type', 'Legacy'),
                    kicad.footprint.type.key_data('uri', uri),
                    kicad.footprint.type.key_data('options', '""'),
                    kicad.footprint.type.key_data('descr', '"{}"'.format(mapping[name] if name in mapping else ''))
                ])
            ) + "\n")

        sym_lib_table = kicad.footprint.type.key_data('sym_lib_table\n', lib)

        output = open(args.output, "w")
        output.write(str(sym_lib_table) + "\n")
        output.close()
    else:
        print("Unknown action type")
        sys.exit(1)
