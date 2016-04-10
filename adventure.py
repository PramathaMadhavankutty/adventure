from data import locations
from data import rooms

directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (1, 0),
}

position = (0, 0)
valid_directions = {}
accessories =[]
while True:
    location = locations[position]
    print("you are at the %s" % location)
    print("you can choose from these items %s" % rooms[location[0]])

    prompt = input("choose the items you need\n")
    chosen_item = prompt
    accessories = chosen_item
    print("your accessories : %s" % accessories)

    for k, v in directions.items():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_location:
            print('to the %s is a %s' % (k, possible_location[0]))
            valid_directions[k] = possible_position


    direction = input('which direction do you want to go?\n')
    new_position = valid_directions.get(direction)
    if new_position:
        position = new_position
    else:
        print("sorry, that isn't a valid direction")
