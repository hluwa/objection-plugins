/*
* Author: hluwa <hluwa888@gmail.com>
* HomePage: https://github.com/hluwa
* CreatedTime: 2020/3/8 22:42
* */
var jclazz = null;
var jobj = null;

function getObjClassName(obj) {
    if (!jclazz) {
        var jclazz = Java.use("java.lang.Class");
    }
    if (!jobj) {
        var jobj = Java.use("java.lang.Object");
    }
    return jclazz.getName.call(jobj.getClass.call(obj));
}

function watch(obj, mtdName) {
    var listener_name = getObjClassName(obj);
    var target = Java.use(listener_name);
    if (!target || !mtdName in target) {
        return;
    }
    // send("[WatchEvent] hooking " + mtdName + ": " + listener_name);
    target[mtdName].overloads.forEach(function (overload) {
        overload.implementation = function () {
            send("[WatchEvent] " + mtdName + ": " + getObjClassName(this));
            return this[mtdName].apply(this, arguments);
        };
    })


}


rpc.exports = {
    onclick: function () {
        Java.perform(function () {


            Java.use("android.view.View").setOnClickListener.implementation = function (listener) {
                if (listener != null) {
                    watch(listener, 'onClick');
                }
                return this.setOnClickListener(listener);
            };


            Java.choose("android.view.View$ListenerInfo", {
                onMatch: function (instance) {
                    instance = instance.mOnClickListener.value;
                    if (instance) {
                        watch(instance, 'onClick');
                    }
                },
                onComplete: function () {
                }
            })
        })
    }
};
