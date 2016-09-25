"""

maze = [['1', '0', '2', '2', '1', '2', '3', '0'], ['3', '2', '2', '1', '2', '0', '2', '2'], ['3', '0', '1', '1', '3', '1', '0', '0'], ['2', '0', '3', '0', '0', '1', '2', '0'],
        ['3', '2', '2', '0', '1', '2', '3', '2'], ['1', '0', '0', '1', '1', '0', '0', '0']]
"""
maze = [['0', '2', '2', '3', '0', '2', '1', '2', '0', '2', '2', '2'], ['2', '2', '2', '2', '2', '3', '1', '1', '1', '0', '3', '2'], ['3', '0', '1', '3', '2', '2', '1', '3', '0', '3', '0', '2'],
        ['3', '1', '2', '3', '2', '2', '2', '3', '2', '3', '3', '0'], ['0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0']]


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
                print('road', i)
            continue
        print('chekc later', i)


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
