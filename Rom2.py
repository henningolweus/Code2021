class rooms:
  def __init__(self, type, width, height):
    self.type = type
    self.width = width
    self.height = height

def make_floor(x, y): # lager et tomt areal
    floor = []
    for i in range(x + 1):
        if i > 0:
            floor.append(row)
        row = []
        for j in range(y + 1):
            row.append('[ ]')
    floor.append(row)
    return floor

def print_floor(floor): #printer nåværende areal
    for i in range(len(floor)):
        print(*floor[i])

def occupy_floor(floor, type, x, len_x, y, len_y): #lager et rom med nederst venstre hjørne i (x, y)
    for i in range(y - 1 , y + len_y - 1):
        for j in range(x - 1 , x + len_x - 1):
            floor[-i - 1][j] = f"[{type.upper()}]"
    return floor

def get_rooms():
    rooms = []
    room = ['.']
    while room != '0':
        room = input("Angi romspesifikasjoner (type,lengde,bredde): ")
        if room == '0':
            break
        room = room.split(',')
        room[1] = int(room[1])
        room[2] = int(room[2])
        rooms.append(room)
    return rooms

def main():
    gulv = make_floor(20, 20)
    rooms = get_rooms()
    for i in range(len(rooms)):
        gulv = occupy_floor(gulv, rooms[i][0], 1, rooms[i][1], (i * 2 + 1), rooms[i][2])
    print_floor(gulv)

main()










