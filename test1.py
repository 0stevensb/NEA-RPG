import combat
s=open("statuses.txt")
i=open("items.txt")
j=open("specials.txt")
k=open("skills.txt")
r=open("enemies.txt")
p=open("units.txt")
statuses=s.readlines()
items=i.readlines()
specials=j.readlines()
skills=k.readlines()
enemies=r.readlines()
units=p.readlines()
stuff=statuses+items+specials+skills+enemies+units
g=[]
for i in stuff:
    g.append(i.replace("\n", ""))
items=[]
statuses=[]
specials=[]
skills=[]
enemies=[]
units=[]
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
        else:
            skills.append(combat.skill(e[0],int(e[1]),int(e[2]),e[3],int(e[4]),int(e[5]),int(e[6])))
for i in range(len(stuff)):
    e=g[i].split(",")
    if e[-1]=="e":
        weaponspecialnums=e[10].split("/")
        weaponspecials=[]
        for i in weaponspecialnums:
            i=i.replace("[", "")
            i=i.replace("]", "")
            if i!="":
                weaponspecials.append(specials[int(i)])
        enemyskillsnums=e[11].split("/")
        enemyskills=[]
        for i in enemyskillsnums:
            i=i.replace("[", "")
            i=i.replace("]", "")
            if i!="":
                enemyskills.append(skills[int(i)])
        enemyequipmentnums=e[12].split("/")
        enemyequipment=[]
        for i in enemyequipmentnums:
            i=i.replace("[", "")
            i=i.replace("]", "")
            if i!="":
                enemyequipment.append(items[int(i)])
        enemyequipment=combat.equipped(enemyequipment[0],enemyequipment[1],enemyequipment[2],enemyequipment[3],enemyequipment[4],enemyequipment[5])
        enemyitemdropnums=e[18].split("/")
        enemyitemdrop=[]
        for i in enemyitemdropnums:
            i=i.replace("[", "")
            i=i.replace("]", "")
            if i!="":
                enemyitemdropnums.append(items[int(i)])
        enemies.append(combat.enemy(e[0],int(e[1]),int(e[2]),int(e[3]),int(e[4]),int(e[5]),int(e[6]),int(e[7]),int(e[8]),int(e[9]),weaponspecials,enemyskills,enemyequipment,int(e[13]),bool(e[14]),bool(e[15]),int(e[16]),int(e[17]),enemyequipmentnums))
    elif e[-1]=="pm":
        weaponspecialnums=e[10].split("/")
        weaponspecials=[]
        for i in weaponspecialnums:
            i=i.replace("[", "")
            i=i.replace("]", "")
            if i!="":
                weaponspecials.append(specials[int(i)])
        enemyskillsnums=e[11].split("/")
        enemyskills=[]
        for i in enemyskillsnums:
            i=i.replace("[", "")
            i=i.replace("]", "")
            if i!="":
                enemyskills.append(skills[int(i)])
        enemyequipmentnums=e[13].split("/")
        enemyequipment=[]
        for i in enemyequipmentnums:
            i=i.replace("[", "")
            i=i.replace("]", "")
            if i!="":
                enemyequipment.append(items[int(i)])
        enemyequipment=combat.equipped(enemyequipment[0],enemyequipment[1],enemyequipment[2],enemyequipment[3],enemyequipment[4],enemyequipment[5])
        units.append(combat.enemy(e[0],int(e[1]),int(e[2]),int(e[3]),int(e[4]),int(e[5]),int(e[6]),int(e[7]),int(e[8]),int(e[9]),weaponspecials,enemyskills,enemyequipment,int(e[13]),bool(e[14]),bool(e[15]),int(e[16]),int(e[17]),enemyequipmentnums))
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
print("Enemies:")
for i in enemies:
    print(f"{i.id}: {i.name}")