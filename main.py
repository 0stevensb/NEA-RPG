import random
class unit():
    def __init__(self,name,maxhp,maxmp,attack,defence,speed,magic,dex,agility,abilities,skills,equipped,playable,level,friendly):
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
    def setstats(self):
       self.effattack=(self.baseattack+self.equipped.totalatk)*(1+self.atkbst*0.25)
       self.effdefence=self.basedefence+self.equipped.totaldef*(1+self.defbst*0.25)
       self.effspeed=self.basespeed+self.equipped.totalspd*(1+self.spdbst*0.25)
       self.effmag=self.basemagic+self.equipped.totalmag*(1+self.magbst*0.25)
       self.effdex=self.basedex+self.equipped.totaldex*(1+self.dexbst*0.25)
       self.effagility=self.baseagility+self.equipped.totalagility*(1+self.agilitybst*0.25)
class partymember(unit):
   def __init__(self, name, maxhp, maxmp, attack, defence, speed, magic, dex,agility,abilities, skills, equipped,level,xp,playable,friendly):
      super().__init__(name, maxhp, maxmp, attack, defence, speed, magic, dex, agility, abilities, skills, equipped, playable, level, friendly)
      self.xp=xp
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
          for x in cskill.special:
             specials.append(x)
          return specials
def specialsassignnoskill(cunit):
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
          return specials
def turnorder(list1):
   n = len(list1)
   for i in range(n-1):
      for j in range(n-i-1):
        if list1[j].effspeed < list1[j+1].effspeed:
          list1[j], list1[j+1] = list1[j+1], list1[j]
def moveselect(cunit):
      valid=False
      while not valid:
       choice=input("Attack (1), Skills (2) ")
       if choice=="1" or choice=="2":
          if choice =="1":
             cskill=basicatk
             print("Attacked")
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
          for i in specials:
             if i.ID==1:
                cunit.spdbst+=1
                print("Speed went up!")
          hitchance=(cunit.effdex/target.effagility)*cskill.accuracy
          if random.randint(1,100)<=hitchance or cskill.accuracy==101:
            dmg=damagecalc(cunit,cskill,target,specials,specialsassignnoskill(target))   
            target.hp-=dmg
            print(f"{target.name} took {dmg} damage!")
            for i in units:
                  if i.hp <=0:
                     print(f"{i.name} was defeated!")
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
   dmg=round((atkstat/defstat)*power*(random.randint(85,100))/100)
   return dmg
   

      
espear=weapon(0,False,0,20,0,0,0,5,[],"Thunder Spear",1)
gloves=armour(50,True,15,30,0,0,0,0,[],"arms","Gloves")
ironswrd=weapon(30,True,5,20,-2,0,0,0,[],"Iron Sword",1)
lthrchest=armour(25,True,25,0,0,0,0,0,[],"body","Leather Chestplate")
nothingarmour=armour(0,False,0,0,0,0,0,0,[],"any","nothing")
nothingweapon=weapon(0,False,0,0,0,0,0,0,[],"nothing",1)
speedboost=special("Speed Boost",1)
tbolt=atkskill("Thunderbolt",1,0,20,2,2,"Attack an enemy with a bolt of lightning, dealing magic damage and a chance to paralyse",10,1,[],100)
spdyslsh=atkskill("Speedy Slash",2,0,10,1,1,"Strike an enemy quickly, raising the user's speed stat",15,1,[speedboost],100)
basicatk=atkskill("Basic attack",0,0,10,1,1,"",0,1,[],100)
cass=partymember("Cass",50,30,50,40,40,30,30,30,[speedboost],[tbolt,spdyslsh],equipped(espear,nothingarmour,nothingarmour,lthrchest,nothingarmour,gloves),10,0,True,True)
slime=unit("Slime",50,10,20,50,20,15,10,10,[],[],equipped(nothingweapon,nothingarmour,nothingarmour,nothingarmour,nothingarmour,nothingarmour),False,5,False)
skeleton=unit("Skeleton",30,7,30,20,30,10,20,25,[],[],equipped(ironswrd,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),False,5,False)
units=[cass,slime,skeleton]
playerunits=[cass]
friendlyunits=[]
enemyunits=[slime,skeleton]
while len(units)>len(playerunits):
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
            allies=[]
            cskill=basicatk
            for i in units:
               if i.friendly:
                  allies.append(i)
            target=random.choice(allies)
            dmg=damagecalc(x,cskill,target,specialsassign(x,cskill),specialsassignnoskill(target))
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
                        enemyunits.remove(i)
                     units.remove(i)
      


