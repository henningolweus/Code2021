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
        """
        if len(self.workingRoomsList) > getMaxWorkRooms():
            for i in range(len(self.workingRooms)-2, self.getMaxWorkRooms()):
                workingRooms.pop()
        """
    def getMaxWorkRooms(self):
        return int(self.x*1/2)*2 + int((self.y-8)/2)*2
    
    def getMinYFromListOfRooms(self,listOfRooms):
        mini = math.inf
        for i in listOfRooms:
            if mini > i.posTopLeft[1]-i.y:
                mini = i.posTopLeft[1]-i.y
        return mini
            
    
    
    def removeE(self, listOfRooms):
        for i in listOfRooms:
            if i.id == "e":
                listOfRooms.remove(i)
    
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
                nextRoom.posTopLeft[0] = self.topRooms[-1].posTopLeft[0] + self.topRooms[-1].x
                nextRoom.posTopLeft[1] = self.y
                self.topRooms.append(nextRoom)
            
            while len(workingRoomsListCopy) != 0 and self.topRooms[-1].posTopLeft[0] + 8< self.x:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.posTopLeft[0] = self.topRooms[-1].posTopLeft[0] + self.topRooms[-1].x
                nextRoom.posTopLeft[1] = self.y
                
                self.topRooms.append(nextRoom)
            
            if (self.x%2 == 0) and len(workingRoomsListCopy) >=2:
                while len(workingRoomsListCopy) != 0 and self.bottomRooms[-1].posTopLeft[0] +2< self.x:
                    nextRoom = workingRoomsListCopy.pop()
                    nextRoom.posTopLeft[0] = self.bottomRooms[-1].posTopLeft[0] + self.bottomRooms[-1].x
                    nextRoom.posTopLeft[1] = 3
                    
                    self.bottomRooms.append(nextRoom)
            
            
            elif (self.x%2 == 1) and len(workingRoomsListCopy) >=2:
                while len(workingRoomsListCopy) != 0 and self.bottomRooms[-1].posTopLeft[0] +3< self.x:
                    nextRoom = workingRoomsListCopy.pop()
                    nextRoom.posTopLeft[0] = self.bottomRooms[-1].posTopLeft[0] + self.bottomRooms[-1].x
                    nextRoom.posTopLeft[1] = 3
                    
                    self.bottomRooms.append(nextRoom)
                    
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.posTopLeft[0] = self.bottomRooms[-1].posTopLeft[0] + self.bottomRooms[-1].x
                nextRoom.posTopLeft[1] = 3
                self.bottomRooms.append(nextRoom)
            
            
            while len(workingRoomsListCopy) != 0 and self.rightRooms[-1].posTopLeft[1] >7:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.rotate()
                nextRoom.posTopLeft[1] = self.rightRooms[-1].posTopLeft[1] - self.rightRooms[-1].y
                nextRoom.posTopLeft[0] = self.x-3
                
                self.rightRooms.append(nextRoom)
            
                    
                    
            self.leftRooms[-1].posTopLeft[1] = self.getMinYFromListOfRooms(self.topRooms)
            
            while len(workingRoomsListCopy) != 0 and self.leftRooms[-1].posTopLeft[1] >7:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.rotate()
                nextRoom.posTopLeft[1] = self.leftRooms[-1].posTopLeft[1] - self.leftRooms[-1].y
                nextRoom.posTopLeft[0] = self.x-3
                
                self.leftRooms.append(nextRoom)
            
            self.removeE(self.topRooms)
            self.removeE(self.bottomRooms)
            self.removeE(self.rightRooms)
            self.removeE(self.leftRooms)
                


bygningTest = building(16,16)
for i in bygningTest.topRooms:
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
 




        
        


