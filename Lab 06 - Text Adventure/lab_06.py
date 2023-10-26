class Room:
    def __init__(self, description = "", north = 0, east = 0, south = 0, west = 0):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description

def main():
    room_list = []
    current_room = 0

    room = Room("""You are in an entrance room, there is a door to the north""", 1, None, None, None)
    room_list.append(room)

    room = Room("""You are in the Dining Hall, there is a door to the east, south, and to the west""", None, 2, 0, 3)
    room_list.append(room)

    room = Room("""You are in the Kitchen, there is a door to the north and west""", 4, None, None, 1)
    room_list.append(room)

    room = Room("""You are in the Bathroom, there is a door to the north and east""", 9, 1, None, None)
    room_list.append(room)

    room = Room("""You are in the Master Bedroom, there is a door to the west and south""", None, None, 2, 5)
    room_list.append(room)

    room = Room("""You are in the Hallway, there is a door to the north, west, and east""", 6, 4, None, 9)
    room_list.append(room)

    room = Room("""You are in the Garden, there is a door to the east and south""", None, 7, 5, None)
    room_list.append(room)

    room = Room("""You are in the Gaming Room, there is a door to the north and west""", 10, None, None, 6)
    room_list.append(room)

    room = Room("""You are in the Closet, there is a door to the south""", None, None, 9, None)
    room_list.append(room)

    room = Room("""You are in the Guest Bedroom, there is a door to the north, east, and south""", 8, 5, 3, None)
    room_list.append(room)

    room = Room("""You Have Escaped!""", None, None, None, None)
    room_list.append(room)

    done=False

    while done == False:
        print(room_list[current_room].description)
        action = input("Where would you like to move?")
        print("")

        if action.lower() == "n" or action.lower() == "north":
            next_room = room_list[current_room].north
            if room_list[current_room].north == None:
                print("You cannot go that way!")
            else:
                current_room = room_list[current_room].north

        if action.lower() == "s" or action.lower() == "south":
            next_room = room_list[current_room].south
            if room_list[current_room].south == None:
                print("You cannot go this way!")
            else:
                current_room = room_list[current_room].south

        if action.lower() == "e" or action.lower() == "east":
            next_room = room_list[current_room].east
            if room_list[current_room].east == None:
                print("You cannot go this way!")
            else:
                current_room = room_list[current_room].east

        if action.lower() == "w" or action.lower() == "west":
            next_room = room_list[current_room].west
            if room_list[current_room].west == None:
                print("You cannot go this way!")
            else:
                current_room = room_list[current_room].west

        if current_room == 10:
            print("You have escaped!")
            done=True



main()