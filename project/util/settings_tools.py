# coding=UTF8
import os

def append(file, setting, value, type):
    if not os.path.exists(file):
        return
    if type not in ("t","tt","d","dd","l","ll","b","i","s"):
        return
    f = open(file, "a")
    entry = ""
    tab = "    "
    if type == "s":
        entry = "%s = '%s'\n" % (setting, value)
    if type == "i":
        entry = "%s = %s\n" % (setting, value)
    if type == "b":
        entry = "%s = %s\n" % (setting, value)
    if type == "l":
        entry = "%s = [\n" % (setting)
        for val in value:
            entry = "%s%s'%s',\n" % (entry, tab, val)
        entry = entry + "]\n"        
    if type == "ll":
        entry = "%s = [\n" % (setting)
        for lis in value:
            entry = "%s%s%s,\n" % (entry, tab, lis)
        entry = entry + "]\n"        
    if type == "t":
        entry = "%s = (\n" % (setting)
        for val in value:
            entry = "%s%s'%s',\n" % (entry, tab, val)
        entry = entry + ")\n"        
    if type == "tt":
        entry = "%s = (\n" % (setting)
        for tup in value:
            entry = "%s%s%s,\n" % (entry, tab, tup)
        entry = entry + ")\n"
    if type == "d":
        entry = "%s = {\n" % (setting)
        for key, val in value.iteritems():
            entry = "%s%s'%s': '%s',\n" % (entry, tab, key, val)
        entry = entry + "}\n"          
    if type == "dd":
        entry = "%s = {\n" % (setting)
        for out_key, out_value in value.iteritems():
            entry = "%s%s'%s': {\n" % (entry, tab, out_key)
            for in_key, in_value in out_value.iteritems():
                entry = "%s%s%s'%s': '%s',\n" % (entry, tab, tab, in_key, in_value)
        entry = entry + "}\n"
    f.write(entry + "\n")
    f.close()