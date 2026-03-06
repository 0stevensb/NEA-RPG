import random
class unit():
    def __init__(self,name,maxhp,maxmp,attack,defence,speed,magic,dex,agility,abilities,skills,equipped,level,playable,friendly,status):
      self.name=name
      self.maxhp=maxhp
      self.hp=self.maxhp
      self.maxmp=maxmp
      self.mp=self.maxmp
      self.baseattack=attack
      self.basedefence=defence
      self.basespeed=speed
      self.basemagic=magic
      self.basedex=dex
      self.baseagility=agility
      self.abilities=abilities
      self.skills=skills
      self.abilities=abilities
      self.equipped=equipped
      self.playable=playable
      self.level=level
      self.friendly=friendly
      self.status=0
      self.atkbst=0
      self.defbst=0
      self.spdbst=0
      self.magbst=0
      self.agilitybst=0
      self.dexbst=0
      self.status=0
    def setstats(self):
       self.effattack=(self.baseattack+self.equipped.totalatk)*(1+self.atkbst*0.25)
       self.effdefence=self.basedefence+self.equipped.totaldef*(1+self.defbst*0.25)
       self.effspeed=self.basespeed+self.equipped.totalspd*(1+self.spdbst*0.25)
       if self.status.ID==1:
          self.effspeed/=2
       self.effmag=self.basemagic+self.equipped.totalmag*(1+self.magbst*0.25)
       self.effdex=self.basedex+self.equipped.totaldex*(1+self.dexbst*0.25)
       self.effagility=self.baseagility+self.equipped.totalagility*(1+self.agilitybst*0.25)
class partymember(unit):
   def __init__(self, name, maxhp, maxmp, attack, defence, speed, magic, dex,agility,abilities, skills, equipped,level,xp,playable,friendly,status):
      super().__init__(name, maxhp, maxmp, attack, defence, speed, magic, dex, agility, abilities, skills, equipped, playable, level, friendly,status)
      self.xp=xp
class enemy(unit):
   def __init__(self, name, maxhp, maxmp, attack, defence, speed, magic, dex, agility, abilities, skills, equipped, level, playable, friendly,xpdrop,goldrop,itemdrop,status):
      super().__init__(name, maxhp, maxmp, attack, defence, speed, magic, dex, agility, abilities, skills, equipped, level, playable, friendly,status)
      self.xpdrop=xpdrop
      self.goldrop=goldrop
      self.itemdrop=itemdrop
class equipped():
    def __init__(self,weapon,head,legs,body,feet,arms):
       self.weapon=weapon
       self.head=head
       self.legs=legs
       self.body=body
       self.feet=feet
       self.arms=arms
       self.totalatk=self.weapon.attack+self.head.attack+self.legs.attack+self.body.attack+self.feet.attack+self.arms.attack
       self.totaldef=self.weapon.defence+self.head.defence+self.legs.defence+self.body.defence+self.feet.defence+self.arms.defence
       self.totalspd=self.weapon.speed+self.head.speed+self.legs.speed+self.body.speed+self.feet.speed+self.arms.speed
       self.totalmag=self.weapon.magic+self.head.magic+self.legs.magic+self.body.magic+self.feet.magic+self.arms.magic
       self.totaldex=self.weapon.dex+self.head.dex+self.legs.dex+self.body.dex+self.feet.dex+self.arms.dex
       self.totalagility=self.weapon.agility+self.head.agility+self.legs.agility+self.body.agility+self.feet.agility+self.arms.agility

class item():
   def __init__(self,price,sellable,name):
      self.price=price
      self.sellable=sellable
      self.name=name
class armour(item):
   def __init__(self, price, sellable,defence,attack,speed,magic,dex,agility,special,slot,name):
      super().__init__(price, sellable,name)
      self.defence=defence
      self.attack=attack
      self.speed=speed
      self.magic=magic
      self.agility=agility
      self.dex=dex
      self.special=special
      self.slot=slot
class weapon(item):
   def __init__(self, price, sellable,defence,attack,speed,dex,agility,magic,special,name,damagetype):
      super().__init__(price, sellable,name)
      self.defence=defence
      self.attack=attack
      self.speed=speed
      self.magic=magic
      self.dex=dex
      self.agility=agility
      self.special=special
      self.damagetype=damagetype
class ability():
   def __init__(self,name,ID):
      self.name=name
      self.ID=ID
class skill():
   def __init__(self,name,ID,type,desc,manacost,targets):
      self.name = name
      self.ID=ID
      self.type=type
      self.desc=desc
      self.manacost=manacost
      self.targets=targets
class atkskill(skill):
   def   __init__(self, name, ID, type,power,atktype,dmgtype,desc,manacost,targets,special,acc):
      super().__init__(name, ID, type,desc,manacost,targets)
      self.power=power
      self.atktype =atktype
      self.dmgtype=dmgtype
      self.special=special
      self.accuracy=acc
class special():
   def __init__(self,name,ID):
      self.name=name
      self.ID=ID
class status():
   def __init__(self,name,ID):
      self.name=name
      self.ID=ID
def specialsassign(cunit,cskill):
          specials=[]
          for x in cunit.equipped.weapon.special:
             specials.append(x)
          for x in cunit.equipped.head.special:
             specials.append(x)
          for x in cunit.equipped.arms.special:
             specials.append(x)
          for x in cunit.equipped.body.special:
             specials.append(x)
          for x in cunit.equipped.legs.special:
             specials.append(x)
          for x in cunit.equipped.feet.special:
             specials.append(x)
          for x in cunit.abilities:
             specials.append(x)
          if cskill!=0:
            for x in cskill.special:
             specials.append(x)
          return specials
def turnorder(list1):
   n = len(list1)
   for i in range(n-1):
      for j in range(n-i-1):
        if list1[j].effspeed < list1[j+1].effspeed:
          list1[j], list1[j+1] = list1[j+1], list1[j]
def moveselect(cunit):
      valid=False
      choice=0
      cskill=basicatk
      while not valid:
       choice=input("Attack (1), Skills (2) ")
       if choice=="1" or choice=="2":
          if choice =="1":
             cskill=basicatk
             valid=True
          elif choice =="2":
             valid= True
             cskill=0
             while cskill==0:
               cskill=skillselect(cunit)
          if cskill.targets==1:
                tempunits=units.copy()
                tempunits.remove(cunit)
                for x in range(len(tempunits)):
                 print(f"{x+1}: {tempunits[x].name}")
                valid=False
                while not valid:
                    targetnum=int(input("Which will you target? "))-1
                    if targetnum<=len(tempunits):
                        target=tempunits[targetnum]
                        valid=True
          specials = specialsassign(cunit,cskill)
          if cskill.type==0:
            hitchance=(cunit.effdex/target.effagility)*cskill.accuracy
            if random.randint(1,100)<=hitchance or cskill.accuracy==101:
                dmg=damagecalc(cunit,cskill,target,specials,specialsassign(target,0))   
                target.hp-=dmg
                print(f"{target.name} took {dmg} damage!")
                for i in specials:
                    if i.ID==1:
                        cunit.spdbst+=1
                        print(f"{cunit.name}'s speed rose!")
                    if i.ID==2 and random.randint(1,3)==3:
                        target.dexbst-=1
                        print(f"{target.name}'s dexterity dropped!")
                    if i.ID ==3:
                       cunit.agilitybst+=1
                       print(F"{cunit.name}'s agility rose!")
                    if i.ID==5 and random.randint(1,3)==3 and target.status==0:
                       target.status=paralysis
                for i in units:
                    if i.hp <=0:
                     print(f"{i.name} was defeated!")
                     if i.playable:
                        playerunits.remove(i)
                     elif i.friendly:
                        friendlyunits.remove(i)
                     else:
                        enemyunits.remove(i)
                     units.remove(i)
            else:
                print("The attack missed!")
def skillselect(cunit):
             print("Skills:")
             for i in range(len(cunit.skills)):
                print(f"{i+1}: {cunit.skills[i].name}")
             valid=False
             while not valid:
                choice=int(input("Which skill? 0 to leave "))
                if choice <= len(cunit.skills) and choice>=0:
                   valid=True
                   if choice !=0:
                     cskill=cunit.skills[choice-1]
                     print(cskill.desc)
                     print(f"Power: {cskill.power} Mana cost: {cskill.manacost} Accuracy: {cskill.accuracy}")
                     if cunit.mp< cskill.manacost:
                        print("Insufiicent MP!")
                        moveselect(cunit)
                     else:
                        valid = False
                        while not valid:
                           choice = input("Use this skill? (y/n) ").lower()
                           if choice =="y" or choice =="n":
                              valid = True
                              if choice=="y":
                                    cunit.mp-=cskill.manacost
                                    return cskill
                              else:
                                    return 0
                   else:
                      moveselect(cunit)
def damagecalc(attacker,cskill,target,atkspecials,defspecials):
   if cskill.ID==0:
      atktype=attacker.equipped.weapon.damagetype
      dmgtype=atktype
      power=10
   else:
      atktype=cskill.atktype
      dmgtype=cskill.dmgtype
      power=cskill.power
   if atktype==1:
      atkstat=attacker.effattack
   elif atktype==2:
      atkstat=attacker.effmag
   if dmgtype==1:
      defstat=target.effdefence
   elif dmgtype==2:
      defstat=target.effmag
   dmgmult=1
   critratemult=1
   for x in atkspecials:
      if x.ID==4 and atktype==1:
        critratemult=1.5
   critrate=(attacker.effdex/2)*critratemult
   if random.randint(1,100)<=critrate:
      dmgmult*=3
      print("Critical Hit!")
   dmg=round((atkstat/defstat)*power*(random.randint(85,115))/100)*dmgmult
   return dmg
   

speedboost=special("Speed Boost",1)
dexdwn=special("Dex Down",2)
aglup=special("Agility Up",3)
physcritup=special("Crit Rate up",4) 
paralyse=special("Paralyse", 5)  

normal=status("Normal",0)
paralysis=status("Paralysed",1)

espear=weapon(0,False,0,20,0,0,0,5,[],"Thunder Spear",1)
knife=weapon(20,True,0,10,5,5,0,0,[],"Knife",1)
assassinknife=weapon(30,True,0,15,7,7,5,0,[physcritup],"Assassin Knife",1)
wand=weapon(50,True,0,5,0,0,0,20,[],"Wand",2)
gloves=armour(50,True,15,30,0,0,0,0,[],"arms","Gloves")
ironswrd=weapon(30,True,5,20,-2,0,0,0,[],"Iron Sword",1)
lthrchest=armour(25,True,25,0,0,0,0,0,[],"body","Leather Chestplate")
robe=armour(40,True,5,0,0,10,0,0,[],"body","Robe")
nothingarmour=armour(0,False,0,0,0,0,0,0,[],"any","nothing")
nothingweapon=weapon(0,False,0,0,0,0,0,0,[],"nothing",1)

basicatk=atkskill("Basic attack",0,0,10,1,1,"A basic attack",0,1,[],100)
tbolt=atkskill("Thunderbolt",1,0,20,2,2,"Attack an enemy with a bolt of lightning, dealing magic damage and a chance to paralyse",10,1,[paralyse],90)
spdyslsh=atkskill("Speedy Slash",2,0,8,1,1,"Strike an enemy quickly, raising the user's speed stat",15,1,[speedboost],100)
wildstrike=atkskill("Wild Strike",3,0,30,1,1,"A powerful but inaccurate physical attack",5,1,[],60)
darkspike=atkskill("Dark Spike",4,0,15,2,1,"Attack a target with spikes of darkness. A magical attack that deals physical damage",7,1,[],95)
darkblast=atkskill("Dark Blast",5,0,20,2,2,"Launch a collection of dark energy at the target. Chance to reduce dexterity",10,1,[dexdwn],90)
sneakystrike=atkskill("Sneaky Strike",6,0,9,1,1,"Attack the target from the shadows, raising agility and never missing",5,1,[aglup],101)

cass=partymember("Cass",50,30,50,40,40,30,30,30,[],[tbolt,spdyslsh,wildstrike],equipped(espear,nothingarmour,nothingarmour,lthrchest,nothingarmour,gloves),10,0,True,True)
aster=partymember("Aster",30,25,30,20,35,40,50,50,[],[spdyslsh,darkspike,darkblast,sneakystrike],equipped(assassinknife,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),10,0,True,True)
elphis=partymember("Elphis",25,50,15,15,25,50,20,20,[],[tbolt],equipped(wand,nothingarmour,nothingarmour,robe,nothingarmour,nothingarmour),10,0,True,True)

slime=enemy("Slime",50,10,20,50,20,15,10,10,[],[],equipped(nothingweapon,nothingarmour,nothingarmour,nothingarmour,nothingarmour,nothingarmour),5,False,False,10,10,[])
skeleton=enemy("Skeleton",30,7,30,20,30,10,20,25,[],[],equipped(ironswrd,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),5,False,False,10,10,[])

jeff=unit("Jeff",20,10,10,10,10,5,15,15,[],[],equipped(ironswrd,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),4,False,True)

units=[cass,aster,slime,skeleton,jeff,elphis]
playerunits=[]
friendlyunits=[]
enemyunits=[]
defeated=[]
for x in units:
   if x.friendly:
      if x.playable:
         playerunits.append(x)
      else:
         friendlyunits.append(x)
   else:
      enemyunits.append(x)
while len(playerunits)>0 and len(enemyunits)>0:
   for x in units:
      x.setstats()
   turnorder(units)
   for x in units:
      if len(playerunits)>0 and len(enemyunits)>0:
         x.setstats()
         print (f"{x.name}'s turn!")
         if x.playable:
            print(f"HP: {x.hp}/{x.maxhp}")
            print(f"MP: {x.mp}/{x.maxmp}")
            moveselect(x)
         else:
            enemies=[]
            cskill=basicatk
            for i in units:
               if x.friendly:
                if not i.friendly:
                  enemies.append(i)
               else:
                  if i.friendly:
                     enemies.append(i)
            target=random.choice(enemies)
            dmg=damagecalc(x,cskill,target,specialsassign(x,cskill),specialsassign(target,0))
            target.hp-=dmg
            print(f"{target.name} took {dmg} damage!")
            for i in units:
                  if i.hp <=0:
                     print(f"{i.name} was defeated!")
                     if i.playable:
                        playerunits.remove(i)
                     elif i.friendly:
                        friendlyunits.remove(i)
                     else:
                        defeated.append(i)
                        enemyunits.remove(i)
                     units.remove(i)
      
