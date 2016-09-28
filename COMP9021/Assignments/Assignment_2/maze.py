import os
import sys
import copy

if __name__ == "__main__":
    #sys.argv = ['maze.py', '-print', '--file', 'maze1.txt']
    sys.argv = ['maze.py', '--file', 'maze3.txt']


"""
initialisation
-----------------------------
"""

errMsg_1 = "I expect --file followed by filename and possibly -print as command line arguments."
errMsg_2 = "Incorrect input."

maze = []
maze_set = {'0', '1', '2', '3'}

maze_dim_min = 2
maze_width_max = 31
maze_height_max = 41

N = 0   # row length of maze
M = 0   # col length of maze

hor_lines = []
ver_lines = []
pillars = []
red_cross = []



final_walls = ""
final_Pillars = ""
final_red_cross = ""
final_path = ""


pathObject = []
entryPoint = []
final_path_set = []
allPath = []
yellowMaze =[]

# question 1
gates = 0
wallSet = 0
inaccess = 0
acc_area = 0
blocker = 0
path_num = 0

"""
Class and Functions
-----------------------------
"""

class space:
    def __init__(self, value = 0, N_wall = 0, S_wall = 0, W_wall = 0, E_wall = 0):
        self.value = value
        self.N_wall = N_wall
        self.S_wall = S_wall
        self.W_wall = W_wall
        self.E_wall = E_wall

def DisplayList(a):
    for row in a:
        for col in row:
            print(col, end = ' ')
        print()

def Check_file_content(f_Name):
	
    maze_collect = set()		# set to collect unique number of current file

    with open(f_Name, 'r') as f:
        # read each row
        for lines in f:
		
            row_list = []		# empty list to store new all digit in new row
            
            # read each char per row
            for d in lines.strip():
                # filter space and store value to list
                if d != ' ':
                    row_list.append(d)
            
            # filter empty rows
            if row_list:
                # collect and combine all unique char
                maze_collect = maze_collect.union(row_list)
                # check if collection is the sub set of the defined char set
                if not (maze_collect <= maze_set):
                    print('out of set range')
                    return False
                
                # check for width of each row
                if not (len(row_list) >= maze_dim_min and len(row_list) <= maze_width_max):
                    print('row size issue')
                    return False
                
                # check for last digit on each line
                if row_list[-1] == '1' or row_list[-1] == '3':
                    print('last digit issue, 1 or 3')
                    return False

                maze.append(row_list)		# record all suitable char to global list maze
                            
	# check for height of entire maze
        if not (len(maze) >= maze_dim_min and len(maze) <= maze_height_max):
            print('col size issue')
            return False
        # check for last digits of last line
        if maze[-1][-1] == '2':
            print('last line digit issue, 2')
            return False
        print('All good')
        DisplayList(maze)
        
        # assign dim to global variable and create object
        global N, M
        N = len(maze[0])
        M = len(maze)
        print('M', M, N)
        #CreateSpaceMatrix()
        return True

def CreateSpaceMatrix():
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

def DefineSpaceObject():
    pathObject = []
    for i in range(M-1):
        temp = []
        for j in range(N-1):
            temp.append(space())
        pathObject.append(temp)
    
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

            if val_1 == '1' or val_1 == '2':        #can be removed
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
    return pathObject                  
#cul_de_sacs

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

"""
Yellow path

"""
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
    global final_path_set
    final_hor_set_1 = final_ver_set
    final_hor_set.extend(final_ver_set)
    final_path_set = final_hor_set

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




"""
Generate output
-----------------------------
"""

def General():
    """
    wall Section
    ---------------------------------------------------------------------
    """
    # horizontal wall
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

    # vertical walls
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
    
    
    # combine all walls
    hor_lines.extend(ver_lines)
    global final_walls
    for i in hor_lines:
        txt = '    \draw ({},{}) -- ({},{});\n'.format(i[0][0], i[0][1], i[1][0], i[1][1])
        final_walls += txt


    
    """
    pillars Section
    ---------------------------------------------------------------------
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

    global final_Pillars       
    for i in pillars:
        txt = '    \\fill[green] ({},{}) circle(0.2);\n'.format(i[0], i[1])
        final_Pillars += txt

    """
    cul_de_sacs Section
    ---------------------------------------------------------------------
    """
    global pathObject
    pathObject = DefineSpaceObject()
    for i in range(M-1):
        for j in range(N-1):
            MarkWay(i, j)
            
    showList = []
    for i in range(M-1):
        tempList = []
        for j in range(N-1):
            tempList.append(pathObject[i][j].value)
            if pathObject[i][j].value == -1:
                red_cross.append((j+0.5, i+0.5))
        showList.append(tempList)
    DisplayList(showList)
    print(maze)

    global final_red_cross
    for i in red_cross:
        txt = '    \\node at ({},{}) {{}};\n'.format(i[0], i[1])
        final_red_cross += txt

    """
    inaccessible points
        
    """
    global inaccess
    for i in pathObject:
        for j in i:
            if j.value == 0:
                inaccess += 1

    """
    entry-exit path
    ---------------------------------------------------------------------
    """
    global yellowMaze
    yellowMaze =[[0]*(N+1) for _ in range(M+1)]
    
    
    MarkEntryExit()

    for i in range(M-1):
        for j in range(N-1):
            if pathObject[i][j].value == -2:
                entryPoint.append((j, i))
    FindYellowPath()


    global final_path
    for i in final_path_set:
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

    """
    find numbers of gates
    ---------------------------------------------------------------------
    """
    gateSet = []
    global gates
    
    for i in range(M - 1):
        for j in range(N - 1):
            space = pathObject[i][j]
            if i == 0 and space.N_wall == 0:
                gateSet.append((j, i))
                #gates += 1
            if i == M - 2 and space.S_wall == 0:
                gateSet.append((j, i))
                #gates += 1
            if j == 0 and space.W_wall == 0:
                gateSet.append((j, i))
                #gates += 1
            if j == N - 2 and space.E_wall == 0:
                gateSet.append((j, i))
                #gates += 1
    gates = len(gateSet)
  
    
    """
    find connected wall
    ---------------------------------------------------------------------
    """
    
    # make a copy of the maze
    print()
    wallMaze = copy.deepcopy(maze)

    def SeekWall(i, j):
        #print('-'*10)
        #print('excute', i, j, 'mazevalue', wallMaze[i][j])
        val = wallMaze[i][j]
        if val == '0':
            if j - 1 >= 0 and (wallMaze[i][j -1] == '1' or wallMaze[i][j - 1] == '3'):
                SeekWall(i, j - 1)
                j -= 1
            
            if i - 1 >= 0 and (wallMaze[i-1][j] == '2' or wallMaze[i-1][j] == '3'):
                SeekWall(i - 1, j)
                i -= 1
            
            return
        if val == '1':
            wallMaze[i][j] = '0'
            if j + 1 < N:
                SeekWall(i, j + 1)
            if i - 1 >= 0 and (wallMaze[i-1][j] == '2' or wallMaze[i-1][j] == '3'):
                SeekWall(i - 1, j)
            if j - 1 >= 0 and (wallMaze[i][j -1] == '1' or wallMaze[i][j - 1] == '3'):
                SeekWall(i, j - 1)
                j -= 1
            return
        if val == '2':
            wallMaze[i][j] = '0'
            if i + 1 < M:
                SeekWall(i + 1, j)
            if j - 1 >= 0 and (wallMaze[i][j - 1] == '1' or wallMaze[i][j - 1] == '3'):
                SeekWall(i, j - 1)
            if i - 1 >= 0 and (wallMaze[i-1][j] == '2' or wallMaze[i-1][j] == '3'):
                SeekWall(i - 1, j)
                i -= 1
            return
        if val == '3':
            wallMaze[i][j] = '0'
            SeekWall(i, j)
            if j + 1 < N:
                SeekWall(i, j + 1)
            if i + 1 < M:
                SeekWall(i + 1, j)
            return

    global wallSet
    for i in range(M):
        for j in range(N):
            if wallMaze[i][j] != '0':                
                SeekWall(i, j)
                wallSet += 1

    """
    accessible area
    ---------------------------------------------------------------------
    """

    
    tempPath = DefineSpaceObject()
    
    print('tempPath')
    for i in red_cross:
        x = int(i[1] - 0.5)
        y = int(i[0] - 0.5)
        tempPath[x][y].value = -1

    print('before', len(tempPath))
    for i in range(M-1):
        for j in range(N-1):
            print(tempPath[i][j].value, end=' ')
        print()

    def Walker(i, j):

        if i < 0 or j <0 or i >M-2 or j >N-2:
            return
        #print('i, j', i, j)
        space = tempPath[i][j]
        if space.value <= 1:
            return
        #if j > 0 and j < M - 3:
        if space.W_wall == 0:
            space.value -= 1
            if j > 0 and tempPath[i][j - 1].value > 1:
                
                tempPath[i][j - 1].E_wall = 1
                Walker(i, j - 1)
        if space.E_wall == 0:
            #print('test', j < N-3, tempPath[j + 1][i].value)
            space.value -= 1
            if j < N-2 and tempPath[i][j + 1].value > 1:
              
                tempPath[i][j + 1].W_wall = 1
                Walker(i, j + 1)
        #if i > 0 and i < N - 3:
        if space.N_wall == 0:
            space.value -= 1
            if i > 0 and tempPath[i - 1][j].value > 1:
                
                tempPath[i - 1][j].S_wall = 1
                Walker(i - 1, j)
        if space.S_wall == 0:

            space.value -= 1
            
            if i < M - 2 and tempPath[i + 1][j].value > 1:
                
                tempPath[i + 1][j].N_wall = 1
                Walker(i + 1, j)
        return
    global acc_area

    for gate in gateSet:
        i = gate[1]
        j = gate[0]
        if tempPath[i][j].value == -1:
            acc_area += 1
        elif tempPath[i][j].value > 1:
            Walker(i, j)
            acc_area += 1

    """
    for i in gateSet:
        x = i[0]
        y = i[1]
        print(x, y)
    """
    print('after', len(tempPath))
    for i in range(M-1):
        for j in range(N-1):
            print(tempPath[i][j].value, end=' ')
        print()
    """
        tempList = []
        
            tempList.append(tempPath[i][j].value)
        showList.append(
    DisplayList(showList)
    print()
    """

    """
    connected cul-de-sacs
    ---------------------------------------------------------------------
    """

    blockPath = DefineSpaceObject()
    
    print('tempPath')
    for i in red_cross:
        x = int(i[1] - 0.5) 
        y = int(i[0] - 0.5)
        blockPath[x][y].value = -1

    def Blocker(i, j):
        if i < 0 or j <0 or i >M-2 or j >N-2:
            return
        #print('i, j', i, j)
        space = blockPath[i][j]
        if space.value != -1:
            return
        if space.N_wall and space.S_wall and space.W_wall and space.E_wall:
            space.value = 0
            return
        #if j > 0 and j < M - 3:
        if space.W_wall == 0:
            space.value = 0
            if j > 0 and blockPath[i][j - 1].value == -1:
                
                blockPath[i][j - 1].E_wall = 1
                Blocker(i, j - 1)
        if space.E_wall == 0:
            #print('test', j < N-3, blockPath[j + 1][i].value)
            space.value = 0
            if j < N-2 and blockPath[i][j + 1].value == -1:
               
                blockPath[i][j + 1].W_wall = 1
                Blocker(i, j + 1)
        #if i > 0 and i < N - 3:
        if space.N_wall == 0:
            space.value = 0
            if i > 0 and blockPath[i - 1][j].value == -1:
                
                blockPath[i - 1][j].S_wall = 1
                Blocker(i - 1, j)
        if space.S_wall == 0:

            space.value = 0
            
            if i < M - 2 and blockPath[i + 1][j].value == -1:
                
                blockPath[i + 1][j].N_wall = 1
                Blocker(i + 1, j)
        return


    
    global blocker
    
    for i in range(M-1):
        for j in range(N-1):
            if blockPath[i][j].value == -1:
                print(i, j, blockPath[i][j].value)
                Blocker(i, j)
                print('result', blocker)
                """
                for i in range(M-1):
                    for j in range(N-1):
                        print(blockPath[i][j].value, end=' ')
                    print()
                """
                blocker += 1
   
    
    """
    allPath
    ---------------------------------------------------------------------
    """
    global path_num

    for i in allPath:
        entry_point = i[0]
        exit_point = i[-1]
        if len(i) > 1:
            if entry_point in gateSet and exit_point in gateSet:
                path_num += 1
                continue
        if len(i) == 1:
            x = i[0][1]
            y = i[0][0]
            space = pathObject[x][y]
            if x == 0:  # first row
                if y== 0 and space.N_wall == 0 and space.W_wall == 0:
                    path_num += 1
                if y == N-2 and space.N_wall == 0 and space.E_wall == 0:
                    path_num += 1
            if x == M - 2:
                if y == 0 and space.S_wall == 0 and space.W_wall == 0:
                    path_num += 1
                if y == N-2 and space.S_wall == 0 and space.E_wall == 0:
                    path_num += 1
        
def GenerateText():
    print('here is GenerateText')

    if not gates:
        print('The maze has no gate.')
    elif gates == 1:
        print('The maze has a single gate.')
    else:
        print('The maze has {} gates.'.format(gates))
    

    if not wallSet:
        print('The maze has no inaccessible inner point.')
    elif wallSet == 1:
        print('The maze has a unique inaccessible inner point.')
    else:
        print('The maze has {} inaccessible inner points.'.format(wallSet))
    
    if not inaccess:
        print('The maze has no accessible area.')
    elif inaccess == 1:
        print('The maze has a unique accessible area.')
    else:
        print('The maze has {} accessible areas.'.format(inaccess))

    if not acc_area:
        print('The maze has no accessible area.')
    elif acc_area == 1:
        print('The maze has a unique accessible area.')
    else:
        print('The maze has {} accessible areas.'.format(acc_area))
        
    
    if not blocker:
        print('The maze has no accessible cul-de-sac.')
    elif blocker == 1:
        print('The maze has accessible cul-de-sacs that are all connected.')
    else:
        print('The maze has {} sets of accessible cul-de-sacs that are all connected.'.format(blocker))

    if not path_num:
        print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
    elif path_num == 1:
        print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
    else:
        print('The maze has {} entry-exit paths with no intersections not to cul-de-sacs.'.format(path_num))
        
    
def GeneratePdf():
    print('here is GeneratePdf')

    

    
    
    

    """
    write to tex file
    ---------------------------------------------------------------------
    """
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
{3}\end{{tikzpicture}}
\end{{center}}
\vspace*{{\fill}}

\end{{document}}
""".format(final_walls, final_Pillars, final_red_cross, final_path)
    content = content.encode('utf-8')


    tex_name = sys.argv[-1][:-4] + '.tex'
    with open(tex_name,'wb') as f:
        f.write(content)
    
"""
Check input
-----------------------------
"""

in_len = len(sys.argv)

while True:
    try:
        # check for numbers of input parameters
        if not (in_len == 3 or in_len == 4):
            raise ValueError
        
        # allocated variables
        _fName = sys.argv[-1]
        _fdash = sys.argv[-2]
        _print = sys.argv[-3]
        
        # check for parameters_1: if the file existing
        if not os.path.exists(_fName):
            raise ValueError
        # check if the content is within constraint
        if not Check_file_content(_fName):
            print(errMsg_2)
            sys.exit()
        
        # check for parameters_2: --file
        if _fdash != '--file':
            raise ValueError
        
        # check for parameters_3: with or without 'print'
        
        if in_len == 3:
            General()
            GenerateText()
            break
        
        if in_len == 4:
            if _print != '-print':
                raise ValueError
            General()
            GeneratePdf()
            break
    except ValueError:
        print(errMsg_1)
        sys.exit()
    
        

    

