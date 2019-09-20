#!/usr/bin/python3

import os
import sys
import csv
import argparse

import kicad.config
import kicad.symbols.library

string_keywords = ['symbol', 'name', 'description', 'reference', 'keyword', 'manufacturer', 'alias', 'document', 'footprint']

def string_to_int_or_float(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value

def main():
    parser = argparse.ArgumentParser(description = 'Symbols generator from csv table.')
    parser.add_argument('--csv', type = str, help = 'CSV formatted input table', required = True)
    parser.add_argument('--template-path', type = str, help = 'Path to symbol templates', required = True)
    parser.add_argument('--table-path', type = str, help = 'Path to symbol tables', required = True)
    parser.add_argument('--modules-root', type = str, help = 'Root for modules path', required = True)
    parser.add_argument('--documents-root', type = str, help = 'Root for documents path', required = True)
    parser.add_argument('--library', type = str, help = 'Output file for generated KiCAD library', required = True)
    parser.add_argument('--description', type = str, help = 'Output file for generated KiCAD library description', required = True)
    args = parser.parse_args()

    symbols = kicad.symbols.library.symbols()
    descriptions = kicad.symbols.library.descriptions()

    with open(args.csv, 'r') as csvfile:
        table = csv.reader(csvfile, delimiter = ',', quotechar = '"')

        first_row = True
        last_name = ''
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

                # Check data for every line
                if 'symbol' not in data and 'name' not in data:
                    raise Exception("Missing required field 'symbol' and 'name' in CSV data")

                # Name changed, we have to save symbol and create a new one
                if last_name != data['name']:
                    if 'symbol' in locals():
                        symbol.optimize()
                        symbol.sort()
                        symbols.add(symbol)
                        del symbol

                    if 'description' in locals():
                        descriptions.add(description)
                        del description

                    # Simple error checking
                    if 'reference' not in data:
                        raise Exception("Missing required field 'reference' in CSV data")

                    # Check optional fields
                    if 'unit' not in data:
                        data['unit'] = 0

                    if 'section' not in data:
                        data['section'] = ''

                    if 'footprint' not in data:
                        data['footprint'] = ''
                    else:
                        if ':' in data['footprint']:
                            prefix, name = data['footprint'].split(':', 2)
                            if not os.path.isfile(os.path.join(args.modules_root, prefix + kicad.config.footprint.FOLDER_EXTENSION, name + kicad.config.footprint.FILE_EXTENSION)):
                                print("Warning: Footprint '{}' does not exist!".format(data['footprint']))
                                data['footprint'] = ''
                        else:
                            print("Warning: Footprint '{}' has old formatting scheme".format(data['footprint']))
                            data['footprint'] = ''

                    if 'alias' not in data:
                        data['alias'] = ''

                    if 'description' not in data:
                        data['description'] = ''

                    if 'keywords' not in data:
                        data['keywords'] = ''

                    if 'document' not in data:
                        data['document'] = ''
                    elif len(data['document']) > 0:
                        if os.path.isfile(os.path.join(args.documents_root, data['document'])):
                            data['document'] = os.path.join(kicad.config.documents.ROOT, data['document'])
                        else:
                            print("Warning: Document '{}' not found".format(data['document']))
                            data['document'] = ''

                    symbol = kicad.symbols.library.symbol(data['name'], data['reference'], data['footprint'], data['document'], data['alias'])
                    symbol.from_map(data, data['unit'])
                    description = kicad.symbols.library.description(data['name'], data['description'], data['keywords'], data['document'])

                    last_name = data['name']

                # Template symbol
                template_file = os.path.join(args.template_path, data['symbol'] + kicad.config.symbols.LIBRARY_EXTENSION)
                table_file = os.path.join(args.table_path, data['symbol'] + kicad.config.symbols.TABLE_EXTENSION)
                if os.path.isfile(template_file):
                    symbol.from_file(template_file, data, data['unit'])
                elif os.path.isfile(table_file):
                    symbol.from_csv(table_file, data, data['unit'])
                else:
                    raise Exception("Neither template symbol '{:s}' nor csv table '{:s}' found!".format(template_file, table_file))

                # TODO: Check keyword(s) or tags delimiter (modules, symbols)

    if 'symbol' in locals():
        symbol.optimize()
        symbol.sort()
        symbols.add(symbol)
        del symbol

    if 'description' in locals():
        descriptions.add(description)
        del description

    library = open(args.library, "w")
    library.write(str(symbols))
    library.close()

    description = open(args.description, "w")
    description.write(str(descriptions))
    description.close()

if __name__ == "__main__":
    main()
