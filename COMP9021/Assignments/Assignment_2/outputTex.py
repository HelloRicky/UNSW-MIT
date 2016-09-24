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
       

test1 = b"""
hello\nricky
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
{1}
% Inner points in accessible cul-de-sacs
{2}
% Entry-exit paths without intersections
{3}
\end{{tikzpicture}}
\end{{center}}
\vspace*{{\fill}}

\end{{document}}""".format(final_walls,'b','c','d')
content = content.encode('utf-8')



with open('cover2.tex','wb') as f:
    f.write(content)

