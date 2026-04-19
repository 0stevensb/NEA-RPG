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
      self.defeated=False
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
      super().__init__(name, maxhp, maxmp, attack, defence, speed, magic, dex, agility, abilities, skills, equipped, level, playable, friendly)
      self.xp=xp
class enemy(unit):
   def __init__(self, name, maxhp, maxmp, attack, defence, speed, magic, dex, agility, abilities, skills, equipped, level, playable, friendly,xpdrop,goldrop,itemdrop):
      super().__init__(name, maxhp, maxmp, attack, defence, speed, magic, dex, agility, abilities, skills, equipped, level, playable, friendly)
      self.xpdrop=xpdrop
      self.goldrop=goldrop
      self.itemdrop=itemdrop
      self.aggro={}
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
   def __init__(self,name,ID,type,desc,manacost,targets,aggro):
      self.name = name
      self.ID=ID
      self.type=type
      self.desc=desc
      self.manacost=manacost
      self.targets=targets
      self.aggro=aggro
class atkskill(skill):
   def   __init__(self, name, ID, type,power,atktype,dmgtype,desc,manacost,targets,special,acc,aggro):
      super().__init__(name, ID, type,desc,manacost,targets,aggro)
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
   length=len(list1)
   if length<=1:
      return list1
   middle=length//2
   left=list1[:middle]
   right=list1[middle:]
   sortright=turnorder(right)
   sortleft=turnorder(left)
   result=merge(sortleft,sortright)
   return result
def merge(left,right):
   result=[]
   i=0
   j=0
   while i<len(left) and j <len(right):
      if left[i].effspeed<right[j].effspeed:
         result.append(left[i])
         i+=1
      else:
         result.append(right[j])
         j+=1
      result.extend(left[i:])
      result.extend(right[j:])
      return result

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
   
   dmg=round((atkstat/defstat)*power*(random.randint(85,115))/100)*dmgmult
   return dmg
def aiturn(cunit,playerunits,friendlyunits,enemyunits):
            usableskills=[]
            for x in cunit.skills:
               if x.manacost<= cunit.mp:
                  if x.ID==12:
                     if cunit.friendly:
                        usable=False
                        for i in (friendlyunits+playerunits):
                           if i.defeated:
                              usable=True
                     else:
                        usable=False
                        for i in (enemyunits):
                           if i.defeated:
                              usable=True
                     if usable:
                        usable.apppend(x)
                  else:   
                     usableskills.append(x)
            if len(usableskills)>0 and random.randint(1,2)==2:
               cskill=random.choice(usableskills)
               cunit.mp-=cskill.manacost
            else:
               cskill=basicatk
            return cskill
def aitarget(cunit, playerunits, friendlyunits, enemyunits, cskill):
    if cunit.friendly:
        posstargets=enemyunits.copy()
        posstargetscopy=posstargets.copy()
    else:
       posstargets=(playerunits.copy()+friendlyunits.copy())
       posstargetscopy=posstargets.copy()
    for i in posstargetscopy:
       if i.defeated:
          posstargets.remove(i)
    if cskill.targets==0:
       target=[cunit]
    elif cskill.targets==1:
      if not cunit.friendly:
         target=[posstargets[0]]
         for i in posstargets:
            if cunit.aggro[i]>cunit.aggro[target[0]]:
               target=[i]
      else:
         target=[random.choice(posstargets)]
    elif cskill.targets==2:
     target=posstargets
    elif cskill.targets==3:
       if cunit.friendly:
          target=friendlyunits+playerunits
       else:
          target=enemyunits
    elif cskill.targets==4:
        if cunit.friendly:
          targets=[]
          for i in units:
             if i.defeated and i.friendly:
                targets.append(i)
        else:
            targets=[]
            for i in units:
                if i.defeated and not i.friendly:
                   targets.append(i)
        target=[random.choice(targets)]
    elif cskill.targets==5:
       tempunits=units.copy()
       tempunits.remove(cunit)
       for i in tempunits:
          if i.defeated:
             tempunits.remove(i)
       target=tempunits
    return target
def statuscheck(cunit):
    for i in cunit.status:
       if i.ID==2:
          statusdmg=round(cunit.maxhp/10)
          cunit.hp-=statusdmg 
       if i.ID==3:
          statusdmg=round(cunit.maxhp/8)
          cunit.hp-=statusdmg
       if i.ID==4:
           healing=round(cunit.maxhp/10)
           cunit.hp+=healing
           if cunit.hp>cunit.maxhp:
               cunit.hp=cunit.maxhp
def attack(cunit,ctarget,cskill,atkspecials,units):
                  effects=[]
                  dmg=0
                  defspecials=specialsassign(ctarget,0)
                  hitchance=(cunit.effdex/ctarget.effagility)*cskill.accuracy
                  if random.randint(1,100)<=hitchance or cskill.accuracy==101:
                     for i in defspecials:
                         if i.ID==13 and cskill.dmgtype==2:
                             effects.append(1)
                             ctarget=cunit  
                     dmg=damagecalc(cunit,cskill,ctarget,atkspecials,specialsassign(ctarget,0))   
                     ctarget.hp-=dmg
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
                              effects.append(2)
                        if i.ID==2 and random.randint(1,3)==3:
                              ctarget.dexbst-=1
                              effects.append(3)
                        if i.ID ==3:
                           cunit.agilitybst+=1
                           effects.append(4)
                        if i.ID==5 and random.randint(1,3)==3 and not paraimmune:
                           ctarget.status.append(paralysis)
                           effects.append(5)
                        if i.ID==6 and random.randint(1,3)==3 and not brnimmune:
                           ctarget.status.append(burn)
                           effects.append(6)
                        if i.ID==10 and random.randint(1,3)==3 and not toximmune:
                           ctarget.status.append(poison)
                           effects.append(7)
                        if i.ID==14:
                            healing+=round(cunit.maxhp/10)
                        if i.ID==15 and cskill.atktype==1:
                            healing+=round(dmg/2)
                        if i.ID==17 and random.randint(1,3)==1:
                           ctarget.status.append(frozen)
                           effects.append(8)
                        if healing>0:
                           cunit.hp+=healing
                           effects.append(9)
                           if cunit.hp>cunit.maxhp:
                              cunit.hp=cunit.maxhp
                  else:
                     effects.append(0) 
                  hpcheck(units)
                  return effects,dmg,unit
def hpcheck(units):
 for i in units:
   if i.hp <=0:
      i.defeated=True
def checkmove(x):
    move=True
    for j in x.status:
       if j.ID==1 and random.randint(1,3)==3:
          move=False
       if j.ID==5:
          move=False
    return move
def battleend(playerunits,enemyunits):
   if len(playerunits)>0:
      totalxp=0
      totalgold=0
      for x in enemyunits:
         totalxp+=x.xpdrop
         totalgold+=x.goldrop
      playable=[]
      for x in playerunits:
         if x.playable:
            playable.append(x)
      for x in playable:
         xpgain=round(totalxp/len(playable))
         x.xp+=xpgain
         if x.xp>100:
            x.xp-=100
            x.level+=1
            stats=[x.maxhp,x.maxmp,x.basespeed,x.baseattack,x.baseattack,x.basemagic,x.baseagility,x.basedex]
            for i in range(5):
               stats[random.randint(0,len(stats)-1)]+=5
            x.hp,x.mp=x.maxhp,x.maxmp
      return totalgold
def combatinit(units):
   playerunits=[]
   enemyunits=[]
   friendlyunits=[]
   for x in units:
      if x.friendly:
         if x.playable:
            playerunits.append(x)
         else:
            friendlyunits.append(x)
      else:
         enemyunits.append(x)
   return playerunits,friendlyunits,enemyunits
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

healthpotion=item(20,True,"Health Potion")
bomb=item(40,True,"Bomb")
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

basicatk=atkskill("Basic attack",0,0,10,1,1,"A basic attack",0,1,[],100,10)
tbolt=atkskill("Thunderbolt",1,0,20,2,2,"Attack an enemy with a bolt of lightning, dealing magic damage and a chance to paralyse",10,1,[paralyse],90,30)
spdyslsh=atkskill("Speedy Slash",2,0,8,1,1,"Strike an enemy quickly, raising the user's speed stat",15,1,[speedboost],100,15)
wildstrike=atkskill("Wild Strike",3,0,30,1,1,"A powerful but inaccurate physical attack",5,1,[],60,35)
darkspike=atkskill("Dark Spike",4,0,15,2,1,"Attack a target with spikes of darkness. A magical attack that deals physical damage",7,1,[],95,25)
darkblast=atkskill("Dark Blast",5,0,20,2,2,"Launch a collection of dark energy at the target. Chance to reduce dexterity",10,1,[dexdwn],90,20)
sneakystrike=atkskill("Sneaky Strike",6,0,11,1,1,"Attack the target from the shadows, raising agility and never missing",5,1,[aglup],101,-20)
heatwave=atkskill("Heat Wave",7,0,14,2,2,"Hit all opponents with a blast of superheated air. Has a chance to burn",10,2,[burnaf,fire],80,35)
heal=skill("Heal",9,2,"Restore the target's HP",10,3,30)
poisonstrike=atkskill("Poisoned Strike",10,0,12,1,1,"Attack an enemy with a poisoned attack",6,1,[toxic],100,20)
poisonspray=atkskill("Poison Spray",11,0,15,2,2,"Spray poison at all enemies",5,2,[toxic,poison],85,30)
revive=skill("Revive",12,1,"Revive a defeated ally",20,4,50)
blizzard=atkskill("Blizzard",13,0,17,2,2,"Summon a blizzard that hits all units on the field with a chance to freeze",13,5,[freeze],80,45)
bombthrow=atkskill("Bomb Throw",14,0,25,1,2,"Throw a bomb at the target",0,1,[],100,30)

cass=partymember("Cass",50,30,50,40,40,30,30,30,[],[tbolt,spdyslsh,wildstrike],equipped(espear,nothingarmour,nothingarmour,lthrchest,nothingarmour,gloves),10,100,True,True)
aster=partymember("Aster",30,25,30,20,35,40,50,50,[],[spdyslsh,darkspike,darkblast,sneakystrike,poisonstrike],equipped(assassinknife,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),10,0,True,True)
elphis=partymember("Elphis",25,50,15,15,25,50,20,20,[],[tbolt,heatwave,heal,blizzard],equipped(wand,nothingarmour,nothingarmour,robe,nothingarmour,nothingarmour),10,0,True,True)

slime=enemy("Slime",50,10,20,50,20,15,10,10,[paralysisimmune,toximmune],[poisonspray],equipped(nothingweapon,nothingarmour,nothingarmour,nothingarmour,nothingarmour,nothingarmour),5,False,False,10,10,[])
skeleton=enemy("Skeleton",30,7,30,20,30,10,20,25,[undead,paralysisimmune],[],equipped(ironswrd,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),5,False,False,10,10,[])
firespirit=enemy("Fire Spirit",20,30,10,10,40,35,30,35,[intangible,fireimmune,undead,paralysisimmune],[heatwave],equipped(magignothingweapon,nothingarmour,nothingarmour,nothingarmour,nothingarmour,nothingarmour),10,False,False,20,30,[])
healer=enemy("Healer",25,40,10,20,20,40,20,20,[magreflect,regenerate],[heal],equipped(wand,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),7,False,False,30,30,[])
vampire=enemy("Vampire",40,25,30,25,30,25,35,25,[vampiric,fireweak,undead],[],equipped(nothingweapon,nothingarmour,nothingarmour,nothingarmour,nothingarmour,nothingarmour),10,False,False,30,40,[])
necromancer=enemy("Necromancer",50,60,10,25,15,35,20,10,[],[revive],equipped(magignothingweapon,nothingarmour,nothingarmour,nothingarmour,nothingarmour,nothingarmour),15,False,False,60,60,[])

jeff=unit("Jeff",20,10,10,10,10,5,15,15,[],[],equipped(ironswrd,nothingarmour,nothingarmour,lthrchest,nothingarmour,nothingarmour),4,False,True)

units=[cass,aster,jeff,elphis]
inventory=[healthpotion,healthpotion,healthpotion,bomb]



       
      