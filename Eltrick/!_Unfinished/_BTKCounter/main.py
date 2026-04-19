bomblist = []
with open("bomb.txt") as f:
    bomblist = f.readlines()

with open("spevil.txt") as g:
    spevil = g.readlines()
    t = 0
    for c in spevil:
        if c in bomblist:
            if c == "UltraStores":
                t += 4
            elif c == "Simon Stores":
                t += 1
            print(c.strip())
            t += 1
    print(f"Total Spevil Score: {t}\n")

t = 0
for c in bomblist:
    if "Forget" in c:
        if c == "Forget Them All":
            t += 4
        elif c == "Forget Me Now":
            t += 1
        print(c.strip())
        t += 1
print(f"Total Forget Score: {t}\n")

with open("3stage.txt") as g:
    tristage = g.readlines()
    t = 0
    for c in tristage:
        if c in bomblist:
            print(c.strip())
            t += 1
    print(f"Total 3-stage Score: {t}\n")

with open("kritzy.txt") as g:
    kritzy = g.readlines()
    t = 0
    for c in kritzy:
        if c in bomblist:
            print(c.strip())
            t += 1
    print(f"Total Kritzy Score: {t}\n")

with open("rtcontrolled.txt") as g:
    rtcontrolled = g.readlines()
    t = 0
    for c in rtcontrolled:
        if c in bomblist:
            print(c.strip())
            t += 1
    print(f"Total RT-Controlled Score: {t}\n")

with open("rtsensitive.txt") as g:
    rtsensitive = g.readlines()
    t = 0
    for c in rtsensitive:
        if c in bomblist:
            print(c.strip())
            t += 1
    print(f"Total RT-Sensitive Score: {t}")

