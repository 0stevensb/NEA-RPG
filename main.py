import random
class unit():
    def __init__(self,name,maxhp,maxmp,attack,defence,speed,magic,dex,agility,abilities,skills,equipped,level,playable,friendly):
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
      self.status=[]
    def setstats(self):
       self.effattack=(self.baseattack+self.equipped.totalatk)*(1+self.atkbst*0.25)
       self.effdefence=(self.basedefence+self.equipped.totaldef)*(1+self.defbst*0.25)
       self.effspeed=(self.basespeed+self.equipped.totalspd)*(1+self.spdbst*0.25)
       self.effmag=(self.basemagic+self.equipped.totalmag)*(1+self.magbst*0.25)
       self.effdex=(self.basedex+self.equipped.totaldex)*(1+self.dexbst*0.25)
       self.effagility=(self.baseagility+self.equipped.totalagility)*(1+self.agilitybst*0.25)
       for x in self.status:
           if x.ID==2:
            self.effdefence=round(self.effdefence*0.85)
           if x.ID==1:
            self.effspeed=round(self.effspeed/2) 
class partymember(unit):
   def __init__(self, name, maxhp, maxmp, attack, defence, speed, magic, dex,agility,abilities, skills, equipped,level,xp,playable,friendly):
      super().__init__(name, maxhp, maxmp, attack, defence, speed, magic, dex, agility, abilities, skills, equipped, playable, level, friendly)
      self.xp=xp
class enemy(unit):
   def __init__(self, name, maxhp, maxmp, attack, defence, speed, magic, dex, agility, abilities, skills, equipped, level, playable, friendly,xpdrop,goldrop,itemdrop):
      super().__init__(name, maxhp, maxmp, attack, defence, speed, magic, dex, agility, abilities, skills, equipped, level, playable, friendly)
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
   def __init__(self,name,ID,desc):
      self.name=name
      self.ID=ID
      self.desc=desc
class status():
   def __init__(self,name,ID,type):
      self.name=name
      self.ID=ID
      self.type=type
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
      global enemyunits,playerunits,friendlyunits
      valid=False
      choice=0
      cskill=basicatk
      while not valid:
       choice=input("Attack (1), Skills (2) ")
       if choice=="1" or choice=="2":
          if choice =="1":
             valid=True
          elif choice =="2":
             valid= True
             cskill=0
             while cskill==0:
               cskill=skillselect(cunit)
               if cskill==1:
                  moveselect(cunit)
      makemove(cunit,cskill)
def makemove(cunit,cskill):
          global enemyunits,playerunits,friendlyunits
          if cskill.targets==1:
                tempunits=units.copy()
                tempunits.remove(cunit)
                for x in range(len(tempunits)):
                 print(f"{x+1}: {tempunits[x].name}")
                valid=False
                while not valid:
                    targetnum=int(input("Which will you target? "))-1
                    if targetnum<=len(tempunits):
                        target=[tempunits[targetnum]]
                        valid=True
          elif cskill.targets==2:
             target=enemyunits.copy()
          elif cskill.targets==5:
               tempunits=units.copy()
               tempunits.remove(cunit)
               target=tempunits
          if cskill.type==0:
            atkspecials = specialsassign(cunit,cskill)
            for ctarget in target:
               attack(cunit,ctarget,cskill,atkspecials)
          elif cskill.type==1:
              if cskill.ID==12:
                  for x in range(len(friendlydefeated)):
                     print(f"{x+1}: {friendlydefeated[x].name}")
                  valid=False
                  while not valid:
                     targetnum=int(input("Which will you target? "))-1
                     if targetnum<=len(friendlydefeated):
                           target=friendlydefeated[targetnum]
                           valid=True
                     target.hp=round(target.maxhp/2)
                     units.append(target)
                     print(f"{target.name} was revived!")
                     for x in units:
                        x.setstats()
                     playerunits=[]
                     friendlyunits=[]
                     enemyunits=[]
                     for x in units:
                           if x.friendly:
                              if x.playable:
                                 playerunits.append(x)
                              else:
                                 friendlyunits.append(x)
                           else:
                              enemyunits.append(x)
                           turnorder(units)
          elif cskill.type==2:
               for x in range(len(units)):
                 print(f"{x+1}: {units[x].name}")
               valid=False
               while not valid:
                    targetnum=int(input("Which will you target? "))-1
                    if targetnum<=len(units):
                        target=units[targetnum]
                        valid=True
               if cskill.ID==9:
                  healing=round(0.75*cunit.effmag)
                  target.hp+=healing
                  if target.hp>target.maxhp:
                     target.hp=target.maxhp
                  print(f"{target.name} healed {healing} hp!")
          for i in cunit.status:
           if i.ID==2:
               statusdmg=round(cunit.maxhp/10)
               cunit.hp-=statusdmg
               print(f"{cunit.name} took {statusdmg} burn damage!")   
           if i.ID==3:
               statusdmg=round(cunit.maxhp/8)
               cunit.hp-=statusdmg
               print(f"{cunit.name} took {statusdmg} poison damage!") 
          hpcheck()
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
                     if cskill.type==0:
                        print(f"Power: {cskill.power} Mana cost: {cskill.manacost} Accuracy: {cskill.accuracy}")
                     if cunit.mp< cskill.manacost:
                        print("Insufiicent MP!")
                        return 0
                     elif cskill.ID==12 and len(friendlydefeated)<1:
                         print("No valid targets")
                         return 0
                     else:
                        valid = False
                        while not valid:
                           choice = input("Use this skill? (y/n) ").lower()
                           if choice =="y" or choice =="n":
                              valid = True
                        if choice=="y":
                              cunit.mp-=cskill.manacost
                              return cskill
                        elif choice=="n":
                              return 0
                   else:
                      return 1
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
        critratemult*=1.5
   for x in defspecials:
      if x.ID==7 and dmgtype==1:
         dmgmult=0
      for i in atkspecials:
       if x.ID==15 and i.ID==18:
          dmgmult*=2
       if x.ID==8 and i.ID==18:
         dmgmult=0
       if (x.ID==12 or x.ID==7) and i.ID==19 :
          dmgmult=0
   critrate=(attacker.effdex/2)*critratemult
   if random.randint(1,100)<=critrate:
      dmgmult*=3
      print("Critical Hit!")
   
   dmg=round((atkstat/defstat)*power*(random.randint(85,115))/100)*dmgmult
   return dmg
def aiturn(cunit):
            global playerunits,friendlyunits,enemyunits,enemydefeated,friendlydefeated
            enemies=[]
            for i in units:
               if cunit.friendly:
                if not i.friendly:
                  enemies.append(i)
               else:
                  if i.friendly:
                     enemies.append(i)
            usableskills=[]
            for x in cunit.skills:
               if x.manacost<= cunit.mp:
                  if cunit.friendly:
                      if len(friendlydefeated)>0:
                        usableskills.append(x)
                  else:
                      if len(enemydefeated)>0:
                        usableskills.append(x)
            if len(usableskills)>0 and random.randint(1,2)==2:
               cskill=random.choice(usableskills)
               cunit.mp-=cskill.manacost
            else:
               cskill=basicatk
            print(f"{cunit.name} used {cskill.name}!")
            if cunit.friendly:
                posstargets=enemyunits.copy()
            else:
               posstargets=playerunits.copy()+friendlyunits.copy()
            if cskill.targets==1:
             target=[random.choice(posstargets)]
            elif cskill.targets==2:
             target=posstargets
            elif cskill.targets==4:
                if cunit.friendly:
                  target=random.choice(friendlydefeated)
                else:
                    target=random.choice(enemydefeated)
            elif cskill.targets==5:
               tempunits=units.copy()
               tempunits.remove(cunit)
               target=tempunits
            if cskill.type==0:
               atkspecials = specialsassign(cunit,cskill)
               for ctarget in target:
                  attack(cunit,ctarget,cskill,atkspecials)
            elif cskill.type==1:
               if cskill.ID==8:
                  for x in range(2):
                     units.append(enemy(cunit.name+f" {x+1}",round(cunit.hp/2),round(cunit.maxmp/2),round(cunit.baseattack/2),round(cunit.basedefence/2),round(cunit.basespeed/2),round(cunit.basemagic/2),round(cunit.basedex/2),round(cunit.baseagility*2),cunit.abilities,cunit.skills,cunit.equipped,cunit.level,cunit.playable,cunit.friendly,round(cunit.xpdrop/2),round(cunit.goldrop/2),cunit.itemdrop))
                  units.remove(cunit)
                  for x in units:
                     x.setstats()
                  playerunits=[]
                  friendlyunits=[]
                  enemyunits=[]
                  for x in units:
                     if x.friendly:
                        if x.playable:
                           playerunits.append(x)
                        else:
                           friendlyunits.append(x)
                     else:
                        enemyunits.append(x)
                     turnorder(units)
               if cskill.ID==12:
                   target.hp=round(target.maxhp/2)
                   units.append(target)
                   print(f"{target.name} was revived!")
                   for x in units:
                     x.setstats()
                   playerunits=[]
                   friendlyunits=[]
                   enemyunits=[]
                   for x in units:
                        if x.friendly:
                           if x.playable:
                              playerunits.append(x)
                           else:
                              friendlyunits.append(x)
                        else:
                           enemyunits.append(x)
                        turnorder(units)
            elif cskill.type==2:
               target=random.choice(enemyunits)
               if cskill.ID==9:
                  for x in enemyunits:
                      if x.hp< target.hp:
                          target=x
                  healing=round(0.75*cunit.effmag)
                  target.hp+=healing
                  if target.hp>target.maxhp:
                     target.hp=target.maxhp
                  print(f"{target.name} healed {healing} hp!")
            for i in cunit.status:
               if i.ID==2:
                  statusdmg=round(cunit.maxhp/10)
                  cunit.hp-=statusdmg
                  print(f"{cunit.name} took {statusdmg} burn damage!")   
               if i.ID==3:
                  statusdmg=round(cunit.maxhp/8)
                  cunit.hp-=statusdmg
                  print(f"{cunit.name} took {statusdmg} poison damage!") 
               if i.ID==4:
                   healing=round(cunit.maxhp/10)
                   cunit.hp+=healing
                   if cunit.hp>cunit.maxhp:
                       cunit.hp=cunit.maxhp
                   print(f"{cunit.name} healed {healing} hp!")
            hpcheck()
def attack(cunit,ctarget,cskill,atkspecials):
                  defspecials=specialsassign(ctarget,0)
                  hitchance=(cunit.effdex/ctarget.effagility)*cskill.accuracy
                  if random.randint(1,100)<=hitchance or cskill.accuracy==101:
                     for i in defspecials:
                         if i.ID==13 and cskill.dmgtype==2:
                             print(f"The attack was reflected by {ctarget.name}!")
                             ctarget=cunit
                             
                     dmg=damagecalc(cunit,cskill,ctarget,atkspecials,specialsassign(ctarget,0))   
                     ctarget.hp-=dmg
                     print(f"{ctarget.name} took {dmg} damage!")
                     brnimmune=False
                     toximmune=False
                     paraimmune=False
                     for i in defspecials:
                        if i.ID==8:
                           brnimmune=True
                        if i.ID==10:
                           toximmune=True
                        if i.ID==11:
                           paraimmune=True
                        if i.ID==12:
                            toximmune=True
                     for i in atkspecials:
                        healing=0
                        if i.ID==1:
                              cunit.spdbst+=1
                              print(f"{cunit.name}'s speed rose!")
                        if i.ID==2 and random.randint(1,3)==3:
                              ctarget.dexbst-=1
                              print(f"{ctarget.name}'s dexterity dropped!")
                        if i.ID ==3:
                           cunit.agilitybst+=1
                           print(F"{cunit.name}'s agility rose!")
                        if i.ID==5 and random.randint(1,3)==3 and not paraimmune:
                           ctarget.status.append(paralysis)
                           print(f"{ctarget.name} was paralysed!")
                        if i.ID==6 and random.randint(1,3)==3 and not brnimmune:
                           ctarget.status.append(burn)
                           print(f"{ctarget.name} was burned!")
                        if i.ID==10 and random.randint(1,3)==3 and not toximmune:
                           ctarget.status.append(poison)
                           print(f"{ctarget.name} was poisoned!")
                        if i.ID==14:
                            healing+=round(cunit.maxhp/10)
                        if i.ID==15 and cskill.atktype==1:
                            healing+=round(dmg/2)
                        if i.ID==17 and random.randint(1,3)==1:
                           ctarget.status.append(frozen)
                           print(f"{ctarget.name} was frozen!")
                        if healing>0:
                           cunit.hp+=healing
                           print(f"{cunit.name} healed {healing} hp!")
                           if cunit.hp>cunit.maxhp:
                              cunit.hp=cunit.maxhp
                  else:
                     print(f"{ctarget.name} dodged the attack!")  
def hpcheck():
 for i in units:
                     if i.hp <=0:
                        print(f"{i.name} was defeated!")
                        if i.playable:
                           playerunits.remove(i)
                           friendlydefeated.append(i)
                        elif i.friendly:
                           friendlyunits.remove(i)
                           friendlydefeated.append(i)
                        else:
                           enemydefeated.append(i)
                           enemyunits.remove(i)
                        units.remove(i)
def combat():
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
            move=True
            for j in x.status:
               if j.ID==1 and random.randint(1,3)==3:
                  move=False
                  print(f"{x.name} is fully paralysed!")
               if j.ID==5:
                  move=False
                  print(f"{x.name} is frozen!")
                  if random.randint(1,3)==3:
                     x.status.remove(j)
                     print(f"{x.name} thawed out!")
            if move:
                  if x.playable:
                        print(f"HP: {x.hp}/{x.maxhp}")
                        print(f"MP: {x.mp}/{x.maxmp}")
                        moveselect(x)
                  else:
                     aiturn(x)
def battleend():
   if len(playerunits)>0:
      totalxp=0
      totalgold=0
      print("You won!")
      for x in enemydefeated:
         totalxp+=x.xpdrop
         totalgold+=x.goldrop
      print(f"You gained {totalgold} gold!")
      for x in playerunits:
         xpgain=round(totalxp/len(playerunits))
         print(f"{x.name} gained {xpgain} xp!")
         x.xp+=xpgain
   else:
      print("You lost")

speedboost=special("Speed Boost",1,"Raises speed stat when attacking")
dexdwn=special("Dex Down",2,"1/3 chance to lower target's dexterity")
aglup=special("Agility Up",3,"Raises agility when attacking")
physcritup=special("Crit Rate up",4,"Physical attacks are 50% more likely to crit") 
paralyse=special("Paralyse", 5,"1/3 chance to inflict paralysis when attacking")
burnaf=special("Burned",6,"1/3 chance to inflict burn when attacking")
intangible=special("Intangible",7,"Take no damage from physical attacks")
fireimmune=special("Fire Immune",8,"Take no damage from fire attacks and immune to burn")
undead=special("Undead",9,"Immune to poison and bleed")
toxic=special("Toxic",10,"1/3 chance to apply poison when attacking")
paralysisimmune=special("Paralysis Immune",11,"Cannot be paralysed")
toximmune=special("Poison Immune",12,"Immune to poison attacks and being poisoned")
magreflect=special("Reflect Magic",13,"Reflect magic attacks back at the attacker")
regenerate=special("Regenerate",14,"Regenerate 10% of hp each turn")
vampiric=special("Vampiric",15,"Recover half of physical damage done")
fireweak=special("Fire Weakness",16,"Take double damage from fire attacks")
freeze=special("Freeze",17,"1/3 chance to freeze when attacking")
fire=special("Fire",18,"Fire")
poison=special("Poison",19,"Poison")


paralysis=status("Paralysed",1,1)
burn=status("Burned",2,1)
poison=status("Poisoned",3,1)
regen=status("Regen",4,2)
frozen=status("Frozen",5,1)

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
magignothingweapon=weapon(0,False,0,0,0,0,0,0,[],"nothing",2)

basicatk=atkskill("Basic attack",0,0,10,1,1,"A basic attack",0,1,[],100)
tbolt=atkskill("Thunderbolt",1,0,20,2,2,"Attack an enemy with a bolt of lightning, dealing magic damage and a chance to paralyse",10,1,[paralyse],90)
spdyslsh=atkskill("Speedy Slash",2,0,8,1,1,"Strike an enemy quickly, raising the user's speed stat",15,1,[speedboost],100)
wildstrike=atkskill("Wild Strike",3,0,30,1,1,"A powerful but inaccurate physical attack",5,1,[],60)
darkspike=atkskill("Dark Spike",4,0,15,2,1,"Attack a target with spikes of darkness. A magical attack that deals physical damage",7,1,[],95)
darkblast=atkskill("Dark Blast",5,0,20,2,2,"Launch a collection of dark energy at the target. Chance to reduce dexterity",10,1,[dexdwn],90)
sneakystrike=atkskill("Sneaky Strike",6,0,11,1,1,"Attack the target from the shadows, raising agility and never missing",5,1,[aglup],101)
heatwave=atkskill("Heat Wave",7,0,14,2,2,"Hit all opponents with a blast of superheated air. Has a chance to burn",10,2,[burnaf,fire],80)
split=skill("Split",8,1,"Split into two smaller copies",0,0)
heal=skill("Heal",9,2,"Restore the target's HP",10,3)
poisonstrike=atkskill("Poisoned Strike",10,0,12,1,1,"Attack an enemy with a poisoned attack",6,1,[toxic],100)
poisonspray=atkskill("Poison Spray",11,0,15,2,2,"Spray poison at all enemies",5,2,[toxic,poison],85)
revive=skill("Revive",12,1,"Revive a defeated ally",20,4)
blizzard=atkskill("Blizzard",13,0,17,2,2,"Summon a blizzard that hits all units on the field with a chance to freeze",13,5,[freeze],80)

cass=partymember("Cass",50,30,50,40,40,30,30,30,[],[tbolt,spdyslsh,wildstrike],equipped(espear,nothingarmour,nothingarmour,lthrchest,nothingarmour,gloves),10,0,True,True)
aster=partymember("Aster",30,25,30,20,35,40,50,50,[],[spdyslsh,darkspike,darkblast,sneakystrike,poisonstrike],equipped(assassinknife,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),10,0,True,True)
elphis=partymember("Elphis",25,50,15,15,25,50,20,20,[],[tbolt,heatwave,heal,blizzard],equipped(wand,nothingarmour,nothingarmour,robe,nothingarmour,nothingarmour),10,0,True,True)

slime=enemy("Slime",50,10,20,50,20,15,10,10,[paralysisimmune,toximmune],[split,poisonspray],equipped(nothingweapon,nothingarmour,nothingarmour,nothingarmour,nothingarmour,nothingarmour),5,False,False,10,10,[])
skeleton=enemy("Skeleton",30,7,30,20,30,10,20,25,[undead,paralysisimmune],[],equipped(ironswrd,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),5,False,False,10,10,[])
firespirit=enemy("Fire Spirit",20,30,10,10,40,35,30,35,[intangible,fireimmune,undead,paralysisimmune],[heatwave],equipped(magignothingweapon,nothingarmour,nothingarmour,nothingarmour,nothingarmour,nothingarmour),10,False,False,20,30,[])
healer=enemy("Healer",25,40,10,20,20,40,20,20,[magreflect,regenerate],[heal],equipped(wand,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),7,False,False,30,30,[])
vampire=enemy("Vampire",40,25,30,25,30,25,35,25,[vampiric,fireweak,undead],[],equipped(nothingweapon,nothingarmour,nothingarmour,nothingarmour,nothingarmour,nothingarmour),10,False,False,30,40,[])
necromancer=enemy("Necromancer",50,60,10,25,15,35,20,10,[],[revive],equipped(magignothingweapon,nothingarmour,nothingarmour,nothingarmour,nothingarmour,nothingarmour),15,False,False,60,60,[])

jeff=unit("Jeff",20,10,10,10,10,5,15,15,[],[],equipped(ironswrd,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),4,False,True)

units=[cass,aster,slime,skeleton,jeff,elphis,firespirit,healer,vampire,necromancer]
playerunits=[]
friendlyunits=[]
enemyunits=[]
enemydefeated=[]
friendlydefeated=[]


combat()
battleend()
       
      