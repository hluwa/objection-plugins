__description__ = "a simple plugin to watching view events"

import os

from objection.utils.plugin import Plugin


class WatchEvent(Plugin):
    """ WatchEvent is a simple plugin to watching view events"""

    def __init__(self, ns):
        """
            Creates a new instance of the plugin

            :param ns:
        """

        # plugin sources are specified, so when the plugin is loaded it will not
        # try and discover an index.js next to this file.
        self.script_path = os.path.join(os.path.dirname(__file__), "agent.js")

        # as script_src is specified, a path is not necessary. this is simply an
        # example of an alternate method to load a Frida script
        # self.script_path = os.path.join(os.path.dirname(__file__), "script.js")

        implementation = {
            'meta': 'watching view events',
            'commands': {
                'onclick': {
                    'meta': 'search all OnClickListener and hook setOnClickListener to watching onClick.',
                    'exec': self.onclick
                }
            }
        }

        super().__init__(__file__, ns, implementation)

        self.inject()

    def onclick(self, args: list):
        """
            Tests a plugin by calling an RPC export method
            called getInformation, and printing the result.

            :param args:
            :return:
        """

        v = self.api.onclick()


namespace = 'watch_event'
plugin = WatchEvent
