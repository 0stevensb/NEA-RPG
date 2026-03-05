import random
class unit():
    def __init__(self,name,maxhp,maxmp,attack,defence,speed,magic,abilities,skills,equipped,playable,level):
      self.name=name
      self.maxhp=maxhp
      self.hp=self.maxhp
      self.maxmp=maxmp
      self.mp=self.maxmp
      self.baseattack=attack
      self.basedefence=defence
      self.basespeed=speed
      self.basemagic=magic
      self.abilities=abilities
      self.skills=skills
      self.abilities=abilities
      self.equipped=equipped
      self.playable=playable
      self.level=level
      self.status=0
      self.atkbst=0
      self.defbst=0
      self.spdbst=0
      self.magbst=0
    def setstats(self):
       self.effattack=(self.baseattack+self.equipped.totalatk)*(1+self.atkbst*0.25)
       self.effdefence=self.basedefence+self.equipped.totaldef*(1+self.defbst*0.25)
       self.effspeed=self.basespeed+self.equipped.totalspd*(1+self.spdbst*0.25)
       self.effmag=self.basemagic+self.equipped.totalmag*(1+self.magbst*0.25)
class partymember(unit):
   def __init__(self, name, maxhp, maxmp, attack, defence, speed, magic, abilities, skills, equipped,level,xp,playable):
      super().__init__(name, maxhp, maxmp, attack, defence, speed, magic, abilities, skills, equipped,playable,level)
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
class item():
   def __init__(self,price,sellable,name):
      self.price=price
      self.sellable=sellable
      self.name=name
class armour(item):
   def __init__(self, price, sellable,defence,attack,speed,magic,special,slot,name):
      super().__init__(price, sellable,name)
      self.defence=defence
      self.attack=attack
      self.speed=speed
      self.magic=magic
      self.special=special
      self.slot=slot
class weapon(item):
   def __init__(self, price, sellable,defence,attack,speed,magic,special,name,damagetype):
      super().__init__(price, sellable,name)
      self.defence=defence
      self.attack=attack
      self.speed=speed
      self.magic=magic
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
   def   __init__(self, name, ID, type,power,atktype,dmgtype,desc,manacost,targets,special):
      super().__init__(name, ID, type,desc,manacost,targets)
      self.power=power
      self.atktype =atktype
      self.dmgtype=dmgtype
      self.special=special
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
             cskill=0
             print("Attacked")
             valid=True
          elif choice =="2":
             valid= True
             cskill=skillselect(cunit)
          if cskill.targets==1 or cskill==0:
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
          damagecalc(cunit,cskill,target)   
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
                     print(f"Power: {cskill.power} Mana cost: {cskill.manacost}")
                     valid = False
                     while not valid:
                      choice = input("Use this skill? (y/n) ").lower()
                      if choice =="y" or choice =="n":
                         valid = True
                         if choice=="y":
                          print("Skill used")
                          return cskill
                         else:
                            skillselect(cunit)
                   else:
                      moveselect(cunit)
def damagecalc(attacker,cskill,target):
   if cskill==0:
      atktype=attacker.equipped.weapon.damagetype
      dmgtype=atktype
      power=10
      special=attacker.equipped.weapon.special 
   else:
      atktype=cskill.atktype
      dmgtype=cskill.dmgtype
      power=cskill.power
      special=cskill.special
   if atktype==1:
      atkstat=attacker.effattack
   elif atktype==2:
      atkstat=attacker.effmag
   if dmgtype==1:
      defstat=target.effdefence
   elif dmgtype==2:
      defstat=target.effmag
   dmg=round((atkstat/defstat)*power*(random.randint(85,100))/100)
   print(dmg)

      
espear=weapon(0,False,0,20,0,5,[],"Thunder Spear",1)
gloves=armour(50,True,15,30,0,0,[],"arms","Gloves")
ironswrd=weapon(30,True,5,20,-2,0,[],"Iron Sword",1)
lthrchest=armour(25,True,25,0,0,0,[],"body","Leather Chestplate")
nothingarmour=armour(0,False,0,0,0,0,[],"any","nothing")
nothingweapon=weapon(0,False,0,0,0,0,[],"nothing",1)
speedboost=ability("Speed Boost",1)
tbolt=atkskill("Thunderbolt",1,0,20,2,2,"Attack an enemy with a bolt of lightning, dealing magic damage and a chance to paralyse",10,1,[])
cass=partymember("Cass",100,30,50,40,40,30,[speedboost],[tbolt],equipped(espear,nothingarmour,nothingarmour,lthrchest,nothingarmour,gloves),10,0,True)
slime=unit("Slime",50,10,20,50,20,15,[],[],equipped(nothingweapon,nothingarmour,nothingarmour,nothingarmour,nothingarmour,nothingarmour),False,5)
skeleton=unit("Skeleton",30,7,30,20,30,10,[],[],equipped(ironswrd,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),False,5)
units=[cass,slime,skeleton]

for x in units:
   x.setstats()
turnorder(units)
for x in units:
   print (x.name)
   if x.playable:
      moveselect(x)
      


