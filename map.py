import pygame
import combat
import copy
class tile():
    def __init__(self,id,name,y,x,passable,image,colour):
        self.ID=id
        self.name=name
        self.x,self.y=x,y
        self.passable=passable
        self.image=image
        self.colour=colour
class enemy():
    def __init__(self,x,y,ID,image,type,level,enemies):
        self.x,self.y=x,y
        self.ID=ID
        self.image=image
        self.type=type
        self.level=level
        self.enemies=enemies
        self.movecd=0
class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,a):
        self.queue.append(a)
    def dequeue(self):
        if self.empty():
            return "Empty"
        else:
            return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def empty(self):
        return len(self.queue)==0
    def length(self):
        return len(self.queue)
class graph:
    def __init__(self):
        self.graph={}
    def addnode(self,node,adjacent):
        self.graph.update({node:adjacent})
    def bfs(self,root,targetnode):
        visited={}
        for i in self.graph:
            visited.update({i:i==root})
        q=queue()
        q.enqueue(root)
        parentmap={}
        while q.queue:
            currentnode=q.dequeue()
            if (currentnode)==(targetnode):
                return self.pathreconstruct(parentmap,targetnode,root)
            for i in self.graph[currentnode]:
                if not visited[i]:
                    q.enqueue(i)
                    visited[i]=True
                    parentmap.update({i:currentnode})
        return[]
    def pathreconstruct(self,parentmap,targetnode,root):
        currentnode=targetnode
        path=[]
        while currentnode != root:
            path.append(currentnode)
            currentnode=parentmap[currentnode]
        path.reverse()
        return path

def mapgraph(map,rows,cols):
   currentmap=graph()
   for i in map:
      for j in i:
         touching=[]
         if j.x+1<=cols-1:
            if map[j.y][j.x+1].passable:
               touching.append(map[j.y][j.x+1])
         if j.x-1>=0:
            if map[j.y][j.x-1].passable:
               touching.append(map[j.y][j.x-1])
         if j.y+1<=rows-1:
            if map[j.y+1][j.x].passable:
               touching.append(map[j.y+1][j.x])
         if j.y-1>=0:
            if map[j.y-1][j.x].passable:
               touching.append(map[j.y-1][j.x])
         currentmap.addnode(j,touching)
   return currentmap
tiles ={"g":"grass", "t":"tree","r":"rock","c":"chest","rd":"road","s":"shop"}
darkgreen=(49, 107, 20)
grey=(84, 83, 84)
grassimage=pygame.image.load('grass.jpg')
rockimage=pygame.image.load('rock.jpeg')
treeimage=pygame.image.load('trees.jpg')
chestimage=pygame.image.load('chest.jpg')
roadimage=pygame.image.load('road.jpg')
jeffimage=pygame.image.load('enemy.png')
shopimage=pygame.image.load("shop.png")
enemyimages={"jeff":jeffimage}
tileimages={"g":grassimage,"t":treeimage,"r":rockimage,"c":chestimage,"rd":roadimage,"s":shopimage}
tilebg={"g":darkgreen,"rd":grey}
maps=open("maps.txt","r")
mapdests=open("mapdests.txt","r")
mapscontent=maps.readlines()
mapdestscontent=mapdests.readlines()
mapenemies=open("mapenemies.txt","r")
mapenemiescontent=mapenemies.readlines()
passable=["g","rd","c"]
def openmap(mapscontent,mapID,px,py):
    cmap=mapscontent[mapID].split("^")
    
    rows=len(cmap)
    for i in range(len(cmap)):
       cmap[i]=cmap[i].split(",")
    cols=len(cmap[0])
    cid=0
    for i in range(rows):
       cmap[i] = [x.replace('"', '') for x in cmap[i]]
       cmap[i] = [x.replace(']', '') for x in cmap[i]]
       cmap[i] = [x.replace('[', '') for x in cmap[i]]
       cmap[i] = [x.replace(' ', '') for x in cmap[i]]
       cmap[i] = [x.replace('\n', '') for x in cmap[i]]
       for j in range(cols):
             if cmap[i][j] in tilebg:
              cmap[i][j]=tile(cid,tiles[(cmap[i][j])],i,j,cmap[i][j] in passable,tileimages[(cmap[i][j])],tilebg[cmap[i][j]])
             else:
                 cmap[i][j]=tile(cid,tiles[(cmap[i][j])],i,j,cmap[i][j] in passable,tileimages[(cmap[i][j])],0)
             cid+=1
    cmapenemies=mapenemiescontent[mapID].split("^")
    for i in range(len(cmapenemies)):
       cmapenemies[i]=cmapenemies[i].split(",")
    enemies=[]
    
    for i in range(len(cmapenemies)):
       cmapenemies[i] = [x.replace('"', '') for x in cmapenemies[i]]
       cmapenemies[i] = [x.replace(']', '') for x in cmapenemies[i]]
       cmapenemies[i] = [x.replace('[', '') for x in cmapenemies[i]]
       cmapenemies[i] = [x.replace(' ', '') for x in cmapenemies[i]]
       cmapenemies[i] = [x.replace('\n', '') for x in cmapenemies[i]]
    if len(cmapenemies[0])!=1:
      for i in cmapenemies:
         enemies.append(enemy(int(i[0]),int(i[1]),int(i[2]),enemyimages[i[3]],i[3],int(i[4]),[]))
    for i in enemies:
       if i.type=="jeff":
          i.enemies =[copy.deepcopy(combat.slime),copy.deepcopy(combat.cleric),copy.deepcopy(combat.skeleton)]
    cmapgraph=mapgraph(cmap,rows,cols)
    return cmap,rows,cols,px,py,enemies,cmapgraph