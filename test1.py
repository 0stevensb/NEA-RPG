import combat

s=open("statuses.txt")
i=open("items.txt")
j=open("specials.txt")
statuses=s.readlines()
items=i.readlines()
specials=j.readlines()
stuff=statuses+items+specials
g=[]
for i in stuff:
    g.append(i.replace("\n", ""))
items=[]
statuses=[]
specials=[]
for i in range(len(stuff)):
    e=g[i-1].split(",")
    if e[-1]=="st":
        statuses.append(combat.status(e[0],e[1],e[2]))
    elif e[-1]=="i":
     items.append(combat.item(e[0],e[1],bool(e[2]),e[3]))
    elif e[-1]=="sp":
        specials.append(combat.special(e[0],e[1],e[2]))
    
for i in statuses:
    print(i.name)
for i in items:
    print(i.name)
for i in specials:
    print(i.name)