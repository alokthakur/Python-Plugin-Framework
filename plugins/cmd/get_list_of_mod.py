from core.iplugin import CommandPlugin
import os

class GetModuleList(CommandPlugin):
    def __init__(self):
        print " in GetModule list"
    cmd = "lsmod"

    def execute(self, cmd):
        if(cmd):
            os.system(cmd)
        return "done"
    def format(self, result):
        return result
    def filter(self):
        return True
