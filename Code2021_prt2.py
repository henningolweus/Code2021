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
        self.x = 3
        self.y = 4
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
        
        # creating five arrays, each representing a different edge in the room, or the middle of the room. 
        self.topRooms = []
        self.bottomRooms = []
        self.rightRooms = []
        self.leftRooms = []
        self.middleRooms = []
        self.size = x*y
        
        # We create three lists of different types of rooms, m1, m2 and w. 
        self.meetingRooms2List = []
        self.meetingRooms1List = []
        
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
        
        ammountOfMeetingRooms = int(len(self.workingRoomsList)/4)-2
        ammountOfMeetingRooms2 = ammountOfMeetingRooms//2
        
        if (ammountOfMeetingRooms2 <0):
            ammountOfMeetingRooms2=0
        ammountOfMeetingRooms1 = ammountOfMeetingRooms-2*ammountOfMeetingRooms2+2
    
        print(ammountOfMeetingRooms2)
        print(ammountOfMeetingRooms1)
        for i in range(0,ammountOfMeetingRooms1):
            self.meetingRooms1List.append(meetingRoom1())
        
        
        for i in range(0,ammountOfMeetingRooms2):
            self.meetingRooms2List.append(meetingRoom2())
            
        
        
        if len(self.workingRoomsList) >= self.getMaxWorkRooms():
            for i in range(self.getMaxWorkRooms()-2,len(self.workingRoomsList) ):
                self.workingRoomsList.pop()
                
                
    def getMaxWorkRooms(self):
        return int(self.x*1/2)*2 + int((self.y-8)/2)*2
    
    def getMinYFromListOfRooms(self,listOfRooms):
        mini = math.inf
        for i in listOfRooms:
            if mini > i.posTopLeft[1]-i.y:
                mini = i.posTopLeft[1]-i.y
        return mini
            
    def getAllRooms(self):
        return self.bottomRooms + self.topRooms + self.leftRooms + self.rightRooms + self.middleRooms
    
    def removeE(self, listOfRooms):
        for i in listOfRooms:
            if i.size == 0 or i.id == "e":
                listOfRooms.remove(i)
    
        
    def placeRooms(self):
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
                nextRoom.rotate()
                nextRoom.posTopLeft[0] = self.topRooms[-1].posTopLeft[0] + self.topRooms[-1].x
                nextRoom.posTopLeft[1] = self.y
                self.topRooms.append(nextRoom)
            
            while len(meetingRooms1ListCopy) != 0:
                nextRoom = meetingRooms1ListCopy.pop()
                nextRoom.rotate()
                nextRoom.posTopLeft[0] = self.topRooms[-1].posTopLeft[0]
                nextRoom.posTopLeft[1] = self.topRooms[-1].posTopLeft[1]-self.topRooms[-1].y
                self.topRooms.append(nextRoom)
            
            if (self.x%2 == 0) and len(workingRoomsListCopy) >=2:
                while len(workingRoomsListCopy) != 0 and self.bottomRooms[-1].posTopLeft[0] +2< self.x:
                    nextRoom = workingRoomsListCopy.pop()
                    nextRoom.posTopLeft[0] = self.bottomRooms[-1].posTopLeft[0] + self.bottomRooms[-1].x
                    nextRoom.posTopLeft[1] = 3
                    
                    self.bottomRooms.append(nextRoom)
        
        
            elif (self.x%2 == 1) and len(workingRoomsListCopy) >=2:
                while len(workingRoomsListCopy) != 0 and self.bottomRooms[-1].posTopLeft[0] +5< self.x:
                    nextRoom = workingRoomsListCopy.pop()
                    nextRoom.posTopLeft[0] = self.bottomRooms[-1].posTopLeft[0] + self.bottomRooms[-1].x
                    nextRoom.posTopLeft[1] = 3
                    
                    self.bottomRooms.append(nextRoom)
                
                if len(workingRoomsListCopy)!=0:
                    nextRoom = workingRoomsListCopy.pop()
                    nextRoom.posTopLeft[0] = self.bottomRooms[-1].posTopLeft[0] + self.bottomRooms[-1].x
                    nextRoom.posTopLeft[1] = 2
                    self.bottomRooms.append(nextRoom)
              
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
            
            
            #right
            while len(workingRoomsListCopy) != 0 and self.rightRooms[-1].posTopLeft[1] >7:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.rotate()
                nextRoom.posTopLeft[1] = self.rightRooms[-1].posTopLeft[1] - self.rightRooms[-1].y
                nextRoom.posTopLeft[0] = self.x-3
                
                self.rightRooms.append(nextRoom)
            
                    
                    
            self.leftRooms[-1].posTopLeft[1] = self.getMinYFromListOfRooms(self.topRooms)
            #left
            while len(workingRoomsListCopy) != 0 and self.leftRooms[-1].posTopLeft[1] >7:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.rotate()
                nextRoom.posTopLeft[1] = self.leftRooms[-1].posTopLeft[1] - self.leftRooms[-1].y
                nextRoom.posTopLeft[0] = 0
                
                self.leftRooms.append(nextRoom)
            
            self.removeE(self.topRooms)
            self.removeE(self.bottomRooms)
            self.removeE(self.rightRooms)
            self.removeE(self.leftRooms)
        
        else:
            self.placeRooms2()
    
    def placeRooms2(self):
        #initialize placing:
        meetingRooms2ListCopy = self.meetingRooms2List.copy()
        meetingRooms1ListCopy = self.meetingRooms1List.copy()
        workingRoomsListCopy = self.workingRoomsList.copy()
        
        self.topRooms.append(emptyRoom())
        self.topRooms[-1].posTopLeft[0] = 5
        self.topRooms[-1].posTopLeft[1] = self.y
        self.topRooms.append(emptyRoom())
        self.topRooms[-1].posTopLeft[0] = self.x-7
        self.topRooms[-1].posTopLeft[1] = self.y
        
        self.rightRooms.append(emptyRoom())
        self.rightRooms[-1].posTopLeft[0] = self.x-3
        self.rightRooms[-1].posTopLeft[1] = self.y
        self.bottomRooms.append(emptyRoom())
        self.bottomRooms[-1].posTopLeft[1] = 3
        self.leftRooms.append(emptyRoom())
        self.leftRooms[-1].posTopLeft[1] = self.y
        # bottom row, placed!
        """
        while len(workingRoomsListCopy) != 0 and self.topRooms[-1].posTopLeft[0] + 8< self.x:
            nextRoom = workingRoomsListCopy.pop()
            nextRoom.posTopLeft[0] = self.topRooms[-1].posTopLeft[0] + self.topRooms[-1].x
            nextRoom.posTopLeft[1] = self.y
            
            self.topRooms.append(nextRoom)
        """
        if (self.x%2 == 0) and len(workingRoomsListCopy) >=2:
            while len(workingRoomsListCopy) != 0 and self.bottomRooms[-1].posTopLeft[0] +2< self.x:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.posTopLeft[0] = self.bottomRooms[-1].posTopLeft[0] + self.bottomRooms[-1].x
                nextRoom.posTopLeft[1] = 3
                
                self.bottomRooms.append(nextRoom)
        
        
        elif (self.x%2 == 1) and len(workingRoomsListCopy) >=2:
            while len(workingRoomsListCopy) != 0 and self.bottomRooms[-1].posTopLeft[0] +5< self.x:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.posTopLeft[0] = self.bottomRooms[-1].posTopLeft[0] + self.bottomRooms[-1].x
                nextRoom.posTopLeft[1] = 3
                
                self.bottomRooms.append(nextRoom)
                
            nextRoom = workingRoomsListCopy.pop()
            nextRoom.posTopLeft[0] = self.bottomRooms[-1].posTopLeft[0] + self.bottomRooms[-1].x
            nextRoom.posTopLeft[1] = 2
            self.bottomRooms.append(nextRoom)
        
        # placing left then right
        
        while len(workingRoomsListCopy) != 0 and self.leftRooms[-1].posTopLeft[1] >7:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.rotate()
                nextRoom.posTopLeft[1] = self.leftRooms[-1].posTopLeft[1] - self.leftRooms[-1].y
                nextRoom.posTopLeft[0] = 0
                
                self.leftRooms.append(nextRoom)
        
        while len(workingRoomsListCopy) != 0 and self.rightRooms[-1].posTopLeft[1] >7:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.rotate()
                nextRoom.posTopLeft[1] = self.rightRooms[-1].posTopLeft[1] - self.rightRooms[-1].y
                nextRoom.posTopLeft[0] = self.x-3
                
                self.rightRooms.append(nextRoom)
                
                
       
        if len(workingRoomsListCopy) != 0 and self.y%2 == 1 and self.x%2 == 1:
            nextRoom = workingRoomsListCopy.pop()
            nextRoom.posTopLeft[1] = self.rightRooms[-1].posTopLeft[1] - self.rightRooms[-1].y
            nextRoom.posTopLeft[0] = self.x-2
            
            self.rightRooms.append(nextRoom)
        i = 0
        #top row
        while len(workingRoomsListCopy) > 0:
            i+=1
            if i%2 ==1:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.posTopLeft[1] = self.y
                nextRoom.posTopLeft[0] = self.topRooms[-2].posTopLeft[0] + self.topRooms[-2].x
                
                self.topRooms.append(nextRoom)
            
            if i%2 ==0:
                nextRoom = workingRoomsListCopy.pop()
                nextRoom.posTopLeft[1] = self.y
                nextRoom.posTopLeft[0] = self.topRooms[-2].posTopLeft[0] - self.topRooms[-2].x
                
                self.topRooms.append(nextRoom)
        
        avaliableSpace2 = self.x -3*2-2-4*2 -(len(self.topRooms)-3)*2   #her skal evt det ligge to møterom
        
        # checking if we can lay down two. 
        if (avaliableSpace2>=0):
            
            nextRoom = meetingRooms2ListCopy.pop()
            nextRoom.posTopLeft[1] = self.y
            nextRoom.posTopLeft[0] = int(self.x/2)-4
            self.middleRooms.append(nextRoom)
            
            if len(meetingRooms2ListCopy) ==0:
                nextRoom = workingRooms1ListCopy.pop()
                nextRoom.rotate()
                nextRoom.posTopLeft[1] = self.y
                nextRoom.posTopLeft[0] = int(self.x/2)
                self.middleRooms.append(nextRoom)
                
                if (len(workingRooms1ListCopy)>0):
                    nextRoom = workingRooms1ListCopy.pop()
                    nextRoom.rotate()
                    nextRoom.posTopLeft[1] = self.y-3
                    nextRoom.posTopLeft[0] = int(self.x/2)
                    self.middleRooms.append(nextRoom)
            else:
                nextRoom = meetingRooms2ListCopy.pop()
                nextRoom.posTopLeft[1] = self.y
                nextRoom.posTopLeft[0] = int(self.x/2)
                self.middleRooms.append(nextRoom)
        
       
        else:
            nextRoom = meetingRooms2ListCopy.pop()
            nextRoom.posTopLeft[1] = self.y
            nextRoom.posTopLeft[0] = int(self.x/2)-2
            self.middleRooms.append(nextRoom)
        
        
        
        i = 0
        if (len(meetingRooms2ListCopy)) >=2:
            i = 1
        x = 0
        # legger til alle meetingrooms2
        if i == 1:
            nextRoom = meetingRooms2ListCopy.pop()
            nextRoom.rotate()
            nextRoom.posTopLeft[0] = int(self.x/2)-6
            nextRoom.posTopLeft[1] = self.y-6
            self.middleRooms.append(nextRoom)
            nextRoom = meetingRooms2ListCopy.pop()
            nextRoom.rotate()
            nextRoom.posTopLeft[0] = int(self.x/2)
            nextRoom.posTopLeft[1] = self.y-6
            self.middleRooms.append(nextRoom)
        
        elif len(meetingRooms2ListCopy)!=0:
                nextRoom = meetingRooms2ListCopy.pop()
                nextRoom.rotate()
                nextRoom.posTopLeft[0] = int(self.x/2)-3
                nextRoom.posTopLeft[1] = self.y-6
                self.middleRooms.append(nextRoom)
        
        while (len(meetingRooms2ListCopy) != 0):
            x+=2
            if i == 1:
                while (len(meetingRooms2ListCopy) != 0):
                    nextRoom = meetingRooms2ListCopy.pop()
                    x+=2
                    if x%4 != 0:
                        nextRoom.rotate()
                        nextRoom.posTopLeft[1] = self.middleRooms[-1].posTopLeft[1]
                        nextRoom.posTopLeft[0] = int(self.x/2)
                        self.middleRooms.append(nextRoom)
                    else:
                        nextRoom.rotate()
                        nextRoom.posTopLeft[1] = self.middleRooms[-1].posTopLeft[1]-4
                        nextRoom.posTopLeft[0] = int(self.x/2)-6
                        self.middleRooms.append(nextRoom)
                    
            else: 
                if x%4 != 0:
                    nextRoom.rotate()
                    nextRoom.posTopLeft[1] = self.middleRooms[-1].posTopLeft[1]
                    nextRoom.posTopLeft[0] = int(self.x/2)
                    self.middleRooms.append(nextRoom)
                else:
                    nextRoom.rotate()
                    nextRoom.posTopLeft[1] = self.middleRooms[-1].posTopLeft[1]-4
                    nextRoom.posTopLeft[0] = int(self.x/2)-6
                    self.middleRooms.append(nextRoom)

        if i == 1: #Special Case, her er bredden lik 12
            while (len(meetingRooms1ListCopy) !=0):
                nextRoom = meetingRooms1ListCopy.pop()
                
                x+=1
                if x%4 !=0:
                    nextRoom.posTopLeft[1] = self.middleRooms[-1].posTopLeft[1]
                    nextRoom.posTopLeft[0] = self.middleRooms[-1].posTopLeft[0]+self.middleRooms[-1].x
                    self.middleRooms.append(nextRoom)
                
                else:
                    nextRoom.posTopLeft[1] = self.middleRooms[-1].posTopLeft[1]-4
                    nextRoom.posTopLeft[0] = int(self.x/2)
                    self.middleRooms.append(nextRoom)
                
        else:
            x = 1
            while (len(meetingRooms1ListCopy) !=0):
                nextRoom = meetingRooms1ListCopy.pop()
                
                x+=1
                if x%2 !=0:
                    nextRoom.posTopLeft[0] = self.middleRooms[-1].posTopLeft[0]+self.middleRooms[-1].x
                    
                    nextRoom.posTopLeft[1] = self.middleRooms[-1].posTopLeft[1]
                    
                    self.middleRooms.append(nextRoom)
                
                else:
                    nextRoom.posTopLeft[0] = int(self.x/2)-3
                    nextRoom.posTopLeft[1] = self.middleRooms[-1].posTopLeft[1]-self.middleRooms[-1].y
                    self.middleRooms.append(nextRoom)
                    
                    
        while (len(meetingRooms1ListCopy) !=0):
            nextRoom = meetingRooms1ListCopy.pop()
            
            x+=1
            if x%4 !=0:
                nextRoom.posTopLeft[1] = self.middleRooms[-1].posTopLeft[1]
                nextRoom.posTopLeft[0] = self.middleRooms[-1].posTopLeft[0]+self.middleRooms[-1].x
                self.middleRooms.append(nextRoom)
            
            else:
                nextRoom.posTopLeft[1] = self.middleRooms[-1].posTopLeft[1]-4
                nextRoom.posTopLeft[0] = int(self.x/2)-3*k
                self.middleRooms.append(nextRoom)
        
            
           
        self.removeE(self.topRooms)
        self.removeE(self.topRooms)
        self.removeE(self.bottomRooms)
        self.removeE(self.bottomRooms)
        self.removeE(self.rightRooms)
        self.removeE(self.rightRooms)
        self.removeE(self.leftRooms)
        self.removeE(self.leftRooms)
        
                
            
            
            
        
            
        
        

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
 
 
 




        
        


