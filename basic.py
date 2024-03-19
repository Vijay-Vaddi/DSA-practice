def solution(directions):

    '''
    assuming the robot is facing north and at postion (0,0)
    R command turns the direction N to east, and so on, 
    R-> {N to E, E to S, S to W, W to N}
    Likewise 
    L-> {N to W, W to S, S to E, E to N }
    this can be saved in a dict for direction tracking.
    '''
    x=0
    y=0
    direction = 'N'
    r_turn = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}
    l_turn = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}
    
    for command in directions:
        if command == 'R':
            direction= r_turn[direction]
        elif command == 'L':
            direction= r_turn[direction]
        elif command == 'F':
            # #move the robot in the direction
            if direction == 'N':
                y+=1
            elif direction == 'S':
                y-=1
            elif direction == 'E':
                x+=1
            elif direction == 'W':
                x-=1
    #the robot is already at the origin
    if (abs(x)+abs(y)) == 0:
        return 0
        
    #to calculate quadrant the robot in. 
    if x ==0 or y ==0:
        if y>0:
            quadrant = 3
        elif y<0:
            quadrant = 1
        elif x>0:
            quadrant = 2
        else:
            quadrant = 0
    
    print(quadrant)
    


    #to calculate the number of direction turns needed to face back
    # if 'NESW'.index(direction) < 'NESW'.index('N'): 
    #     num_of_turns = ('NESW'.index('N') - 'NESW'.index(direction)) % 4
    # else:
    #     num_of_turns = (4 + ('NESW'.index(direction) - 'NESW'.index('N'))) % 4     
    
    # return (abs(x)+abs(y)) + num_of_turns

print(solution('RFR'))