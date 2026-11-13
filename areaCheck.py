from classes import *



secondArea = Area(15, 15)

startArea = Area(5, 5)


startArea.create_door(3, 1, secondArea)
secondArea.create_door(5, 15, startArea)

for i in range(5):
    secondArea.create_wall(6, 4+i)

for i in range(5):
    secondArea.create_wall(4+i, 6)


area = secondArea

print(" ", *[x for x in range(len(area.area[0]))])
qw = 0
for i in area.area:
    print(qw, *i)
    qw+=1

