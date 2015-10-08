import os
import imp

class IPluginRegistry(type):
    def __init__(cls, name, bases, dict):
        pass
class IPlugin(object):
    __metaclass__ = IPluginRegistry
    def __init__():
        print "in Iplugin"

class CommandPluginRegistry(IPluginRegistry):
    cmd_plugins = []
    def __init__(cls, name, bases, dict):
        if name != "CommandPlugin":
            CommandPluginRegistry.cmd_plugins.append(cls)
            print cls
            print name

class CommandPlugin(IPlugin):
    __metaclass__ = CommandPluginRegistry
    def __init__():
        print "in command plugin"
    def execute(self, cmd):
        return None
    def format(self, result):
        return None

def discover_cmd_plugins(dir):
    for file in os.listdir(dir):
        filename, ext = os.path.splitext(file)
        if ext == '.py':
            file_ob, pathname, description = imp.find_module(filename, [dir])
            mod = imp.load_module(filename, file_ob, pathname, description)
    return CommandPluginRegistry.cmd_plugins
