import combat
class thing:
    def __init__(self,q,w):
        self.text1=q
        self.text2=w

s=open("statuses.txt")
i=open("items.txt")
statuses=s.readlines()
items=i.readlines()
g=[]
for i in statuses:
    g.append(i.replace("\n", ""))
f=[]
for i in items:
    f.append(i.replace("\n", ""))
things=[]
for i in range(len(g)):
    e=g[i-1].split(",")
    things.append(combat.status(e[0],e[1],e[2]))
for i in range(len(f)):
    e=f[i-1].split(",")
    things.append(combat.item(e[0],bool(e[1]),e[2]))
for i in things:
    print(i.name)