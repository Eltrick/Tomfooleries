import json

loop = None
missions = None
modules = None
noTP = None

name = "name"
bombs = "bombs"
pools = "pools"
modules = "modules"

# Paste the output of https://bombs.samfun.dev/json/missions in the file
with open("./missions.json", "r", encoding='utf-8', errors='ignore') as file:
    content = file.readlines()[0]
    missions = json.loads(content)

with open("./notp.txt", "r", encoding='utf-8', errors='ignore') as file:
    noTP = file.readlines()[0].split(",")

with open("./list.txt", "r", encoding='utf-8', errors='ignore') as file:
    content = file.readlines()[0]
    loop = content.split(",")

for m in missions:
    if m[name] in loop:
        notplog = []
        
        bomblist = m[bombs]
        for b in bomblist:
            poollist = b[pools]
            
            for mp in poollist:
                modlist = mp[modules]
                for mod in modlist:
                    if mod in noTP:
                        notplog.append(mod)
        if len(notplog) != 0:
            print(m[name] + ": " + "; ".join(notplog))