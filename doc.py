#!/usr/bin/env python3

import os
import csv
import argparse

import kicad.footprint.generator
from kicad.footprint.generators import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Documentation generator for this project.')
    parser.add_argument('--type', metavar = 'action', choices = ['config', 'footprint'], help = 'CSV formatted input table', required = True)
#    parser.add_argument('--package3d-root', metavar = 'path', type = str, help = 'Root path for 3D models, searchpath will be path/csv_basename/symbol_name.wrl', required = False)
    parser.add_argument('--output', metavar = 'file', type = str, help = 'Output file with generated markdown documentation', required = True)
    args = parser.parse_args()


    if args.type == 'config':
        print("Config")

    elif args.type == 'footprint':
        output = open(args.output, "w")
        output.write("# Footprint\n\n")

        for name in kicad.footprint.generator.registry:
            output.write("## Generator `{}`\n\n".format(name))
            output.write(kicad.footprint.generator.registry[name].__doc__)
            output.write("\n\n")

        output.close()
    else:
        print("Unknown action type")
        sys.exit(1)
