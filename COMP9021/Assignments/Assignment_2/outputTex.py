

maze1 = [['1', '0', '2', '2', '1', '2', '3', '0'], ['3', '2', '2', '1', '2', '0', '2', '2'], ['3', '0', '1', '1', '3', '1', '0', '0'], ['2', '0', '3', '0', '0', '1', '2', '0'],
        ['3', '2', '2', '0', '1', '2', '3', '2'], ['1', '0', '0', '1', '1', '0', '0', '0']]

maze2 = [['0', '2', '2', '3', '0', '2', '1', '2', '0', '2', '2', '2'], ['2', '2', '2', '2', '2', '3', '1', '1', '1', '0', '3', '2'], ['3', '0', '1', '3', '2', '2', '1', '3', '0', '3', '0', '2'],
        ['3', '1', '2', '3', '2', '2', '2', '3', '2', '3', '3', '0'], ['0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0']]


maze3 = [['3', '1', '1', '1', '1', '1', '1', '1', '1', '3', '2'], ['2', '1', '1', '2', '2', '1', '3', '1', '2', '0', '2'], ['3', '3', '0', '2', '3', '0', '2', '2', '1', '1', '2'], ['2', '0', '3', '1', '0', '2', '1', '3', '1', '2', '2'], ['3', '1', '0', '1', '1', '1', '2', '0', '2', '0', '2'], ['2', '1', '2', '3', '0', '2', '3', '0', '1', '1', '2'], ['3', '0', '2', '2', '3', '0', '3', '1', '3', '0', '2'], ['0', '3', '1', '2', '2', '1', '2', '1', '2', '1', '2'], ['2', '2', '2', '0', '3', '1', '1', '0', '3', '2', '2'],
        ['2', '2', '1', '1', '0', '3', '1', '1', '0', '0', '2'], ['1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0']]


maze = maze2

final_walls = ""
final_Pillars = ""
final_red_cross = ""
final_path = ""

N = len(maze[0])    # row length
M = len(maze)       # col length
hor_lines = []
ver_lines = []
pillars = []
red_cross = []

class space:
    def __init__(self, value = 0, N_wall = 0, S_wall = 0, W_wall = 0, E_wall = 0):
        self.value = value
        self.N_wall = N_wall
        self.S_wall = S_wall
        self.W_wall = W_wall
        self.E_wall = E_wall

#mazePath = [[0]*(N-1) for _ in range(M - 1)]

pathObject = []
for i in range(M-1):
    temp = []
    for j in range(N-1):
        temp.append(space())
    pathObject.append(temp)

""" find how many access to the space
0 to toal clock space
1 to one acesss
4 to max access
"""

def DisplayList(a):
    for row in a:
        for col in row:
            print(col, end = ' ')
        print()


        
def DefineSpaceObject():
    for i in range(M-1):
        for j in range(N-1):
            val_1 = maze[i][j]
            val_2 = maze[i][j + 1]
            val_3 = maze[i + 1][j]

            if val_1 == '0':
                if val_2 == '0' or val_2 == '1':
                    if val_3 == '0' or val_3 == '2':
                        pathObject[i][j].value = 4                      
                        continue
                    if val_3 == '1' or val_3 == '3':
                        pathObject[i][j].value = 3
                        pathObject[i][j].S_wall = 1
                        continue
                    
                if val_2 == '2' or val_2 == '3':
                    pathObject[i][j].E_wall = 1
                    if val_3 == '0' or val_3 == '2':
                        pathObject[i][j].value = 3
                        continue
                    if val_3 == '1' or val_3 == '3':
                        pathObject[i][j].value = 2
                        pathObject[i][j].S_wall = 1
                        continue

            if val_1 == '3':
                pathObject[i][j].N_wall = 1
                pathObject[i][j].W_wall = 1
                if val_2 == '0' or val_2 == '1':
                    if val_3 == '0' or val_3 == '2':
                        pathObject[i][j].value = 2
                        continue
                    if val_3 == '1' or val_3 == '3':
                        pathObject[i][j].value = 1
                        pathObject[i][j].S_wall = 1
                        continue
                if val_2 == '2' or val_2 == '3':
                    if val_3 == '0' or val_3 == '2':
                        pathObject[i][j].value = 1
                        pathObject[i][j].E_wall = 1
                        continue
                    if val_3 == '1' or val_3 == '3':
                        pathObject[i][j].value = 0
                        pathObject[i][j].S_wall = 1
                        pathObject[i][j].E_wall = 1
                        continue

            if val_1 == '1' or val_1 == '2':
                if val_1 == '1':
                    pathObject[i][j].N_wall = 1
                else:
                    pathObject[i][j].W_wall = 1
                if val_2 == '0' or val_2 == '1':
                    if val_3 == '0' or val_3 == '2':
                        pathObject[i][j].value = 3
                        continue
                    if val_3 == '1' or val_3 == '3':
                        pathObject[i][j].value = 2
                        pathObject[i][j].S_wall = 1
                        continue
                if val_2 == '2' or val_2 == '3':
                    if val_3 == '0' or val_3 == '2':
                        pathObject[i][j].value = 2
                        pathObject[i][j].E_wall = 1
                        continue
                    if val_3 == '1' or val_3 == '3':
                        pathObject[i][j].value = 1
                        pathObject[i][j].S_wall = 1
                        pathObject[i][j].E_wall = 1
                 

              
               

"""
build walls
"""
def FindEndPoint_hor(i, j):
    val = maze[i][j]
    if val == '0' or val == '2':
        return j
    return FindEndPoint_hor(i, j + 1)

def FindEndPoint_ver(j, i):
    val = maze[j][i]
    if val == '0' or val == '1':
        return j
    return FindEndPoint_ver(j + 1, i)

# for all horizontal lines
for i in range(M):
    j = 0
    while j < N:
        
        val = maze[i][j]
        if val != '0' and val != '2':
            start_point = (j, i)
            j = FindEndPoint_hor(i, j+1)
            end_point = (j, i)            
            hor_lines.append([start_point,end_point])
        j += 1

# for all vertical lines
for i in range(N):
    j = 0
    while j < M:
        
        val = maze[j][i]
        if val != '0' and val != '1':
            start_point = (i, j)
            j = FindEndPoint_ver(j+1, i)
            end_point = (i, j)            
            ver_lines.append([start_point,end_point])
        j += 1

hor_lines.extend(ver_lines)

for i in hor_lines:
    txt = '    \draw ({},{}) -- ({},{});\n'.format(i[0][0], i[0][1], i[1][0], i[1][1])
    final_walls += txt
       
"""
 generate pillars
"""
for i in range(M):
    for j in range(N):
        val = maze[i][j]
        # only work for value '0'
        if val == '0':
            # check for first row
            if i == 0:
                #top left point
                if j == 0:
                    pillars.append((j, i))
                    continue
                # check left point if equal to 0 or 2
                left_val = maze[i][j-1]
                if left_val == '0' or left_val == '2':
                    pillars.append((j, i))
                    continue
            # check for first item below first low
            top_val = maze[i - 1][j]
            if j == 0:
                # check for one point above
                if top_val == '0' or top_val == '1':
                    pillars.append((j, i))
                    continue
            # check for rest point
            left_val = maze[i][j-1]
            if (top_val == '0' or top_val == '1') and (left_val == '0' or left_val == '2'):
                pillars.append((j, i))

for i in pillars:
    txt = '    \\fill[green] ({},{}) circle(0.2);\n'.format(i[0], i[1])
    final_Pillars += txt
                


# copy mazePath without reference
#cul_de_sacs = deepcopy(mazePath)
    

def MarkWay(i, j):
    space = pathObject[i][j]
    if space.value == 1:
        pathObject[i][j].value = -1
        # find gate
        if i == 0 or i == M-2:
            # for top line
            if i == 0:
                if space.S_wall == 0 and pathObject[i + 1][j].value > 0:
                    pathObject[i + 1][j].value -= 1
                    if pathObject[i + 1][j].value == 0:
                        pathObject[i][j].value = 0
                        return
                    
                    MarkWay(i + 1, j)
                    
                    if pathObject[i + 1][j].value == 0:
                        pathObject[i][j].value = 0
                        return
            # for bottom line
            else:
                if space.N_wall == 0 and pathObject[i - 1][j].value > 0:
                    pathObject[i - 1][j].value -= 1

                    if pathObject[i - 1][j].value == 0:
                        pathObject[i][j].value = 0
                        return
                    
                    MarkWay(i - 1, j)

                    if pathObject[i - 1][j].value == 0:
                        pathObject[i][j].value = 0
                        return
            # for left most point
            if j == 0:                
                if space.E_wall == 0 and pathObject[i][j + 1].value > 0:
                    pathObject[i][j + 1].value -= 1

                    if pathObject[i][j + 1].value == 0:
                        pathObject[i][j].value = 0
                        return
                    
                    MarkWay(i, j + 1)

                    if pathObject[i][j + 1].value == 0:
                        pathObject[i][j].value = 0
                        return
            # for right most point
            if j == N - 2:
                if space.W_wall == 0 and pathObject[i][j - 1].value > 0:
                    pathObject[i][j - 1].value -= 1

                    if pathObject[i][j - 1].value == 0:
                        pathObject[i][j].value = 0
                        return
                    MarkWay(i, j - 1)

                    if pathObject[i][j - 1].value == 0:
                        pathObject[i][j].value = 0
                        return
            # for left and right
            if space.E_wall == 0 and pathObject[i][j + 1].value > 0:
                
                
                pathObject[i][j + 1].value -= 1

                if pathObject[i][j + 1].value == 0:
                    pathObject[i][j].value = 0
                    return
                
                MarkWay(i, j + 1)

                if pathObject[i][j + 1].value == 0:
                    pathObject[i][j].value = 0
                    return
            if space.W_wall == 0 and pathObject[i][j - 1].value > 0:
                pathObject[i][j - 1].value -= 1

                if pathObject[i][j - 1].value == 0:
                    pathObject[i][j].value = 0
                    return
                MarkWay(i, j - 1)

                if pathObject[i][j - 1].value == 0:
                    pathObject[i][j].value = 0
                    return
            return
        
        # lines in between top and bottom lines
        # look for bottom line
        if space.S_wall == 0 and pathObject[i + 1][j].value > 0:
            pathObject[i + 1][j].value -= 1

            if pathObject[i + 1][j].value == 0:
                pathObject[i][j].value = 0
                return
            MarkWay(i + 1, j)

            if pathObject[i + 1][j].value == 0:
                pathObject[i][j].value = 0
                return
                
        # look for top line
        if space.N_wall == 0 and pathObject[i - 1][j].value > 0:
            pathObject[i - 1][j].value -= 1

            if pathObject[i - 1][j].value == 0:
                pathObject[i][j].value = 0
                return
            
            MarkWay(i - 1, j)

            if pathObject[i - 1][j].value == 0:
                pathObject[i][j].value = 0
                return

        # for left most point
        if j == 0:
            if space.E_wall == 0 and pathObject[i][j + 1].value > 0:
                pathObject[i][j + 1].value -= 1

                if pathObject[i][j + 1].value == 0:
                    pathObject[i][j].value = 0
                    return
                MarkWay(i, j + 1)

                if pathObject[i][j + 1].value == 0:
                    pathObject[i][j].value = 0
                    return
            return
        # for right most point
        if j == N - 2:
            if space.W_wall == 0 and pathObject[i][j - 1].value > 0:
                pathObject[i][j - 1].value -= 1

                if pathObject[i][j - 1].value == 0:
                    pathObject[i][j].value = 0
                    return
                MarkWay(i, j - 1)

                if pathObject[i][j - 1].value == 0:
                    pathObject[i][j].value = 0
                    return
            return
        # rest of point in middle
        if space.E_wall == 0 and pathObject[i][j + 1].value > 0:
            pathObject[i][j + 1].value -= 1

            if pathObject[i][j + 1].value == 0:
                pathObject[i][j].value = 0
                return
            
            MarkWay(i, j + 1)

            if pathObject[i][j + 1].value == 0:
                pathObject[i][j].value = 0
                return
        if space.W_wall == 0 and pathObject[i][j - 1].value > 0:
            pathObject[i][j - 1].value -= 1

            if pathObject[i][j - 1].value == 0:
                pathObject[i][j].value = 0
                return
            
            MarkWay(i, j - 1)

            if pathObject[i][j - 1].value == 0:
                pathObject[i][j].value = 0
                return
        return



def FindWay():
    for i in range(M-1):
        for j in range(N-1):
            MarkWay(i, j)
            
# cul-de-sacs
"""
DefineSapce()
DisplayList(mazePath)
"""
space_val = [[0]*(N-1) for _ in range(M-1)]

DefineSpaceObject()
for i in range(M-1):
    for j in range(N-1):
        space_val[i][j] = pathObject[i][j].value
print('Oject path')
DisplayList(space_val)



FindWay()
for i in range(M-1):
    for j in range(N-1):
        space_val[i][j] = pathObject[i][j].value
print('Oject path')
DisplayList(space_val)

for i in range(M-1):
    for j in range(N-1):
        if pathObject[i][j].value == -1:
            red_cross.append((j+0.5, i+0.5))
        
for i in red_cross:
    txt = '    \\node at ({},{}) {{}};\n'.format(i[0], i[1])
    final_red_cross += txt

#find path

            


            
def MarkEntryExit():
    for i in range(M-1):
        for j in range(N-1):
            #find entry point
            space = pathObject[i][j]
            if space.value == 2:
                if i == 0:
                    if not space.N_wall:
                        space.value = -2
                if i == M-2:
                    if not space.S_wall:
                        space.value = -2
                if j == 0:
                    if not space.W_wall:
                        space.value = -2
                if j == N-2:
                    if not space.E_wall:
                        space.value = -2

MarkEntryExit()

for i in range(M-1):
    for j in range(N-1):
        space_val[i][j] = pathObject[i][j].value
print('Entry Exit')
DisplayList(space_val)

entryPoint = []

for i in range(M-1):
    for j in range(N-1):
        if pathObject[i][j].value == -2:
            entryPoint.append((j, i))

def MovingDirection(i, j):
    space = pathObject[i][j]
    if i == 0:
        # check for S site
        if space.S_wall == 0 and abs(pathObject[i + 1][j].value) == 2:
            return i + 1, j
        
        if j == 0:
            if space.E_wall == 0 and abs(pathObject[i][j + 1].value) == 2:
                return i, j+1
            return i, j # no moving
        if j == N - 2:
            if space.W_wall == 0 and abs(pathObject[i][j - 1].value) == 2:
                return i, j-1
            return i, j # no moving
        
        # check for left and right
        if space.E_wall == 0 and abs(pathObject[i][j + 1].value) == 2:
            return i, j+1
        
        if space.W_wall == 0 and abs(pathObject[i][j - 1].value) == 2:
            return i, j-1
        return i, j # no moving

    if i == M - 2:
        # check for N site
        if space.N_wall == 0 and abs(pathObject[i - 1][j].value) == 2:
            return i - 1, j
        
        if j == 0:
            if space.E_wall == 0 and abs(pathObject[i][j + 1].value) == 2:
                return i, j+1
            return i, j # no moving
        if j == N - 2:
            if space.W_wall == 0 and abs(pathObject[i][j - 1].value) == 2:
                return i, j-1
            return i, j # no moving
        # check for left and right
        if space.E_wall == 0 and abs(pathObject[i][j + 1].value) == 2:
            return i, j+1
        
        if space.W_wall == 0 and abs(pathObject[i][j - 1].value) == 2:
            return i, j-1
        return i, j # no moving

    # Top and below
    if space.N_wall == 0 and abs(pathObject[i - 1][j].value) == 2:
        return i - 1, j
    if space.S_wall == 0 and abs(pathObject[i + 1][j].value) == 2:
        return i + 1, j
    # left most line
    if j == 0:
        if space.E_wall == 0 and abs(pathObject[i][j + 1].value) == 2:
            return i, j+1
        return i, j # no moving
    # right most line
    if j == N - 2:
        if space.W_wall == 0 and abs(pathObject[i][j - 1].value) == 2:
            return i, j-1
        return i, j # no moving
    if space.E_wall == 0 and abs(pathObject[i][j + 1].value) == 2:
        return i, j+1
    if space.W_wall == 0 and abs(pathObject[i][j - 1].value) == 2:
        return i, j-1
    return i, j # no moving

final_hor_set_1 = []
final_ver_set_1 = []

yellowMaze = [[0]*(N+1) for _ in range(M+1)]

def DrawYellowPath(path):
    final_hor_set = []
    final_ver_set = []
    print('input path', path)
    size = len(path)
    for i in range(size):
        x = path[i][1] + 1        
        y = path[i][0] + 1

        # if entry or exit point
        if i == 0:
            if x == 1:
                yellowMaze[x-1][y] = 1
            if x == M - 1:
                yellowMaze[x+1][y] = -1
            if y == 1: 
                yellowMaze[x][y - 1] = 2
            if y == N - 1:
                yellowMaze[x][y + 1] = -2
        if i == size -1:
            if x == 1:
                yellowMaze[x-1][y] = -1
            if x == M - 1:
                yellowMaze[x+1][y] = 1
            if y == 1: 
                yellowMaze[x][y - 1] = -2
            if y == N - 1:
                yellowMaze[x][y + 1] = 2
        if i== size - 1:
            if y == 1: 
                yellowMaze[x][y] = -2
            if y == N - 1:
                yellowMaze[x][y] = 2
            if x == 1:
                yellowMaze[x][y] = -1
            if x == M - 1:
                yellowMaze[x][y] = 1
        # check for corners
        if pathObject[0][0].N_wall:
            yellowMaze[0][1] = 0
        if pathObject[0][0].W_wall:
            yellowMaze[1][0] = 0

        if pathObject[M-2][0].S_wall:
            yellowMaze[M][1] = 0
        if pathObject[M-2][0].W_wall:
            yellowMaze[M-1][0] = 0

        if pathObject[0][N-2].N_wall:
            yellowMaze[0][N-1] = 0
        if pathObject[0][N-2].E_wall:
            yellowMaze[1][N] = 0

        if pathObject[M-2][N-2].S_wall:
            yellowMaze[M][N-2] = 0
        if pathObject[M-2][N-2].E_wall:
            yellowMaze[M-1][N] = 0
            
            
        if i < size - 1:
            if x == path[i + 1][1] + 1:
                if y > path[i+1][0] + 1:
                    val = -2
                else:
                    val =2
                yellowMaze[x][y] = val
                continue
            if x > path[i+1][1] + 1:
                val = -1
            else:
                val = 1
            yellowMaze[x][y] = val

    print('yellowMze')
    DisplayList(yellowMaze)
    # store horizontal path
    for i in range(M + 1):
        j = 0
        while j < N + 1:
            if yellowMaze[i][j] == 2:
                if j == N:
                    final_hor_set.append([(j-1.5, i-0.5)])
                else:
                    final_hor_set.append([(j-0.5, i-0.5)])
                j += 1
                while j < N + 1 and yellowMaze[i][j] == 2:
                    j += 1
                final_hor_set[-1].append([j - 0.5, i - 0.5])
            """
            if j == 0 and yellowMaze[i][j] == -2:
                final_hor_set.append([(j-1.5, i-0.5)])
                j += 1
                final_hor_set[-1].append([j - 0.5, i - 0.5])
            
            if j > 0 and j < N+ 1 and yellowMaze[i][j] == -2:
                final_hor_set.append([(j-1.5, i-0.5)])
                j += 1
                while j < N+ 1 and yellowMaze[i][j] == -2:
                    j += 1
                final_hor_set[-1].append([j - 1.5, i - 0.5])

                
            """

            if j < N+ 1 and yellowMaze[i][j] == -2:
                final_hor_set.append([(j-1.5, i-0.5)])
                if j==0:
                    j += 1
                    while j < N+ 1 and yellowMaze[i][j] == -2:
                        j += 1
                    final_hor_set[-1].append([j - 0.5, i - 0.5])
                else:
                    j += 1
                    while j < N+ 1 and yellowMaze[i][j] == -2:
                        j += 1
                    final_hor_set[-1].append([j - 1.5, i - 0.5])
            j += 1
    
    #print('final_hor_set',final_hor_set)
    # store verticle path
    for j in range(N + 1):
        i = 0
        while i < M + 1:
            if yellowMaze[i][j] == 1:
                
                final_ver_set.append([(j-0.5, i - 0.5)])
                i += 1
                while i < M + 1 and yellowMaze[i][j] == 1:
                    i += 1
                final_ver_set[-1].append([j - 0.5, i - 0.5])

            if i < M+ 1 and yellowMaze[i][j] == -1:
                
                final_ver_set.append([(j-0.5, i-1.5)])
                i += 1
                while i < M+ 1 and yellowMaze[i][j] == -1:
                    i += 1
                final_ver_set[-1].append([j - 0.5, i - 1.5])
                
            i += 1
    global final_hor_set_1
    final_hor_set_1 = final_ver_set
    final_hor_set.extend(final_ver_set)
    print('final_ver_set',final_ver_set)
    final_path = ''
    for i in final_hor_set:
        a = i[0][0]
        b = i[0][1]
        c = i[1][0]
        d = i[1][1]
        if a < -0.5:
            a = -0.5
        if a > N:
            a -= 1
            
        if b < -0.5:
            b = -0.5
        if b > M:
            b -= 1
            
        if c < -0.5:
            c = -0.5
        if c > N:
            c -= 1
        
        if d < -0.5:
            d = -0.5
        if d > M:
            d -= 1
        
        txt = '    \draw[dashed, yellow] ({},{}) -- ({},{});\n'.format(a,b,c,d)
        final_path += txt

    print(final_path)
    
    """
    for j in range(N + 1):
        i = 0
        while i < M + 1:
            if yellowMaze[i][j] == 1:
                if i < M + 1 and abs(yellowMaze[i-1][j]) == 2:
                    i -= 1
                final_ver_set.append([(j-0.5, i-0.5)])
                i += 1
                while i < M + 1 and yellowMaze[i][j] == 1:
                    i += 1
                if i < M + 1 and (yellowMaze[i][j] == 0 or abs(yellowMaze[i - 2][j]) == 2):
                    i -= 1
                # 1 at last row
                if i == M + 1 and yellowMaze[i-1][j] == 1:
                    i -= 1
                final_ver_set[-1].append([j - 0.5, i - 0.5])
                
            i += 1
    
    print('final_ver_set',final_ver_set)
    """
        
"""
def DrawYellowPath(path):
    hor_set = []
    ver_set = []
    if len(path) > 1:
        
        # for horizontal lines
        pre_hor = path[0][0]
        pre_ver = path[0][1]
        hor_gap = 0
        
        for i in path:
            hor_now = i[0]
            ver_now = i[1]               
            if pre_ver == ver_now and pre_hor != hor_now:
                if hor_gap == 0:
                    hor_set.append([(pre_hor + 0.5, pre_ver + 0.5)])
                hor_gap = (hor_now - pre_hor)
                if i != path[-1]:
                    continue
            pre_ver = ver_now
            pre_hor = hor_now
            if hor_gap != 0:
                y = hor_set[-1][0][0]
                x = hor_set[-1][0][1]
                hor_set[-1].append((y + hor_gap,x))
            hor_gap = 0

        # for vertical lines
        pre_hor = path[0][0]
        pre_ver = path[0][1]
        ver_gap = 0
        
        for i in path:
            hor_now = i[0]
            ver_now = i[1]               
            if pre_ver != ver_now and pre_hor == hor_now:
                if ver_gap == 0:
                    ver_set.append([(pre_hor + 0.5, pre_ver + 0.5)])
                ver_gap = (ver_now - pre_ver)
                if i != path[-1]:
                    continue
            pre_ver = ver_now
            pre_hor = hor_now
            if ver_gap != 0:
                y = ver_set[-1][0][0]
                x = ver_set[-1][0][1]
                check_x = x+ver_gap
                ver_set[-1].append((y,x+ver_gap))
            ver_gap = 0

        # add entry length and exit lenth
        print('H:', hor_set)
        print('V:', ver_set)

        if hor_set:
            for i in hor_set:
                
                print('print',i)

        if ver_set:
            ver_size = len(ver_set)
            for i in range(ver_size):
                start_point = ver_set[i][0]
                end_point = ver_set[i][1]
                if start_point[1] == 0.5:
                    print(ver_set[i][0][1])
                    ver_set[i][0][1] = -0.5
                if end_point[1] == M - 1.5:
                    ver_set[i][1][1] += 1
                    
                print('print',i)
"""        

        

allPath = []
def YellowPath(temp, i, j):
    a, b = MovingDirection(i, j)
    
    if not (a == i and b == j):
        temp.append((b, a))
        pathObject[a][b].value = -3
        YellowPath(temp, a, b)
        
    return temp


def FindYellowPath():
    for i in range(M-1):
        for j in range(N-1):
            #find entry point
            space = pathObject[i][j]
            if space.value == -2:
                tempPath = []
                space.value = -3    #update to visited value
                startPoint = (j, i)
                tempPath.append((j, i))               
                allPath.append(YellowPath(tempPath, i, j))
    for i in allPath:
        if len(i) > 1:
            if i[-1] in entryPoint:
                #print('road', i)
                DrawYellowPath(i)
            continue
        # check for corner points
        x = i[0][1]
        y = i[0][0]
        space = pathObject[x][y]
        if x == 0 and y == 0:
            if space.N_wall == 0 and space.W_wall == 0:
                DrawYellowPath(i)
            continue
        if x == 0 and y == N - 2:
            if space.N_wall == 0 and space.E_wall == 0:
                DrawYellowPath(i)
            continue
        if x == M - 2 and y == 0:
            if space.S_wall == 0 and space.W_wall == 0:
                DrawYellowPath(i)
            continue
        if x == M - 2 and y == N - 2:
            if space.S_wall == 0 and space.E_wall == 0:
                DrawYellowPath(i)
        


FindYellowPath()

content = r"""\documentclass[10pt]{{article}}
\usepackage{{tikz}}
\usetikzlibrary{{shapes.misc}}
\usepackage[margin=0cm]{{geometry}}
\pagestyle{{empty}}
\tikzstyle{{every node}}=[cross out, draw, red]

\begin{{document}}

\vspace*{{\fill}}
\begin{{center}}
\begin{{tikzpicture}}[x=0.5cm, y=-0.5cm, ultra thick, blue]
% Walls
{0}% Pillars
{1}% Inner points in accessible cul-de-sacs
{2}% Entry-exit paths without intersections
{3}
\end{{tikzpicture}}
\end{{center}}
\vspace*{{\fill}}

\end{{document}}""".format(final_walls, final_Pillars, final_red_cross,'d')
content = content.encode('utf-8')



with open('cover2.tex','wb') as f:
    f.write(content)



"""


def DefineSapce():
    for i in range(M-1):
        for j in range(N-1):
            val_1 = maze[i][j]
            val_2 = maze[i][j + 1]
            val_3 = maze[i + 1][j]

            if val_1 == '0':
                if val_2 == '0' or val_2 == '1':
                    if val_3 == '0' or val_3 == '2':
                        mazePath[i][j] = 4
                        continue
                    if val_3 == '1' or val_3 == '3':
                        mazePath[i][j] = 3
                        continue
                if val_2 == '2' or val_2 == '3':
                    if val_3 == '0' or val_3 == '2':
                        mazePath[i][j] = 3
                        continue
                    if val_3 == '1' or val_3 == '3':
                        mazePath[i][j] = 2
                        continue
                    
            if val_1 == '1' or val_1 == '2':
                if val_2 == '0' or val_2 == '1':
                    if val_3 == '0' or val_3 == '2':
                        mazePath[i][j] = 3
                        continue
                    if val_3 == '1' or val_3 == '3':
                        mazePath[i][j] = 2
                        continue
                if val_2 == '2' or val_2 == '3':
                    if val_3 == '0' or val_3 == '2':
                        mazePath[i][j] = 2
                        continue
                    if val_3 == '1' or val_3 == '3':
                        mazePath[i][j] = 1
                        continue

            if val_1 == '3':
                if val_2 == '0' or val_2 == '1':
                    if val_3 == '0' or val_3 == '2':
                        mazePath[i][j] = 2
                        continue
                    if val_3 == '1' or val_3 == '3':
                        mazePath[i][j] = 1
                        continue
                if val_2 == '2' or val_2 == '3':
                    if val_3 == '0' or val_3 == '2':
                        mazePath[i][j] = 1
                        continue
                    if val_3 == '1' or val_3 == '3':
                        mazePath[i][j] = 0                   
"""  
