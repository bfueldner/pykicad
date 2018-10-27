#!/usr/bin/python3

import os
import sys
import csv
import argparse

import kicad.config
#import symbol
#from symbol import cfg
#import traceback

string_keywords = ['symbol', 'name', 'description', 'reference', 'keyword', 'manufacturer', 'alias', 'document', 'footprint']

def string_to_int_or_float(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Symbols generator from csv table.')
    parser.add_argument('--csv', type = str, help = 'CSV formatted input table', required = True)
    parser.add_argument('--template-path', type = str, help = 'Path to symbol templates', required = True)
    parser.add_argument('--library', type = str, help = 'Output file for generated KiCAD library', required = True)
    parser.add_argument('--description', type = str, help = 'Output file for generated KiCAD library description', required = True)
    parser.add_argument('--document-root', type = str, help = 'Root for document path', required = True)
#    parser.add_argument('--table_path', type = str, help = 'Path to table based symbols', required = True)
    args = parser.parse_args()

    library = open(args.library, "w")
    library.write(kicad.config.symbols.LIBRARY_START)
    description = open(args.description, "w")
    description.write(kicad.config.symbols.DESCRIPTION_START)

    with open(args.csv, 'r') as csvfile:
        table = csv.reader(csvfile, delimiter=',', quotechar='\"')

        first_row = True
        last_name = ''
        first_element = True
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
                    if 'sym' in locals():
                        sym.optimize()
                        symbol_output.write("\n".join(sym.renderSymbol()))
                        desc_output.write("\n".join(sym.renderDescription()))
                        del sym

                    # Simple error checking
                    if 'reference' not in data:
                        raise Exception("Missing required field 'reference' in CSV data")

                    # Check optional fields
                    if 'footprint' not in data:
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
                        if os.path.isfile(data['document']):
                            data['document'] = os.path.join(args.document_root, data['document'])
                        else:
                            print("Warning: Document '{}' not found".format(data['document']))
                            data['document'] = ''

                    if 'section' not in data:
                        data['section'] = ''

                    sym = symbol.Symbol(data['name'], data['reference'], data['footprint'], data['alias'], data['description'], data['keywords'], data['document'])
                    last_name = data['name']
                    first_element = True

                if 'unit' not in data:
                    data['unit'] = 0

                unit = int(data['unit'])
                if os.path.isfile(template_file):
                    sym.load(template_file, unit, symbol.representation.normal, data, firstElement)
                elif os.path.isfile(table_file):
                    sym.fromCSV(table_file, unit, data['section'], unit != 0)
                    #if not unit and 'value' in data:
                    #   sym.addModule(symbol.Text(0, 0, data['value'], cfg.SYMBOL_TEXT_SIZE))

                #elif os.path.isfile(port_table_file):
                #   sym.fromCSV(port_table_file, int(data['unit']), cfg.SYMBOL_PIN_TEXT_OFFSET, False)
                else:
                    raise Exception("Template file '%s' or table file '%s' does not exist!"%(template_file, table_file))

                # Every element may contain field elements, but we only load them from the first one!
                if first_element:
                    if not sym.setFields(data):
                    #   print "Error in ", template_file
                        raise Exception("Error setting fields %s"%(template_file))
                    #sym.setDescriptions(data)
                    first_element = False

                # TODO: Check keyword(s) or tags delimiter (modules, symbols)
                # TODO: Check datasheet link with user defined variable?
                # TODO: Add modules prefix into footprint entry
                # TODO: Template geometry check after import?
                print(data)


    library.write(kicad.config.symbols.LIBRARY_END)
    description.write(kicad.config.symbols.DESCRIPTION_END)

    x = """
        if 'sym' in locals():
            sym.optimize()
            symbol_output.write("\n".join(sym.renderSymbol()))
            desc_output.write("\n".join(sym.renderDescription()))
            del sym
        symbol_output.write("#\n# End Library\n")
        desc_output.write("#\n# End Doc Library\n")
    except Exception as e:
        if os.path.isfile(args.symbol):
            os.remove(args.symbol)
        if os.path.isfile(args.desc):
            os.remove(args.desc)
        traceback.print_exc()
        sys.exit(2)
#sym = symbol.Symbol()
#sym.load("data/template/test.lib")
#print sym.render_()"""
