import pygame
import combat
import copy
class tile():
    def __init__(self,id,name,y,x,passable,image):
        self.ID=id
        self.name=name
        self.x,self.y=x,y
        self.passable=passable
        self.image=image
class graph():
   def __init__(self):
      self.vertices={}
   def addvertex(self,vertex,touching):
      self.vertices.update({vertex:touching})
        
class enemy():
    def __init__(self,x,y,ID,image,type,level,enemies):
        self.x=x
        self.y=y
        self.ID=ID
        self.image=image
        self.type=type
        self.level=level
        self.enemies=enemies
def mapgraph(map):
   currentmap=graph()
   for i in range(len(map)):
      for j in range(len(map[i])):
         touching=[]
         if map[i-1][j].passable:
            touching.append(map[i-1][j])
         if map[i-1][j-2].passable:
            touching.append(map[i-1][j-2])
         if map[i][j-1].passable:
            touching.append(map[i][j-1])
         if map[i-2][j-1].passable:
            touching.append(map[i-2][j-1])
         currentmap.addvertex(map[i][j],touching)
   return currentmap
tiles ={"g":"grass", "t":"tree","r":"rock","c":"chest","rd":"road"}
grassimage=pygame.image.load('grass.jpg')
rockimage=pygame.image.load('rock.jpeg')
treeimage=pygame.image.load('trees.jpg')
chestimage=pygame.image.load('chest.jpg')
roadimage=pygame.image.load('road.jpg')
jeffimage=pygame.image.load('enemy.png')
enemyimages={"jeff":jeffimage}
tileimages={"g":grassimage,"t":treeimage,"r":rockimage,"c":chestimage,"rd":roadimage}
maps=open("maps.txt","r")
mapdests=open("mapdests.txt","r")
mapscontent=maps.readlines()
mapdestscontent=mapdests.readlines()
mapenemies=open("mapenemies.txt","r")
mapenemiescontent=mapenemies.readlines()
passable=["g","rd"]
def openmap(mapscontent,mapID,px,py):
    cmap=mapscontent[mapID].split("^")
    
    rows=len(cmap)
    for i in range(len(cmap)):
       cmap[i]=cmap[i].split(",")
    cols=len(cmap[0])
    cid=0
    playerx,playery=px,py
    for i in range(rows):
       cmap[i] = [x.replace('"', '') for x in cmap[i]]
       cmap[i] = [x.replace(']', '') for x in cmap[i]]
       cmap[i] = [x.replace('[', '') for x in cmap[i]]
       cmap[i] = [x.replace(' ', '') for x in cmap[i]]
       cmap[i] = [x.replace('\n', '') for x in cmap[i]]
       for j in range(cols):
             if cmap[i][j] in passable:
                cpass=True
             else:
                cpass=False
             cmap[i][j]=tile(cid,tiles[(cmap[i][j])],i,j,cpass,tileimages[(cmap[i][j])])
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
          i.enemies =[copy.deepcopy(combat.slime),copy.deepcopy(combat.healer),copy.deepcopy(combat.skeleton)]
    cmapgraph=mapgraph(cmap)
    return cmap,rows,cols,playerx,playery,enemies,cmapgraph