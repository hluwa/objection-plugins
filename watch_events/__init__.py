__description__ = "a simple plugin to watching view events"

from objection.utils.plugin import Plugin

s = """
rpc.exports = {
    onclick: function() {
        Java.perform(function(){
            var jclazz = Java.use("java.lang.Class");
            var jobj = Java.use("java.lang.Object");

            const func = function(listener){
                var listener_name = jclazz.getName.call(jobj.getClass.call(listener));
                send("[WatchEvent] hooking onclick: " + listener_name);
                Java.use(listener_name).onClick.overload('android.view.View').implementation = function(v){
                    send("[WatchEvent] click: " + jclazz.getName.call(jobj.getClass.call(this)));
                    return this.onClick(v);
                };
            }
            
            Java.use("android.view.View").setOnClickListener.implementation = function(listener){
                if(listener != null){
                    func(listener);
                }
                return this.setOnClickListener(listener);
            }
            

            Java.choose("android.view.View$ListenerInfo", {
                onMatch: function (instance){
                    instance = instance.mOnClickListener.value;
                    if(instance){
                        func(instance);
                    }
                },
                onComplete: function (){
                }
            })
        })
    }
}
"""


class WatchEvent(Plugin):
    """ WatchEvent is a simple plugin to watching view events"""

    def __init__(self, ns):
        """
            Creates a new instance of the plugin

            :param ns:
        """

        # plugin sources are specified, so when the plugin is loaded it will not
        # try and discover an index.js next to this file.
        self.script_src = s

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
