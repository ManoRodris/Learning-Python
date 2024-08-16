# Hurdle 3
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def jump_2():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == False:
    if front_is_clear() == False:
        jump_2()
    else:
        move()
'''

# Hurdle 4
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while front_is_clear() and wall_on_right():
        move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        move()
    while wall_on_right() and front_is_clear():
        move()
    if wall_on_right() and wall_in_front():
        turn_left()
    
    
while at_goal() == False:
    if wall_in_front():
        jump()
    else:
        move()
'''