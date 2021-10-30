import math
class emptyRoom:
    def __init__(self):
        self.id = "e"
        self.x = 0
        self.y = 0
        self.size = 0
        self.posTopLeft = [0,0]

class workingRoom:
    def __init__(self):
        self.id = "w"
        self.size = 6
        self.x = 2
        self.y = 3
        self.posTopLeft = [0,0]
    def rotate(self):
        self.x, self.y = self.y, self.x
        

class meetingRoom1:
    def __init__(self):
        self.id = "m1"
        self.size = 12
        self.x = 4
        self.y = 3
        self.posTopLeft = [0,0]
    def rotate(self):
        self.x, self.y = self.y, self.x

class meetingRoom2:
    def __init__(self):
        self.id = "m2"
        self.size = 24
        self.x = 4
        self.y = 6
        self.posTopLeft = [0,0]
    def rotate(self):
        self.x, self.y = self.y, self.x


class building:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.topRooms = []
        self.bottomRooms = []
        self.rightRooms = []
        self.leftRooms = []
        self.middleRooms = []
        self.size = x*y
        
        self.makeRooms(self.size)
        self.placeRooms()
        
    def makeRooms(self,m):   # we get total meters for the office floor.
        workingRoomsArea = m*0.4   #we want 0.4 of the office floor to be generated as working rooms
          # We count the amount of working rooms to be generated in totalt.
        self.workingRoomsList = []
        
        while workingRoomsArea >= 6:
            workingRoomx = workingRoom()
            self.workingRoomsList.append(workingRoom())  #we add the working room to our list of working rooms
            workingRoomsArea -=6                   # we substract 6m from the total area 
        
        meetingRoomsArea = m*0.2 + workingRoomsArea
        ammountOfMeetingRooms = int(len(self.workingRoomsList)/4)
        ammountOfMeetingRooms2 = int(ammountOfMeetingRooms/4)
        ammountOfMeetingRooms1 = ammountOfMeetingRooms-(ammountOfMeetingRooms2*2)
        
        self.meetingRooms2List = []
        self.meetingRooms1List = []
    
        for i in range(0,ammountOfMeetingRooms1):
            self.meetingRooms1List.append(meetingRoom1())
            
        for i in range(0,ammountOfMeetingRooms2):
            self.meetingRooms2List.append(meetingRoom2())
        
    def getMaxWorkRooms(self):
        return int(self.x*1/2)*2 + int((self.y-8)/2)*2
    
    def getMinYFromListOfRooms(self,listOfRooms):
        mini = math.inf:
        for i in listOfRooms:
            if mini > listOfRooms.topLeftPos[1]:
                mini = listOfRooms.topLeftPos[1]
        return mini
            
    
    def getRoom(self, typ):
        rooms_of_type = []
        for i in self.rooms:
            if i.typ == typ:
                rooms_of_type.append(i)
        rooms_of_type.sort(key=lambda x: x.size)
        return rooms_of_type
    
    def addRoom(self, room):
        self.rooms.append(room)
        self.size+=room.size
    
    def getRoomsSortedBySize(self):
        sortedRooms = self.rooms.copy()
        sortedRooms.sort(key=lambda x: x.size)
        return sortedRooms
    
    def placeRooms(self):
        edges = 0
        meetingRooms2ListCopy = self.meetingRooms2List.copy()
        meetingRooms1ListCopy = self.meetingRooms1List.copy()
        workingRoomsListCopy = self.workingRoomsList.copy()
        self.topRooms.append(emptyRoom())
        self.topRooms[-1].posTopLeft[1] = self.y
        self.rightRooms.append(emptyRoom())
        self.rightRooms[-1].posTopLeft[0] = self.x-3
        self.rightRooms[-1].posTopLeft[1] = self.y
        self.bottomRooms.append(emptyRoom())
        self.bottomRooms[-1].posTopLeft[1] = 3
        self.leftRooms.append(emptyRoom())
        
        
         #First place the upper row. 
        if self.size<=17**2:
            while len(meetingRooms2ListCopy) != 0:
                nextRoom = meetingRooms2ListCopy.pop()
                nextRoom.posTopLeft[0] = self.topRooms[-1].posTopLeft[0] + self.topRooms[-1].x
                nextRoom.posTopLeft[1] = self.y
                self.topRooms.append(nextRoom)
            
            if len(meetingRooms1ListCopy) != 0:
                nextRoom = meetingRooms1ListCopy.pop()
                nextRoom.posTopLeft[0] = self.topRooms[-1].posTopLeft[0] + self.topRooms[-1].x
                nextRoom.posTopLeft[1] = self.y
                self.topRooms.append(nextRoom)
            
            while len(meetingRooms1ListCopy) != 0:
                nextRoom = meetingRooms1ListCopy.pop()
                nextRoom.posTopLeft[0] = self.topRooms[-1].posTopLeft[0]
                nextRoom.posTopLeft[1] = self.topRooms[-1].posTopLeft[1]-self.topRooms[-1].y
                self.topRooms.append(nextRoom)

            if len(workingRoomsListCopy) != 0 and self.topRooms[-1].posTopLeft[0] + 7< self.x:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.rotate()
                print(nextRoom.x)
                print(nextRoom.y)
                nextRoom.posTopLeft[0] = self.topRooms[-1].posTopLeft[0] + self.topRooms[-1].x
                nextRoom.posTopLeft[1] = self.y
                self.topRooms.append(nextRoom)
            
            while len(workingRoomsListCopy) != 0 and self.topRooms[-1].posTopLeft[0] + 6< self.x:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.posTopLeft[0] = self.topRooms[-1].posTopLeft[0] + self.topRooms[-1].x
                nextRoom.posTopLeft[1] = self.y
                
                self.topRooms.append(nextRoom)
            
            while len(workingRoomsListCopy) != 0 and self.rightRooms[-1].posTopLeft[1] >7:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.rotate()
                nextRoom.posTopLeft[1] = self.rightRooms[-1].posTopLeft[1] - self.rightRooms[-1].y
                nextRoom.posTopLeft[0] = self.x-3
                
                self.rightRooms.append(nextRoom)
            print(self.bottomRooms[-1].posTopLeft[0] + 3)
            print(self.x)
            
            while len(workingRoomsListCopy) != 0 and self.bottomRooms[-1].posTopLeft[0] + 5< self.x:
                print("Hello")
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.posTopLeft[0] = self.bottomRooms[-1].posTopLeft[0] + self.bottomRooms[-1].x
                nextRoom.posTopLeft[1] = 3
                
                self.bottomRooms.append(nextRoom)
            self.leftRooms[-1].posTopLeft[1] = self.get
            while len(workingRoomsListCopy) != 0 and self.leftRooms[-1].posTopLeft[1] >7:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.rotate()
                nextRoom.posTopLeft[1] = self.rightRooms[-1].posTopLeft[1] - self.rightRooms[-1].y
                nextRoom.posTopLeft[0] = self.x-3
                
                self.rightRooms.append(nextRoom)
            


bygningTest = building(15,15)
for i in bygningTest.bottomRooms:
    print(i.id)
    print(i.posTopLeft)
    

"""
def checkHowToRotate(room, listOfRooms):
    i = -1
    while listOfRooms[i].posTopLeft[1] <= room.y:
        i-=1
    if listOfRooms[i].posTopLeft[1] + room.y:
        room.rotate()
    if listOfRooms[i].posTopLeft[1] + room.y and :
        
        
"""
        
class room:
    def __init__(self, typ, x, y):
        self.x = int(min(x,y))
        self.y = int(max(x,y))
        self.size = int(x)*int(y)           
        self.typ = typ
        self.space = {
            "r" : int(y),
            "l" : int(y),
            "t" : int(x),
            "b" : int(x)
        }
        self.posTopLeft = [0,0]

bygg = list(input("Hvor stort er bygget deres?(x,y) ").split(","))
bygg[0] = int(bygg[0])
bygg[1] = int(bygg[1])
bygning = building(bygg[0],bygg[1])
print(bygg)
while True:
    rom = list(input("Skriv type rom, (type, x, y, antall), for stopp skriv 0 ").split(","))
    for i in range(1,len(rom)):
        rom[i] = int(rom[i])
    print(rom)
    if rom[0] == "0":
        break
    rom1 = room(rom[0],rom[1],rom[2])
    
    if rom1.typ not in bygning.types:
        print(f"ikke akseptabel type")
        continue
    
    bygning.addRoom(rom1)
    
    for i in range(1,rom[3]):
        romx = room(rom[0],rom[1],rom[2])
        bygning.addRoom(romx)



workspaces = bygning.getTypes("w")
meetrooms = bygning.getTypes("m")
openrooms = bygning.getTypes("o")
sortedRooms = bygning.getRoomsSortedBySize()

room = room("w",0,0)
line1 = []
line1.append(room)

x_total = 0
for i in sortedRooms:
    x_total+= i.x

x_div_room_x = x_total/bygning.x

y_total = 0
for i in sortedRooms:
    y_total+= i.y
    
y_div_room_y = y_total/bygning.y



print("y div room " + str(y_div_room_y))
print("x div room " + str(x_div_room_x))

#while (sortedRooms[-1].size > workspaces[-1].size and sortedRooms[-1].size + sortedRooms[-1].posTopLeft[0] > sum(workspaces.x)/2):
    
line1.append(sortedRooms[-1])
while (bygning.x - (line1[-1].size + line1[-1].posTopLeft[0]) > sum(workspaces.x)/2 and bygning.x - (line1[-1].size + line1[-1].posTopLeft[0]-sortedRooms[-1])):
    line1.append(workspaces)
​
​
​
​

    
​
