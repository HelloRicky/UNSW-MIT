import os
import sys


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

"""
Functions
-----------------------------
"""

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
				
	#check for height of entire maze
	if not (len(maze) >= maze_dim_min and len(maze) <= maze_height_max):
		print('col size issue')
		return False

	# check for last digits of last line
	if maze[-1][-1] == '2':
		print('last line digit issue, 2')
		return False
	
	print('All good')
	DisplayList(maze)
	return True


"""
Generate output
-----------------------------
"""

def GenerateText():
	print('here is GenerateText')
	print(maze)
	
def GeneratePdf():
	print('here is GeneratePdf')

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
			GenerateText()
			break
		
		if in_len == 4:
			if _print != '-print':
				raise ValueError
			GeneratePdf()
			break
	except ValueError:
		print(errMsg_1)
		sys.exit()
        
        
    

