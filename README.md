# objection-plugins

# usage

```
git clone https://github.com/hluwa/objection-plugins ~/.objection/plugins  --recurse-submodules
objection -g com.app.name explore -P ~/.objection/plugins
plugin wallbreaker android.content.ContextProvider
plugin ...
```

# update

```
cd ~/.objection/plugins
git pull
git submodule foreach git pull origin master
```

# Descriptions

| dir | name | author | desc |
| -- | -- | -- | -- |
| FRIDA-DEXDump | dexdump | hluwa | search and dump dex on memory |
| Wallbreaker | wallbreaker | hluwa | help to understand java memory world, eg: classdump |
| watch_events | watch_event | hluwa | trace events listener |
