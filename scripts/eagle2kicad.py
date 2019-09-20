import os
import argparse
import xml.etree.ElementTree

import kicad.footprint.layer
import kicad.footprint.element
import kicad.footprint.generator

eagle_layer_to_kicad = {
    'Top': kicad.footprint.layer.copper_top,
    'Bottom': kicad.footprint.layer.copper_bottom,
    'tStop': kicad.footprint.layer.soldermask_top,
    'bStop': kicad.footprint.layer.soldermask_bottom,
    'tKeepout': kicad.footprint.layer.courtyard_top,
    'bKeepout': kicad.footprint.layer.courtyard_bottom,
    'tGlue': kicad.footprint.layer.adhes_top,
    'bGlue': kicad.footprint.layer.adhes_bottom,
    'tCream': kicad.footprint.layer.solderpaste_top,
    'bCream': kicad.footprint.layer.solderpaste_bottom,

    'tNames': kicad.footprint.layer.silkscreen_top,
    'bNames': kicad.footprint.layer.silkscreen_bottom,
    'tValues': kicad.footprint.layer.fabrication_top,
    'bValues': kicad.footprint.layer.fabrication_bottom,

    'tPlace': kicad.footprint.layer.silkscreen_top,
    'bPlace': kicad.footprint.layer.silkscreen_bottom,
    'tDocu': kicad.footprint.layer.silkscreen_top,
    'bDocu': kicad.footprint.layer.silkscreen_bottom,
}
layers = {}

class module(kicad.footprint.generator.base):

    def __init__(self, name):
        super().__init__(kicad.footprint.type.footprint.smd, name, None, None, None)

    def from_xml(self, element):
        if element.tag == 'description':
            self.description = element.text
        elif element.tag == 'wire':
            x1 = float(element.attrib['x1'])
            y1 = float(element.attrib['y1'])
            x2 = float(element.attrib['x2'])
            y2 = float(element.attrib['y2'])
            width = float(element.attrib['width'])
            layer = layers[int(element.attrib['layer'])]

            super().add(
                kicad.footprint.element.line(
                    layer,
                    x1, y1,
                    x2, y2,
                    width
                )
            )
        elif element.tag == 'text':
            x = float(element.attrib['x'])
            y = float(element.attrib['y'])
            if element.text == '>NAME':
                name = 'reference'
                value = 'REF**'
                layer = kicad.footprint.layer.silkscreen_top
                size = kicad.config.footprint.REFERENCE_FONT_SIZE
                thickness = kicad.config.footprint.REFERENCE_FONT_THICKNESS
            elif element.text == '>VALUE':
                name = 'value'
                value = 'VAL**'
                layer = kicad.footprint.layer.fabrication_top
                size = kicad.config.footprint.VALUE_FONT_SIZE
                thickness = kicad.config.footprint.VALUE_FONT_THICKNESS
            else:
                name = 'user'
                value = element.text
                layer = kicad.footprint.layer.user_comment
                size = kicad.config.footprint.VALUE_FONT_SIZE
                thickness = kicad.config.footprint.VALUE_FONT_THICKNESS

            super().add(
                kicad.footprint.element.text(
                    layer,
                    name,
                    value,
                    x,
                    y,
                    size,
                    thickness
                )
            )
        elif element.tag == 'smd':
            name = element.attrib['name']
            x = float(element.attrib['x'])
            y = float(element.attrib['y'])
            width = float(element.attrib['dx'])
            height = float(element.attrib['dy'])
        #   layer = layers[int(element.attrib['layer'])]
            angle = float(element.attrib['rot'].lstrip('R'))

            super().add(
                kicad.footprint.element.pad(
                    kicad.footprint.layers.smd,
                    name,
                    kicad.footprint.type.technology.smd,
                    kicad.footprint.type.shape.rectangle,
                    x, y,
                    width, height,
                    None,
                    angle
                )
            )
        elif element.tag == 'rectangle':
            x1 = float(element.attrib['x1'])
            y1 = float(element.attrib['y1'])
            x2 = float(element.attrib['x2'])
            y2 = float(element.attrib['y2'])
            layer = layers[int(element.attrib['layer'])]
            angle = int(element.attrib['rot'].lstrip('R'))

            if angle == 90:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            super().add(
                kicad.footprint.element.rectangle(
                    layer,
                    x1,
                    y1,
                    x2,
                    y2,
                    kicad.config.footprint.PACKAGE_LINE_WIDTH
                )
            )
        elif element.tag == 'polygon':
            width = float(element.attrib['width'])
            layer = layers[int(element.attrib['layer'])]

            last_x = None
            last_y = None
            for vertex in element:
                x = float(vertex.attrib['x'])
                y = float(vertex.attrib['y'])

                if last_x is None and last_y is None:
                    first_x = x
                    first_y = y
                else:
                    super().add(
                        kicad.footprint.element.line(
                            layer,
                            last_x,
                            last_y,
                            x,
                            y,
                            width
                        )
                    )
                last_x = x
                last_y = y

            super().add(
                kicad.footprint.element.line(
                    layer,
                    last_x,
                    last_y,
                    first_x,
                    first_y,
                    width
                )
            )
        else:
            print("Skip tag '{}'".format(element.tag))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Convert Eagle xml library to KiCAD symbols/footprints.')
#   parser.add_argument('-l', '--list', dest = "list", action = 'store_const', const = True, default = False, help = 'List all symbols/footprints')
#    parser.add_argument('--harmonize', dest = "harmonize", action = 'store_const', const = True, default = False, help = 'Harmonize symbol/footprint to KiCAD configuration (font, line_with, ...)')
    parser.add_argument('--library', metavar = 'file', type = str, help = 'Eagle xml library (.lbr)', required = True)
#   parser.add_argument('--csv', metavar = 'csv', type = str, help = 'CSV formatted input table', required = True)
    parser.add_argument('--output-path', metavar = 'path', type = str, help = 'Output path for generated KiCAD file', required = True)
#   parser.add_argument('--harmonize', metavar = 'harmonize', help = 'Harmonize symbol/footprint to KiCAD configuration (font, line_with, ...)', required = False)
#   parser.add_argument('-l', metavar = 'list', help = 'List all symbols/footprints', required = False)
    parser.add_argument('--action', choices=['list', 'extract'], help = 'Script action', required = True)
    parser.add_argument('--name', type = str, help = 'Name to extract')
    args = parser.parse_args()

    tree = xml.etree.ElementTree.parse(args.library)
    root = tree.getroot()

    for layer in root.iterfind(".//layer"):
        name = layer.attrib['name']
        if name in eagle_layer_to_kicad:
            layers[int(layer.attrib['number'])] = eagle_layer_to_kicad[name]

    if args.action == 'list':
        packages = []
        for package in root.iterfind(".//package"):
            packages.append(package.attrib['name'])

        packages.sort()
        for package in packages:
            print(package)
    elif args.action == 'extract':
        package = root.find(".//package[@name='{}']".format(args.name))

        new_module = module(args.name)

        for element in package:
            new_module.from_xml(element)

        file = open(os.path.join(args.output_path, args.name + kicad.config.footprint.FILE_EXTENSION), "w")
        file.write(str(new_module))
        file.close()

    x = '''
    tree = etree.parse(args.lbr)
    root = tree.getroot()

    if args.list:
        print "Symbols:"
        for symbol in root.iterfind(".//symbol"):
        #   desc = package.find("description")
        #   if desc is not None:
        #       print re.sub('<[^<]+?>', '', desc.text)
        #   else:
        #       print "Keine Beschreibung"
            print symbol.attrib['name']

        print "\nFootprints:"

        for package in root.iterfind(".//package"):
        #   desc = package.find("description")
        #   if desc is not None:
        #       print re.sub('<[^<]+?>', '', desc.text)
        #   else:
        #       print "Keine Beschreibung"
            print package.attrib['name']
        exit()

    layer_map = {}
    for layer in root.iterfind(".//layer"):
        layer_map[int(layer.attrib['number'])] = layer.attrib['name']
    #print layer_map

    kicad_layer = {}
    kicad_layer[27] = cfg.FOOTPRINT_VALUE_LAYER      # tValues
    kicad_layer[25] = cfg.FOOTPRINT_REFERENCE_LAYER  # tNames
    kicad_layer[21] = cfg.FOOTPRINT_PACKAGE_LAYER    # tPlace
    kicad_layer[51] = cfg.FOOTPRINT_PACKAGE_LAYER    # tDocu
    kicad_layer[39] = cfg.FOOTPRINT_PACKAGE_LAYER    # tKeepout
    kicad_layer[43] = cfg.FOOTPRINT_PACKAGE_LAYER    # vRestrict

    #footprint = fp.base()
    footprint = []

    name = ""
    description = ""
    smd = False
    for package in root.iterfind(".//package"):
        print package.attrib['name']

        if package.attrib['name'] == 'S':
            name = package.attrib['name']
            for element in package:

                elif element.tag == "text":
                    param = {}

                elif element.tag == "wire":
                    param = {}
                    param['layer'] = kicad_layer[int(element.attrib['layer'])]
                    param['x1'] = float(element.attrib['x1'])
                    param['y1'] = float(element.attrib['y1'])
                    param['x2'] = float(element.attrib['x2'])
                    param['y2'] = float(element.attrib['y2'])
                    param['width'] = float(element.attrib['width'])
                    footprint.append(fp.line(**param))
                elif element.tag == "rectangle":

                else:
                    print element.tag, element.text
            break

    fprint = fp.base(name, description, "", smd, False)
    for element in footprint:
        fprint.add(element)
    print fprint.render()
    '''

    #events = ("start", "end")
    #context = etree.iterparse(text, events=events)
    #for action, elem in context:
    #    print("%s: %s" % (action, elem.tag))
