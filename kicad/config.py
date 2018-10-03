"""Configuration parsing module, which generate a python namespace"""
'''
__all__ = ("Config")

from collections import Mapping, Sequence

class Config(object):
    """A dict subclass that exposes its items as attributes.

    Warning: Namespace instances do not have direct access to the
    dict methods.

    """

    def __init__(self, configFile):
        for line in open(configFile,"r"):
            parts = line.rstrip().split("=",1)
            if len(parts) > 1:
                # Strip enclosing double quotes
                if parts[1].startswith('"') and parts[1].endswith('"'):
                    parts[1] = parts[1][1:-1]

                try:
                    numVal = float(parts[1])
                    setattr(self,parts[0],numVal)
                except:
                    setattr(self,parts[0],parts[1])

    __hash__ = None

    def __eq__(self, other):
        return vars(self) == vars(other)

    def __ne__(self, other):
        return not (self == other)

    def __contains__(self, key):
        return key in self.__dict__

    def dict(self):
        return self.__dict__
'''
