import pygame 
import random
import sys
import combat
from pygame.locals import *
pygame.init()
running=True
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
grey=(120, 126, 135)
purple=(93, 25, 133)
white=(255,255,255)
pygame.font.init() 
my_font = pygame.font.SysFont("Roboto", 30)
class button():
    def __init__(self,ID,x,y,width,height,text):
        self.colour=blue
        self.ID=ID
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
        self.cooldown=0
class bar():
    def __init__(self,ID,x,y,width,height,max,current,colour,type,unit):
        self.ID=ID
        self.x,self.y=x,y
        self.width,self.height=width,height
        self.max=max
        self.current=current
        self.colour=colour
        self.type=type
        self.unit=unit
    def draw(self,screen,screencolour):
            pygame.draw.rect(screen,grey,(self.x,self.y,self.width,self.height))
            pygame.draw.rect(screen,self.colour,(self.x,self.y,(self.current/self.max)*self.width,self.height))
            text_surface = my_font.render(self.unit.name, False, white)
            if self.unit.playable:
             pygame.draw.rect(screen,screencolour,(self.x+self.width+50,self.y,100,self.height))
             text_surface = my_font.render(str(self.current), False, white)
             screen.blit(text_surface, ((self.x+(self.width)+50,self.y)))
mousepos=(0,0)
def initmenu(screen_width,screen_height):
    buttonnums=4
    buttonheight=90
    buttons=[]
    bars=[]
    for i in range(buttonnums+1):
        buttons.append(button(i,(screen_width/buttonnums)*(i-1),screen_height-buttonheight,screen_width/buttonnums,buttonheight,i))
    for i in buttons:
        if i.ID==1:
            i.text="Attack"
        if i.ID==2:
            i.text="Skills"
        if i.ID==3:
            i.text="Inventory"
        if i.ID==4:
            i.text="Run"
    return buttons, bars
def menu(screen,running,buttons,bars,screencolour,enemy,party,screen_width,screen_height):
    gap=120
    pygame.init()
    buttos=False
    targetselect=False
    units=party+enemy.enemies
    
    playerunits,friendlyunits,enemyunits=combat.combatinit(units)
    for i in enemyunits:
        for j in playerunits+friendlyunits:
            i.aggro.update({j:50})
    currentunitind=0
    texttimer=60
    text=""
    text2=""
    text3=""
    text4=""
    turnstart=True
    pause=False
    usedskill=False
    skillselect=False
    itemselect=False
    while running:
        if usedskill and texttimer==1:
            currentunitind+=1
            if currentunitind>len(units)-1:
                currentunitind=0
            usedskill=False
            turnstart=True
        currentunit=units[currentunitind]
        for x in units:
         x.setstats()
        units=combat.turnorder(units)
        move=combat.checkmove(currentunit)
        if not move:
            text=(f"{currentunit.name} couldn't move!")
            if not pause:
             texttimer=60
            pause =True
            buttos=False
        if not currentunit.defeated and move :
            
            if turnstart and currentunit.playable:
             text=f"{currentunit.name}'s turn!"
             text2=""
             text3=""
             text4=""
            if currentunit.playable:
                if  buttos and move:
                    for event in pygame.event.get():
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            for i in buttons:
                                if mousepos[0]>=i.x and mousepos[0]<= i.x+i.width and mousepos[1]>=i.y and mousepos[1]<= i.y+i.height and i.cooldown==0:
                                    i.cooldown=10
                                    if not (targetselect or skillselect or itemselect):
                                        if i.ID ==1:
                                                buttons=[]
                                                buttonheight=90
                                                targetselect=True
                                                currentskill=combat.basicatk
                                                
                                                for i in range(len(enemyunits)+1):
                                                    buttons.append(button(i,(screen_width/len(enemyunits))*(i-1),screen_height-buttonheight,screen_width/len(enemyunits),buttonheight,enemyunits[i-1].name))
                                        
                                        elif i.ID==2:
                                                buttons=[]
                                                buttonheight=90
                                                skillselect=True
                                                for i in range(len(currentunit.skills)+1):
                                                    buttons.append(button(i,(screen_width/len(currentunit.skills))*(i-1),screen_height-buttonheight,screen_width/len(currentunit.skills),buttonheight,currentunit.skills[i-1].name))
                                        elif i.ID==3:
                                            if len(combat.inventory)>0:
                                                itemselect=True
                                                buttons=[]
                                                buttonheight=90
                                                for i in range(len(combat.inventory)+1):
                                                        buttons.append(button(i,(screen_width/len(combat.inventory))*(i-1),screen_height-buttonheight,screen_width/len(combat.inventory),buttonheight,combat.inventory[i-1].name))
                                        elif i.ID==4:
                                            running=False
                                    elif targetselect:
                                        if currentskill.targets==1:
                                            if currentskill.type==0:
                                                target= enemyunits[i.ID-1]
                                                if not target.defeated:
                                                    effects,dmg,unit=combat.attack(currentunit,target,currentskill,combat.specialsassign(currentunit,combat.basicatk),units)
                                                    target.aggro[currentunit]+=currentskill.aggro
                                                    text=f"{currentunit.name} attacked {target.name}!"
                                                    text2=f"It dealt {dmg} damage!"
                                                    if len(effects)>0:
                                                        for i in effects:
                                                           
                                                            if i==2:
                                                                text3+=f"{currentunit.name}'s speed rose! "
                                                            if i==3:
                                                                text3+=f"{target.name}'s dexterity dropped! "
                                                            if i==4:
                                                                text3+=f"{currentunit.name}'s agility rose! "
                                                            if i==5:
                                                                text3+=f"{target.name} was paralysed! "
                                                            if i==6:
                                                                text3+=f"{target.name} was burned! "
                                                            if i==7:
                                                                text3+=f"{target.name} was poisoned! "
                                                            if i==8:
                                                                text3+=f"{target.name} was frozen!"
                                                            if i==3:
                                                                text3+=f"{currentunit.name} was healed!"
                                                    buttons,bars=initmenu(screen_width,screen_height)
                                                
                                                usedskill=True
                                                texttimer=60
                                                buttos=False
                                                pause=False
                                                targetselect=False
                                            elif currentskill.targets==3:
                                                target=(friendlyunits+playerunits)[i.ID-1]
                                                if currentskill==combat.heal:
                                                    healing=round(currentunit.effmag*0.5)
                                                    target.hp+=healing
                                                    if target.hp>target.maxhp:
                                                        target.hp=target.maxhp
                                                    text=f"{target.name} healed {healing} HP!"
                                                buttons,bars=initmenu(screen_width,screen_height)
                                            
                                            usedskill=True
                                            texttimer=60
                                            buttos=False
                                            pause=False
                                            targetselect=False
                                    elif skillselect:
                                        
                                        currentskill=currentunit.skills[i.ID-1]
                                        if currentunit.mp>currentskill.manacost:
                                            currentunit.mp-=currentskill.manacost
                                        targetselect=True
                                        skillselect=False
                                        buttons=[]
                                        if currentskill.targets==1:
                                            for i in range(len(enemyunits)+1):
                                                     buttons.append(button(i,(screen_width/len(enemyunits))*(i-1),screen_height-buttonheight,screen_width/len(enemyunits),buttonheight,enemyunits[i-1].name))
                                        elif currentskill.targets==3:
                                            for i in range(len(friendlyunits+playerunits)+1):
                                                     buttons.append(button(i,(screen_width/len(friendlyunits+playerunits))*(i-1),screen_height-buttonheight,screen_width/len(friendlyunits+playerunits),buttonheight,(friendlyunits+playerunits)[i-1].name))
                                    elif itemselect:
                                        item=combat.inventory[i.ID-1]
                                        attack=False
                                        if item==combat.healthpotion:
                                            currentunit.hp+=30
                                            if currentunit.hp>currentunit.maxhp:
                                                currentunit.hp=currentunit.maxhp
                                            combat.inventory.remove(item)
                                        elif item==combat.bomb:
                                            currentskill=combat.bombthrow
                                            attack=True
                                            combat.inventory.remove(item)
                                        if  attack:
                                            targetselect=True
                                            itemselect=False
                                            for i in range(len(enemyunits)+1):
                                                    buttons.append(button(i,(screen_width/len(enemyunits))*(i-1),screen_height-buttonheight,screen_width/len(enemyunits),buttonheight,enemyunits[i-1].name))
                                        else:
                                            usedskill=True
                                            texttimer=60
                                            buttos=False
                                            pause=False
                                            itemselect=False
                                            buttons,bars=initmenu(screen_width,screen_height)
            else:
                pygame.event.get()
                if not pause:
                    texttimer=60
                    skill = combat.aiturn(currentunit,playerunits,friendlyunits,enemyunits)
                    target=combat.aitarget(currentunit,playerunits,friendlyunits,enemyunits,skill)
                    text=f"{currentunit.name} used {skill.name}!"
                    text2="It targeted "
                    for i in range(len(target)):
                        text2+=target[i].name
                        if i<len(target)-1:
                            text2+=", "
                    if skill.type==0:
                        totaleffects=[]
                        text3="It dealt "
                        for ctarget in target:
                            effects,dmg,unit=combat.attack(currentunit,ctarget,skill,combat.specialsassign(currentunit,skill),units)
                            missed=False
                            for i in effects:
                                if i==0:
                                    missed=True
                            if not missed:
                             text3+=str(dmg)+" "
                            else:
                                text3+="miss"+" "
                            totaleffects.append((ctarget,effects,unit))
                        text3+="damage!"
                        if len(totaleffects)>0:
                            for i in totaleffects:
                                if i[1]==2:
                                    text4+=f"{unit.name}'s speed rose! "
                                if i[1]==3:
                                    text4+=f"{i[0].name}'s dexterity dropped! "
                                if i[1]==4:
                                    text4+=f"{unit.name}'s agility rose! "
                                if i[1]==5:
                                    text4+=f"{i[0].name} was paralysed! "
                                if i[1]==6:
                                    text4+=f"{i[0].name} was burned! "
                                if i[1]==7:
                                    text4+=f"{i[0].name} was poisoned! "
                                if i[1]==8:
                                    text4+=f"{i[0].name} was frozen!"
                                if i[1]==3:
                                    text4+=f"{unit.name} was healed!"


                    pause =True
                    buttos=False
                if texttimer==0:
                    currentunitind+=1
                    if currentunitind>len(units)-1:
                        currentunitind=0
                    texttimer=60
                    buttos=False
                    turnstart=True
                    pause=False
        else :   
            currentunitind+=1
            pause=False
            if currentunitind>len(units)-1:
                currentunitind=0
        
        mousepos=pygame.mouse.get_pos()
        screen.fill(screencolour)
        count=0
        bars=[]
        for i in playerunits+friendlyunits:
            bars.append(bar(count,10,(count*gap)+10,100,15,i.maxhp,i.hp,red,"hp",i))
            bars.append(bar(count,10,(count*gap)+30,100,15,i.maxmp,i.mp,blue,"mp",i))
            count+=1
        count=0
        for i in enemyunits:
            bars.append(bar(len(playerunits+friendlyunits)+count,screen_width-110,(count*gap)+10,100,15,i.maxhp,i.hp,red,"hp",i))
            bars.append(bar(len(playerunits+friendlyunits)+count,screen_width-110,(count*gap)+30,100,15,i.maxmp,i.mp,blue,"mp",i))
            count+=1

        if buttos:
            for i in buttons:
                if mousepos[0]>=i.x and mousepos[0]<= i.x+i.width and mousepos[1]>=i.y and mousepos[1]<= i.y+i.height:
                    i.colour=red
                else:
                    i.colour=blue
                pygame.draw.rect(screen, i.colour, (i.x,i.y,i.width,i.height), 100,)
                text_surface = my_font.render(str(i.text), False, (0, 0, 0))
                screen.blit(text_surface, (i.x,i.y))
                
        if not buttos:
            pygame.draw.rect(screen,blue,(0,screen_height-90,screen_width,90))
            text_surface = my_font.render(text, False, (0, 0, 0))
            screen.blit(text_surface, (10,screen_height-80))
            text_surface = my_font.render(text2, False, (0, 0, 0))
            screen.blit(text_surface, (10,screen_height-60))
            text_surface = my_font.render(text3, False, (0, 0, 0))
            screen.blit(text_surface, (10,screen_height-40))
            text_surface = my_font.render(text4, False, (0, 0, 0))
            screen.blit(text_surface, (10,screen_height-20))
        for i in bars:
            i.draw(screen,screencolour)
        count=0
        for i in playerunits+friendlyunits:
            if i==currentunit:
                text_surface = my_font.render(f"{i.name}   lvl {i.level}", False, green)
            else:
                text_surface = my_font.render(f"{i.name}   lvl {i.level}", False, white)
            screen.blit(text_surface, (10,(count*gap)+50))
            count+=1
        count=0
        for i in enemyunits:
            text_surface = my_font.render(f"lvl {i.level}     {i.name}", False, red)
            screen.blit(text_surface, (screen_width-150,(count*gap)+50))
            target=playerunits[0]
            for j in playerunits+friendlyunits:
                if i.aggro[j]>i.aggro[target]:
                    target=j
            text_surface = my_font.render(target.name, False, red)
            screen.blit(text_surface, (screen_width-110,(count*gap)+80))
                
            count+=1

        for i in buttons:
            if i.cooldown>0:
                i.cooldown-=1
        if texttimer>0:
            texttimer-=1
        else:
            turnstart=False
        if texttimer==1: 
         if currentunit.playable:
            buttos=True
        for i in units:
         combat.statuscheck(i)
        combat.hpcheck(units)
        alive=[]
        for i in enemyunits:
            if not i.defeated:
                alive.append(i)
        if len(alive)==0:
            running=False
        pygame.display.flip()
        pygame.time.Clock().tick(30)
        
    