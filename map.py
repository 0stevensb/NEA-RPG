red=(255,0,0)
green=(0,255,0)
darkgreen=(49, 107, 20)
blue=(0,0,255)
grey=(89, 92, 88)
gold=(251, 255, 3)
darkgrey=(51, 51, 49)
import pygame
class tile():
    def __init__(self,id,name,y,x,passable,colour):
        self.ID=id
        self.name=name
        self.x,self.y=x,y
        self.passable=passable
        self.colour=colour
class graph():
   def __init__(self):
      self.vertices={}
   def addvertex(self,vertex,touching):
      self.vertices.update({vertex:touching})
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
tiles ={"g":"grass", "t":"tree","r":"rock","c":"chest","e":"enemy","rd":"road"}
grassimage=pygame.image.load('grass.webp')
rockimage=pygame.image.load('rock.jpeg')
treeimage=pygame.image.load('trees.jpg')
chestimage=pygame.image.load('chest.webp')
enemyimage=pygame.image.load('enemy.jpg')
roadimage=pygame.image.load('mela.png')
tilecolours={"g":grassimage,"t":treeimage,"r":rockimage,"c":chestimage,"e":enemyimage,"rd":roadimage}
maps=open("maps.txt","r")
mapdests=open("mapdests.txt","r")
mapscontent=maps.readlines()
mapdestscontent=mapdests.readlines()
def openmap(tiles, mapscontent,mapID,px,py):
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
             if cmap[i][j]=="g"or cmap[i][j]=="rd":
                cpass=True
             else:
                cpass=False
             cmap[i][j]=tile(cid,tiles[(cmap[i][j])],i,j,cpass,tilecolours[(cmap[i][j])])
             cid+=1
    return cmap,rows,cols,playerx,playery

cmap, rows, cols, playerx, playery = openmap(tiles, mapscontent,0,1,1)

def printmap(cmap, cols, playerx, playery):
    count=0
    for i in cmap:
        for j in i:
         count+=1
         if count==cols:
            if j.x==playerx and j.y==playery:
             print("Ben")
            else:
             print(j.name)
            count=0
         else:
          if j.x==playerx and j.y==playery:
             print(f"Ben ",end="")
          else:
           print(f"{j.name} ",end="")
mapID=0
running=False
while running:
 currentmapgraph=mapgraph(cmap)
 print(mapID)
 adjacent=currentmapgraph.vertices[cmap[playery][playerx]]
 count=1
 for i in adjacent:
    if count<len(adjacent):
     print( i.name+", ",end="")
    else:
       print(i.name)
    count+=1
 printmap(cmap, cols, playerx, playery)
 move=input().lower()
 if move=="d":
    targetx,targety=playerx+1,playery
 elif move=="a":
    targetx,targety=playerx-1,playery
 elif move=="w":
    targetx,targety=playerx,playery-1
 elif move=="s":
    targetx,targety=playerx,playery+1
 print(targetx,targety)
 if targetx<=cols-1 and 0<=targetx and targety<=rows-1 and targety>=0:
    if cmap[targety][targetx].passable:
        playerx,playery=targetx,targety
 else:
  destinations=mapdestscontent[mapID].split(",")
  destinations = [x.replace('"', '') for x in destinations]
  destinations = [x.replace(']', '') for x in destinations]
  destinations = [x.replace('[', '') for x in destinations]
  destinations = [x.replace(' ', '') for x in destinations]
  destinations = [x.replace('\n', '') for x in destinations]
  if targetx>cols-1  :
   cmap, rows, cols, playerx, playery = openmap(tiles, mapscontent,int(destinations[1])-1,0,targety)
   mapID=int(destinations[1])-1
  elif 0>targetx:
     cmap, rows, cols, playerx, playery = openmap( tiles, mapscontent,int(destinations[3])-1,cols-1,targety)
     mapID=int(destinations[3])-1
  elif targety>rows-1:
    cmap, rows, cols, playerx, playery = openmap( tiles, mapscontent,int(destinations[2])-1,targetx,0) 
    mapID=int(destinations[2])-1
  elif 0>targety:
     cmap, rows, cols, playerx, playery = openmap(tiles, mapscontent,int(destinations[0])-1,targetx,rows-1) 
     mapID=int(destinations[0])-1
  print(mapID+1)