# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508




def move_forward(traffic_light, pedestrian, cars_opposite):
    if traffic_light == 'Green' or traffic_light == 'Yellow' and pedestrian == False:
        return True
    else:
        return False

def stop(traffic_light, pedestrian, cars_opposite):
    if traffic_light == 'Red' or traffic_light == 'Yellow' and pedestrian == True:
        return True
    else:
        return False
    
def turn_left(traffic_light, pedestrian, cars_opposite):
    if traffic_light == 'Green' and cars_opposite == False and pedestrian == False:
        return True
    else:
        return False
    

print(turn_left('Green', False, True))
print(turn_left('Green', False, False))
print(turn_left('Red', False, True))
print(move_forward('Yellow', True, True))
