class tile():
    def __init__(self,id,name,y,x):
        self.ID=id
        self.name=name
        self.x,self.y=x,y
tiles ={"g":"grass", "t":"tree","r":"rock","c":"chest"}
maps=open("maps.txt","r")
mapscontent=maps.readlines()
cmap=mapscontent[0].split("^")
rows=len(cmap)
for i in range(len(cmap)):
   cmap[i]=cmap[i].split(",")
cols=len(cmap[0])
cid=0
playerx=0
playery=0
for i in range(rows):
   cmap[i] = [x.replace('"', '') for x in cmap[i]]
   cmap[i] = [x.replace(']', '') for x in cmap[i]]
   cmap[i] = [x.replace('[', '') for x in cmap[i]]
   cmap[i] = [x.replace(' ', '') for x in cmap[i]]
   for j in range(cols):
         cmap[i][j]=tile(cid,tiles[(cmap[i][j])],i,j)
         cid+=1

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
while True:
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
 if targetx<=cols and 0<=targetx and targety<=rows and targety>=0:

    if cmap[targety][targetx].name=="grass":
        playerx,playery=targetx,targety

