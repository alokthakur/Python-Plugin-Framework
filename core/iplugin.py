import os
import imp

class IPluginRegistry(type):
    def __init__(cls, name, bases, dict):
        print "in iplugin registry"
class IPlugin(object):
    __metaclass__=IPluginRegistry
    def __init__():
        print "in Iplugin"

class CommandPlugin(IPlugin):
    def __init__():
        print "in command plugin"
    def execute(self, cmd):
        return None
    def format(self, result):
        return None
