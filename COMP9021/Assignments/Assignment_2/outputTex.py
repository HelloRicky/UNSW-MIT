from copy import deepcopy

maze = [['1', '0', '2', '2', '1', '2', '3', '0'], ['3', '2', '2', '1', '2', '0', '2', '2'], ['3', '0', '1', '1', '3', '1', '0', '0'],
        ['2', '0', '3', '0', '0', '1', '2', '0'], ['3', '2', '2', '0', '1', '2', '3', '2'], ['1', '0', '0', '1', '1', '0', '0', '0']]

final_walls = ""
final_Pillars = ""
final_points = ""
final_path = ""

N = len(maze[0])    # row length
M = len(maze)       # col length
hor_lines = []
ver_lines = []
pillars = []

class space:
    def __init__(self, value = 0, N_wall = 0, S_wall = 0, W_wall = 0, E_wall = 0):
        self.value = value
        self.N_wall = N_wall
        self.S_wall = S_wall
        self.W_wall = W_wall
        self.E_wall = E_wall

mazePath = [[0]*(N-1) for _ in range(M - 1)]

PathObject = []
for i in range(M-1):
    temp = []
    for j in range(N-1):
        temp.append(space())
    PathObject.append(temp)

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
                        PathObject[i][j].value = 4                      
                        continue
                    if val_3 == '1' or val_3 == '3':
                        PathObject[i][j].value = 3
                        PathObject[i][j].S_wall = 1
                        continue
                    
                if val_2 == '2' or val_2 == '3':
                    PathObject[i][j].E_wall = 1
                    if val_3 == '0' or val_3 == '2':
                        PathObject[i][j].value = 3
                        continue
                    if val_3 == '1' or val_3 == '3':
                        PathObject[i][j].value = 2
                        PathObject[i][j].S_wall = 1
                        continue

            if val_1 == '3':
                PathObject[i][j].N_wall = 1
                PathObject[i][j].W_wall = 1
                if val_2 == '0' or val_2 == '1':
                    if val_3 == '0' or val_3 == '2':
                        PathObject[i][j].value = 2
                        continue
                    if val_3 == '1' or val_3 == '3':
                        PathObject[i][j].value = 1
                        PathObject[i][j].S_wall = 1
                        continue
                if val_2 == '2' or val_2 == '3':
                    if val_3 == '0' or val_3 == '2':
                        PathObject[i][j].value = 1
                        PathObject[i][j].E_wall = 1
                        continue
                    if val_3 == '1' or val_3 == '3':
                        PathObject[i][j].value = 0
                        PathObject[i][j].S_wall = 1
                        PathObject[i][j].E_wall = 1
                        continue

            if val_1 == '1' or val_1 == '2':
                if val_1 == '1':
                    PathObject[i][j].N_wall = 1
                else:
                    PathObject[i][j].W_wall = 1
                if val_2 == '0' or val_2 == '1':
                    if val_3 == '0' or val_3 == '2':
                        PathObject[i][j].value = 3
                        continue
                    if val_3 == '1' or val_3 == '3':
                        PathObject[i][j].value = 2
                        PathObject[i][j].S_wall = 1
                        continue
                if val_2 == '2' or val_2 == '3':
                    if val_3 == '0' or val_3 == '2':
                        PathObject[i][j].value = 2
                        PathObject[i][j].E_wall = 1
                        continue
                    if val_3 == '1' or val_3 == '3':
                        PathObject[i][j].value = 1
                        PathObject[i][j].S_wall = 1
                        PathObject[i][j].E_wall = 1
                 




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
                
# cul-de-sacs
DefineSapce()
DisplayList(mazePath)

DefineSpaceObject()
space_val = [[0]*(N-1) for _ in range(M-1)]

for i in range(M-1):
    for j in range(N-1):
        space_val[i][j] = PathObject[i][j].N_wall
print('Oject path')
DisplayList(space_val)

# copy mazePath without reference
cul_de_sacs = deepcopy(mazePath)

def FindWay():
    for i in range(M-1):
        for j in range(N-1):
            val = cul_de_sacs[i][j]

            if val == 1:
                cul_de_sacs[i][j] = -1

                # find gate
                val_1 = maze[i][j]
                val_2 = maze[i][j + 1]
                val_3 = maze[i + 1][j]
                

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

\end{{document}}""".format(final_walls, final_Pillars,'c','d')
content = content.encode('utf-8')


"""
with open('cover2.tex','wb') as f:
    f.write(content)
"""
