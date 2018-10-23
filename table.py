#!/usr/bin/env python3

import os
import glob
import csv
import argparse
import configparser

import kicad.footprint.type
#import kicad.config
#import kicad.schematic.type
#import kicad.footprint.generator
#from kicad.footprint.generators import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Configuration generator for KiCAD.')
    parser.add_argument('--type', metavar = 'action', choices = ['footprint'], help = 'CSV formatted input table', required = True)
    parser.add_argument('--library', metavar = 'path', type = str, help = 'Path for library', required = True)
    parser.add_argument('--output', metavar = 'file', type = str, help = 'Generated output file', required = True)
    args = parser.parse_args()

    # Generate footprint table
    if args.type == 'footprint':
        lib = []
        for dir in glob.glob(os.path.join(args.library, "*.pretty")):
            uri = os.path.join("${KISYSMOD}", os.path.relpath(dir, args.library))
            name = os.path.splitext(os.path.basename(dir))[0].title()

            lib.append(str(
                kicad.footprint.type.key_data('lib', [
                    kicad.footprint.type.key_data('name', name),
                    kicad.footprint.type.key_data('type', 'KiCad'),
                    kicad.footprint.type.key_data('uri', uri),
                    kicad.footprint.type.key_data('options', '""'),
                    kicad.footprint.type.key_data('descr', kicad.footprint.type.name(''))
                ])
            ) + "\n")

        fp_lib_table = kicad.footprint.type.key_data('fp_lib_table\n', lib)

        output = open(args.output, "w")
        output.write(str(fp_lib_table))
        output.close()
    else:
        print("Unknown action type")
        sys.exit(1)
