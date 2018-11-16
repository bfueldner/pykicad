#!/usr/bin/env python3
#
# Copyright (c) 2015, 2018 Benjamin Fueldner <benjamin@fueldner.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# Generate footprint files from csv table

import os
import csv
import argparse

import kicad.footprint.generator
from kicad.footprint.generators import *

string_keywords = ['generator', 'name', 'description', 'tags']

def string_to_int_or_float(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Footprint generator from csv table.')
    parser.add_argument('--csv', metavar = 'file', type = str, help = 'CSV formatted input table', required = True)
    parser.add_argument('--package3d-root', metavar = 'path', type = str, help = 'Root path for 3D models, searchpath will be path/csv_basename/symbol_name.wrl', required = False)
    parser.add_argument('--output-path', metavar = 'path', type = str, help = 'Output path for generated KiCAD footprint files', required = True)
    args = parser.parse_args()

    # Extract family name from csv file name
    package_family = os.path.splitext(os.path.basename(args.csv))[0]

    # Parse csv file and generate dict out of every line
    with open(args.csv, 'r') as csvfile:
        table = csv.reader(csvfile, delimiter = ',', quotechar = '"')
        first_row = True
        for row in table:
            # Take first row for dict keys
            if first_row == True:
                header = row
                first_row = False
            else:
                # Create dict and try to convert to int or even float
                data = dict(zip(header, row))
                for key in data:
                    if key not in string_keywords:
                        data[key] = string_to_int_or_float(data[key])

                # Strip generator
                generator = data['generator']
                del data['generator']

                # Look for 3D model
                data['model'] = None
                if args.package3d_root is not None:
                    for extension in kicad.config.packages3d.FILE_EXTENSION:
                        model_file = os.path.join(args.package3d_root, package_family + kicad.config.packages3d.FOLDER_EXTENSION, data['name'] + '.' + extension)
                        if os.path.isfile(model_file):
                            data['model'] = os.path.join(kicad.config.packages3d.ROOT, package_family + kicad.config.packages3d.FOLDER_EXTENSION, data['name'] + '.' + extension)
                            break

                if generator in kicad.footprint.generator.registry.keys():
                    gen = kicad.footprint.generator.registry[generator](**data)

                    filename = data['name'] + kicad.config.footprint.FILE_EXTENSION
                    if data['model'] is not None:
                        print("Generate '{}' with package3d '{}'".format(filename, data['model']))
                    else:
                        print("Generate '{}'".format(filename))

                    output = open(os.path.join(args.output_path, filename), "w")
                    output.write(str(gen))
                    output.close()
                    del gen
                else:
                    print("Unknown footprint generator '{}'".format(generator))
