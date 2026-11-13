import copy
import sys
from time import sleep, time

TOP = 1
BOT = 2
LEFT = 3
RIGTH = 4





class Game():
 
 def __init__(self, mainArea, protagonist):
  
  self.mainArea = mainArea
  
  self.protagonist = protagonist

 def render(self):

  self.mainArea.render()

 def Hero_move(self, rotation):

  checker = self.protagonist.moveTo(rotation, self.mainArea)

  if checker != None:
    poses = []

    for door in checker[0][2].doors:

     if door[2] == self.mainArea:

      poses = [door[0], door[1]]


    self.mainArea.chars = []

    self.mainArea = checker[0][2]
    if checker[1] == TOP: self.mainArea.append_char(self.protagonist, poses[1], poses[0]-1)

    if checker[1] == BOT: self.mainArea.append_char(self.protagonist, poses[1], poses[0]+1)

    if checker[1] == LEFT: self.mainArea.append_char(self.protagonist, poses[1]-1, poses[0])

    if checker[1] == RIGTH: self.mainArea.append_char(self.protagonist, poses[1]+1, poses[0])

    

   

   


class Time():

 def clock(self, clocks):

  q = time()

  while 1:

   if time() - q >= clocks:
    break

    
class Character():
  
  def __init__(self, maxHp, defend, weapon, skin):
   
   self.y = None
   self.x = None
   
   self.maxHp = maxHp
   self.defend = defend
   self.weapon = weapon
   self.skin = skin

  def moveTo(self, rotation, area):
   if rotation == TOP:
      if area.area[self.y-1][self.x] != "■":
       if area.area[self.y-1][self.x] == "□":
        self.y -= 1
       elif area.area[self.y-1][self.x] == "D":
        for door in area.doors:
          if [door[0], door[1]] == [self.y-1, self.x]:


           return [door, TOP]


   if rotation == BOT:
       if area.area[self.y+1][self.x] != "■":
        if area.area[self.y+1][self.x] == "□":
         self.y +=1
        elif area.area[self.y+1][self.x] == "D":
         for door in area.doors:
           if [door[0], door[1]] == [self.y+1, self.x]:
            
            return [door, BOT]

        


   if rotation == LEFT:
       if area.area[self.y][self.x-1] != "■":
        if area.area[self.y][self.x-1] == "□":
         self.x-=1
        elif area.area[self.y][self.x-1] == "D":
         for door in area.doors:
          if [door[0], door[1]] == [self.y, self.x-1]:

           return [door, LEFT]


   if rotation == RIGTH:
       if area.area[self.y][self.x+1] != "■":
        if area.area[self.y][self.x+1] == "□":
         self.x+=1
        elif area.area[self.y][self.x+1] == "D":
         for door in area.doors:
          if [door[0], door[1]] == [self.y, self.x-1]:
        
           return [door, RIGTH]

   
 
class Weapon():
 
 def __init__(self, name, damage, range, ammo):
  
  self.name = name
  self.damage = damage
  self.range = range
  self.ammo = ammo
  
class Ammo():
 
 def __init__(self, name):
  
  self.name = name
 
class Area():
 
 def __init__(self, x, y):
  self.x = x
  self.y = y
  
  self.doors = []
  self.chars = []
  
  self.area = [["■" for q in range(x)]]
  
  for n in range(y-2):
   
   self.area.append(["□" for q in range (x-2)])
   self.area[n+1].insert(0, "■")
   self.area[n+1].append("■")
   
  
  self.area.append(["■" for q in range (x)])

  

 def create_door(self, x, y, link):
  
  self.doors.append([y-1, x-1, link])
  self.area[y-1][x-1] = "D"

 def create_wall(self, x, y):
  self.area[y][x] = "■"

  
  
 def append_char(self, char, x, y):
  
  char.x = x
  char.y = y
  
  self.chars.append(char)
 
  

 def render(self):
  
  tempArea = copy.deepcopy(self.area)
  
  #for door in self.doors:
   #tempArea[door[0]][door[1]] = "D"
   
  for char in self.chars:
   tempArea[char.y][char.x] = char.skin

  rendered_map = "\n".join(" ".join(row) for row in tempArea)

  sys.stdout.write("\n" * 35 + rendered_map + "\n")
  sys.stdout.flush()
