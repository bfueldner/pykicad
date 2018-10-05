from enum import Enum

class position(Enum):
    all = '*'
    top = 'F'
    bottom = 'B'
    drawing = 'Dwgs'
    comment = 'Cmts'
    eco1 = 'Eco1'
    eco2 = 'Eco2'
    edge = 'Edge'

    in1 = 'In1'
    in2 = 'In2'
    in3 = 'In3'
    in4 = 'In4'
    in5 = 'In5'
    in6 = 'In6'

    def __str__(self):
        return self.value

class type(Enum):
    copper = 'Cu'
    adhes = 'Adhes' # Glue
    paste = 'Paste' # Solderpaste
    silkscreen = 'SilkS'
    soldermask = 'Mask' # Soldermask
    courtyard = 'CrtYd' # Footprint outline
    fabrication = 'Fab' # Footprint mounting (device type)
    cutting = 'Cuts'
    user = 'User'

    drawing = 'Dwgs'
    comment = 'Cmts'
    eco1 = 'Eco1'
    eco2 = 'Eco2'
    edge = 'Edge'   # Board outline
    margin = 'Margin'   # Edge/Board cutting margin

    def __str__(self):
        return self.value

class usage(Enum):
    signal = 'signal'
    user = 'user'

class set(object):

    def __init__(self, index, type, position, usage):
        self.index = index
        self.type = type
        self.position = position
        self.usage = usage

    def render(self):
        return "{}.{}".format(self.position, self.type)

copper_top = set(1, type.copper, position.top, usage.signal)
copper_all = set(1, type.copper, position.all, usage.signal)
copper_bottom = set(1, type.copper, position.bottom, usage.signal)

adhes_top = set(1, type.adhes, position.top, usage.user)
adhes_bottom = set(1, type.adhes, position.bottom, usage.user)

paste_top = set(1, type.paste, position.top, usage.user)
paste_bottom = set(1, type.paste, position.bottom, usage.user)

silkscreen_top = set(1, type.silkscreen, position.top, usage.user)
silkscreen_bottom = set(1, type.silkscreen, position.bottom, usage.user)

soldermask_top = set(1, type.soldermask, position.top, usage.user)
soldermask_bottom = set(1, type.soldermask, position.bottom, usage.user)

courtyard_top = set(1, type.courtyard, position.top, usage.user)
courtyard_bottom = set(1, type.courtyard, position.bottom, usage.user)

fabrication_top = set(1, type.fabrication, position.top, usage.user)
fabrication_bottom = set(1, type.fabrication, position.bottom, usage.user)

user_drawing = set(1, type.user, position.drawing, usage.user)
user_comment = set(1, type.user, position.comment, usage.user)
user_eco1 = set(1, type.user, position.eco1, usage.user)
user_eco2 = set(1, type.user, position.eco2, usage.user)
board_outline = set(1, type.cutting, position.edge, usage.user)
