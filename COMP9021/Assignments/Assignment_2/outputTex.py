maze = [['1', '0', '2', '2', '1', '2', '3', '0'], ['3', '2', '2', '1', '2', '0', '2', '2'], ['3', '0', '1', '1', '3', '1', '0', '0'],
        ['2', '0', '3', '0', '0', '1', '2', '0'], ['3', '2', '2', '0', '1', '2', '3', '2'], ['1', '0', '0', '1', '1', '0', '0', '0']]

final_walls = ""
final_Pillars = ""
final_points = ""
final_path = ""

N = len(maze[0])
M = len(maze)
hor_lines = []
ver_lines = []

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
{}
% Pillars
{}
% Inner points in accessible cul-de-sacs
{}
% Entry-exit paths without intersections
{}
\end{{tikzpicture}}
\end{{center}}
\vspace*{{\fill}}

\end{{document}}
""".format('a','b','c','d')

"""
with open('cover2.tex','w') as f:
    f.write(content)
"""
