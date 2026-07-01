import combat
s=open("statuses.txt")
i=open("items.txt")
j=open("specials.txt")
k=open("skills.txt")
statuses=s.readlines()
items=i.readlines()
specials=j.readlines()
skills=k.readlines()
stuff=statuses+items+specials+skills
g=[]
for i in stuff:
    g.append(i.replace("\n", ""))
items=[]
statuses=[]
specials=[]
skills=[]
for i in range(len(stuff)):
    e=g[i].split(",")
    if e[-1]=="st":
        statuses.append(combat.status(e[0],int(e[1]),e[2]))
    elif e[-1]=="i":
     items.append(combat.item(int(e[0]),e[1],bool(e[2]),e[3]))
    elif e[-1]=="sp":
        specials.append(combat.special(e[0],int(e[1]),e[2]))
for i in range(len(stuff)):
    e=g[i].split(",")
    if e[-1]=="w":
        weaponspecialnums=e[9].split("/")
        weaponspecials=[]
        for i in weaponspecialnums:
            i=i.replace("[", "")
            i=i.replace("]", "")
            if i!="":
                weaponspecials.append(specials[int(i)])
        items.append(combat.weapon(int(e[0]),int(e[1]),bool(e[2]),int(e[3]),int(e[4]),int(e[5]),int(e[6]),int(e[7]),int(e[8]),weaponspecials,e[10],int(e[11])))
    elif e[-1]=="a":
        weaponspecialnums=e[9].split("/")
        weaponspecials=[]
        for i in weaponspecialnums:
            i=i.replace("[", "")
            i=i.replace("]", "")
            if i!="":
                weaponspecials.append(specials[int(i)])
        items.append(combat.armour(int(e[0]),int(e[1]),bool(e[2]),int(e[3]),int(e[4]),int(e[5]),int(e[6]),int(e[7]),int(e[8]),weaponspecials,e[10],e[11]))#
    elif e[-1]=="sk":
        if int(e[2])==0:
            weaponspecialnums=e[9].split("/")
            weaponspecials=[]
            for i in weaponspecialnums:
                i=i.replace("[", "")
                i=i.replace("]", "")
                if i!="":
                    weaponspecials.append(specials[int(i)])
            skills.append(combat.atkskill(e[0],int(e[1]),int(e[2]),int(e[3]),int(e[4]),int(e[5]),e[6],int(e[7]),int(e[8]),weaponspecials,int(e[10]),int(e[11])))
print("Statuses: ")
for i in statuses:
    print(f"{i.ID}: {i.name}")
print("Items: ")
for i in items:
    print(f"{i.id}: {i.name}")
    try:
        for i in i.special:
            print(i.name)
    except:
        pass
print("Specials: ")
for i in specials:
    print(f"{i.ID}: {i.name}")
print("Skills: ")
for i in skills:
    print(f"{i.ID}: {i.name}")