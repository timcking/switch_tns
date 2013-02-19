from PythonCard import model
from configobj import ConfigObj
import re

class Switcher(model.Background):

    def on_initialize(self, event):
        # Get config for last server
        serv_config = ConfigObj('switch_tns.ini')
        server_name = serv_config['Settings']['server']

        self.components.txtStatus.text = 'Current environment is ' + server_name

        if server_name == 'rocky':
            self.components.radEnv.selection = 0
        else:
            self.components.radEnv.selection = 1

    def replace_text(self, replace_string):

        # Get config
        config = ConfigObj('switch_tns.ini')
        the_file = config['Settings']['tnsfile']

        # Read the file
        tns_file = open(the_file, 'r')
        the_text = tns_file.read()
        tns_file.close()

                # Replace
        match_str = re.compile('HOST = \S*.\)')
        the_text = match_str.sub('HOST = ' + replace_string + ')', the_text)

        # Write the file
        tns_file = open(the_file, 'w')
        tns_file.write(the_text)
        tns_file.close()

        # Write the config file
        config['Settings']['server'] = replace_string
        config.write()

    # UI Stuff
    def on_radEnv_select(self, event):
        if self.components.radEnv.selection == 0:
            replace_string = 'rocky'
            self.components.txtStatus.text = 'Current environment is rocky'
        elif self.components.radEnv.selection == 1:
            replace_string = 'xps'
            self.components.txtStatus.text = 'Current environment is xps'

        Switcher.replace_text(self, replace_string)

if __name__ == '__main__':
    app = model.Application(Switcher)
    app.MainLoop()
