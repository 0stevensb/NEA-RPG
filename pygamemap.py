import pygame
import map
import random
import combatUI
import combat
import math
pygame.init()

tiles ={"g":"grass", "t":"tree","r":"rock","c":"chest","rd":"road"}

pygame.display.set_caption('Epic Adventure')
mc = pygame.image.load('mc.png')

tiletextures=[map.grassimage,map.rockimage,map.treeimage,map.chestimage,map.roadimage]

running=True
red=(255,0,0)
green=(0,255,0)
darkgreen=(49, 107, 20)
blue=(0,0,255)
grey=(89, 92, 88)
goldcolour=(251, 255, 3)
darkgrey=(51, 51, 49)
purple=(131, 23, 173)
black=(0,0,0)
onmap=True
onmenu=False
screen_width, screen_height = 750, 525
def djikstra(cmap,cmapgraph,startx,starty):
    unvisited=[]
    for i in cmapgraph.vertices:
        unvisited.append(i)
    distance={}
    for i in unvisited:
        if i.x==startx and i.y==starty:
            distance.update({i:0})
        else:
            distance.update({i:math.inf})
    currentnode=cmap[starty][startx]
    fullinf=False
    while len(unvisited)>0 and not fullinf:
        dist=math.inf
        currentnode=unvisited[0]
        for i in unvisited:
            if distance[i]<dist:
                dist=distance[i]
                currentnode=i
        
        for i in cmapgraph.vertices[currentnode]:
                f=distance[i]
                if f>distance[currentnode]+1:
                    distance.update({i:distance[currentnode]+1})
        unvisited.remove(currentnode)
        fullinf=True
        for i in unvisited:
            if i != math.inf:
                fullinf=False
    return distance
def play(mc, running, mapswitchcooldown, screen_width, screen_height,combatcooldown):
    global onmap,onmenu
    gold=0
    running=True
    if onmap:
     mapID=0
     cmap, rows, cols, playerx, playery,enemies,cmapgraph = map.openmap( map.mapscontent,mapID,1,1)
     screen=pygame.display.set_mode((screen_width,screen_height))
     height=screen_height//rows
     width=screen_width//cols
     while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                keys = pygame.key.get_pressed()
                moving=False
                if keys[pygame.K_q]:
                    running=False
                if keys[pygame.K_r]:
                    onmap=False
                    onmenu=True
                if keys[pygame.K_RIGHT]:
                    targetx,targety=playerx+1,playery
                    moving=True
                if keys[pygame.K_LEFT]:
                    targetx,targety=playerx-1,playery
                    moving=True
                if keys[pygame.K_UP]:
                    targetx,targety=playerx,playery-1
                    moving=True
                if keys[pygame.K_DOWN]:
                    targetx,targety=playerx,playery+1
                    moving=True
            if moving:
                
                if targetx<=cols-1 and 0<=targetx and targety<=rows-1 and targety>=0:
                    if cmap[targety][targetx].name=="chest":
                        gold+=100
                        combat.inventory.append(combat.bomb)
                        cmap[targety][targetx]=map.tile(cmap[targety][targetx].ID,"grass",targety,targetx,True,map.grassimage)
                    if cmap[targety][targetx].passable:
                        free = True
                        
                        for j in enemies:
                            if j.x == targetx and j.y == targety and combatcooldown==0:
                                screen=pygame.display.set_mode((screen_width,screen_height))
                                buttons,bars = combatUI.initmenu(screen_width,screen_height)
                                combatcooldown=30
                                combatUI.menu(screen,running,buttons,bars,black,j,combat.units,screen_width,screen_height)
                                free=False
                                gold+=combat.battleend(combat.units,j.enemies)
                                enemies.remove(j)
                        if cmap[targety][targetx].passable and free:
                            playerx,playery=targetx,targety
                        for i in enemies:
                            dists=djikstra(cmap,cmapgraph,playerx,playery)
                            lowestdist=math.inf

                            z=cmap[i.y][i.x]
                            y=cmapgraph.vertices[z]
                            if len(y)==0:
                                y.append(cmap[i.y-1][i.x])
                            target=y[0]
                            for j in cmapgraph.vertices[z]:
                                if dists[j]<lowestdist:
                                    lowestdist=dists[j]
                                    target=j
                            enemytargetx,enemytargety=target.x,target.y
                            if enemytargetx<=cols-1 and 0<=enemytargetx and enemytargety<=rows-1 and enemytargety>=0:
                                for j in enemies:
                                    if j.x==enemytargetx and j.y==enemytargety:
                                        free=False
                                    else:
                                        free=True
                                if cmap[enemytargety][enemytargetx].passable and free and not (enemytargetx == playerx and enemytargety == playery):
                                    i.x,i.y=enemytargetx,enemytargety
                else:
                    destinations=map.mapdestscontent[mapID].split(",")
                    destinations = [x.replace('"', '') for x in destinations]
                    destinations = [x.replace(']', '') for x in destinations]
                    destinations = [x.replace('[', '') for x in destinations]
                    destinations = [x.replace(' ', '') for x in destinations]
                    destinations = [x.replace('\n', '') for x in destinations]
                    if targetx>cols-1  and mapswitchcooldown==0:
                        cmap, rows, cols, playerx, playery,enemies,cmapgraph = map.openmap( map.mapscontent,int(destinations[1])-1,0,targety)
                        mapID=int(destinations[1])-1
                        mapswitchcooldown=30
                    elif 0>targetx and mapswitchcooldown==0:
                        cmap, rows, cols, playerx, playery,enemies,cmapgraph = map.openmap(  map.mapscontent,int(destinations[3])-1,cols-1,targety)
                        mapID=int(destinations[3])-1
                        mapswitchcooldown=30
                    elif targety>rows-1 and mapswitchcooldown==0:
                        cmap, rows, cols, playerx, playery,enemies,cmapgraph = map.openmap(  map.mapscontent,int(destinations[2])-1,targetx,0) 
                        mapID=int(destinations[2])-1
                        mapswitchcooldown=30
                    elif 0>targety and mapswitchcooldown==0:
                        cmap, rows, cols, playerx, playery,enemies,cmapgraph = map.openmap( map.mapscontent,int(destinations[0])-1,targetx,rows-1) 
                        mapID=int(destinations[0])-1
                        mapswitchcooldown=30

            for i in cmap:
                for j in i:
                    screen.blit(j.image,(((j.x)*width),(j.y)*height))
                    if j.x==playerx and j.y==playery:
                        screen.blit(mc, (int((j.x)*width + width//3), int((j.y)*height)))
                    for k in enemies:
                        if j.x==k.x and j.y==k.y:
                            screen.blit(k.image,(((j.x)*width)+width/3,(j.y)*height))
            text_surface = combatUI.my_font.render(str(gold), False, goldcolour)
            screen.blit(text_surface, (10,10))
            
            if mapswitchcooldown>0:
                mapswitchcooldown-=1
            if combatcooldown>0:
                combatcooldown-=1
            pygame.display.flip()
            pygame.time.Clock().tick(30)
    elif onmenu:
        screen=pygame.display.set_mode((screen_width,screen_height))
        buttons,bars = combatUI.initmenu(screen_width,screen_height)
play(mc, running, 0, screen_width, screen_height,0)