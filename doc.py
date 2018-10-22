#!/usr/bin/env python3

import os
import csv
import argparse

import kicad.config
import kicad.schematic.type
import kicad.footprint.generator
from kicad.footprint.generators import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Documentation generator for this project.')
    parser.add_argument('--type', metavar = 'action', choices = ['config', 'footprint'], help = 'CSV formatted input table', required = True)
    parser.add_argument('--output', metavar = 'file', type = str, help = 'Output file with generated markdown documentation', required = True)
    args = parser.parse_args()


    if args.type == 'config':
        output = open(args.output, "w")
        output.write("# Configuration\n\n")

        output.write("## Field usage\n\n")
        for key in kicad.schematic.type.field:
            output.write("* **F{}:** {}\n".format(key.value, key))
        output.write("\n")

        output.write("## Symbol\n\n")

        output.write("## Footprint\n\n")

        keys = kicad.config.footprint.__dict__.keys()
        keys = [key for key in keys if '__' not in key]
    #    keys.sort()
        for key in keys:
            output.write("* **{}:** {}\n".format(key, kicad.config.footprint.__dict__[key]))



        output.close()

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
