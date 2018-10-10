#!/usr/bin/python
#
# Copyright (c) 2015 Benjamin Fueldner
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

import kicad.pcb.type

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
#    parser.add_argument('--package-root', metavar = 'path', type = str, help = 'Root path for 3D models, searchpath will be root_path/csv_basename/symbol_name.wrl', required = True)
#    parser.add_argument('--output-path', metavar = 'path', type = str, help = 'Output path for generated KiCAD footprint files', required = True)
    args = parser.parse_args()

    # Extract family name from csv file name
    package_family = os.path.splitext(os.path.basename(args.csv))[0]

    # Parse csv file and generate dict out of every line
    with open(args.csv, 'r') as csvfile:
        table = csv.reader(csvfile, delimiter=',', quotechar='\"')
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

                x = '''
                # Search for 3D model
                model_file = os.path.join(args.package_root, package_family, data['name'] + ".wrl" )
                if os.path.isfile(model_file):
                    data['model'] = os.path.join(package_family, data['name'] + ".wrl" )
                else:
                    data['model'] = ''

                if generator in fp.registry.keys():
                    gen = fp.registry[generator](**data)

                    output = open(args.output_path+'/'+data['name']+cfg.FOOTPRINT_EXTENSION, "w")
                    output.write(gen.render())
                    output.close()
                    del gen
                else:
                    print "Unknown footprint generator '"+generator+"'"
'''
