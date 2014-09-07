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
    
def read(file):
    if not os.path.exists(file):
        return
    f = open(file, "rb")    # Mode includes binary (b) for safe handling on Windows OS
    s = f.read()
    f.close()
    settings = {}
    done = False
    pos = -1
    newline = -1
    while not done:
        pos = s.find("=", pos + 1)
        if pos == -1:
            done = True
            continue
        newline = s.rfind("\n", newline + 1, pos)
        if newline == -1:
            pos = s.find("\n", pos)
            newline = pos
            continue
        setting = s[newline + 1:pos].strip()
        nextpos = s.find("=", pos + 1)
        valend = s.rfind("\n", pos, nextpos)
        if valend == -1:
            nextpos = s.find("=", nextpos + 1)
            valend = s.rfind("\n", pos, nextpos)                
        value = remove_comments(s[pos + 1:valend].strip())
        settings[setting] = value
    return settings

def remove_comments(value):
    res = value
    done = False
    pos = value.find("#")
    if pos > -1 and pos < len(value) - 1:
        while not done:
            b = value[pos - 1]
            a = value[pos + 1]
            if ((b == " " or b == "\n") and a == " ") or (a == "\n" and b == "\n"):
                end_of_comment = value.find("\n", pos)
                if end_of_comment == -1:
                    end_of_comment = len(value)
                comment = value[pos:end_of_comment]
                value = value.replace(comment, "").strip()
            pos = value.find("#", pos + 1)
            if pos == -1:
                done = True
        res = value
    return res