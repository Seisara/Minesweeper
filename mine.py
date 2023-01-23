size=input('Enter Grid size')

grid_blank=[
]
line=[
]

for i in range(0,int(size)):
    line.append(0)
    grid_blank.append(line)

grid=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,9,9,9,0,0,0],
    [0,0,9,0,9,0,9,0,0,0],
    [0,0,0,0,0,9,9,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,9,0,0,0,0],
    [0,9,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,9,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

game = True
while game==True:
    for i in range(len(grid)):
        print(grid_blank[i])
    cords=input('Enter coordinates(x,y): ')
    coords=cords.split(',')

    x=int(coords[0])
    y=int(coords[1])
    if grid[x][y]==9:
        print('game over')
        game==False
        break
    else:
        # for x1 in range(len(grid)) :
        #     for y1 in range(len(grid[x])):
        if (grid[x][y+1] == 9):
            print('bellow')
            grid_blank[x][y]+=1 #below
        if grid[x][y-1] == 9:
            print('above')
            grid_blank[x][y]+=1 #above
        if  grid[x+1][y] == 9:
            print('right')
            grid_blank[x][y]+=1 #right
        if  grid[x-1][y] == 9:
            print('left')
            grid_blank[x][y]+=1 #left
        if  grid[x+1][y-1] == 9:
            print('top right')
            grid_blank[x][y]+=1 #top right
        if  grid[x+1][y+1] == 9:
            print('bottom right')
            grid_blank[x][y]+=1 #bottom right
        if  grid[x-1][y+1] == 9:
            print('bottom left')
            grid_blank[x][y]+=1 #bottom left
        if  grid[x-1][y-1] == 9:
            print('top left')
            grid_blank[x][y]+=1 #top left            
    for i in range(len(grid)):
        print(grid_blank[i])

    while type(y)!=int or type(x)!=int or int(y)>len(grid):
        cords=input('Enter coordinates again(x,y): ')
        coords=cords.split(',')
        if len(coords)==2 and int(coords[0])<len(grid):
            break
        
    