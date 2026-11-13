from classes import *
from keyboard import is_pressed
RUN = True

timer = Time()

kulaki = Weapon("Кулаки", 5, 1, None)

secondArea = Area(15, 15)

startArea = Area(5, 5)


startArea.create_door(3, 1, secondArea)
secondArea.create_door(5, 15, startArea)


eblo = Character(100, 0, kulaki, "0")

#startArea.render()

#secondArea.render()

Core = Game(startArea, eblo)

startArea.append_char(eblo, 2, 2)


for i in range(5):
    secondArea.create_wall(6, 4+i)

for i in range(5):
    secondArea.create_wall(4+i, 6)

secondArea.create_wall(4, 5)
secondArea.create_wall(4, 4)

secondArea.create_wall(7, 4)
secondArea.create_wall(8, 4)

secondArea.create_wall(8, 7)
secondArea.create_wall(8, 8)

secondArea.create_wall(5, 8)
secondArea.create_wall(4, 8)





while RUN:

    timer.clock(0.3)
    

    Core.render()

    if is_pressed("W"):

        Core.Hero_move(TOP)

    if is_pressed("S"):
    
        Core.Hero_move(BOT)

    if is_pressed("A"):
    
        Core.Hero_move(LEFT)

    if is_pressed("D"):
    
        Core.Hero_move(RIGTH)