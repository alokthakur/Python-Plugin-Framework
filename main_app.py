from core.iplugin import discover_cmd_plugins
import sys, os
if __name__ == "__main__":
    base_dir = os.getcwd()
    cmd_plugins_dir = os.path.join(base_dir + '/plugins/cmd')
    print cmd_plugins_dir
    plugins = discover_cmd_plugins(cmd_plugins_dir)
    plugins = [x() for x in plugins]
    for plugin in plugins:
        os.system(plugin.cmd)
