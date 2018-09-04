import sys
import numpy as np

#these are what wins look like
x_win = ['x', 'x', 'x']
o_win = ['o', 'o', 'o']

def check_tictactoe(in_grid):
	#we will analyze winning slices to determine if there is a win in the given grid
	
	#horizontal wins
	#check first row
	if np.array_equal(x_win, in_grid[:, 0]) or np.array_equal(o_win, in_grid[:, 0]):		
		return 'Win has been found'
	#check second row
	if np.array_equal(x_win, in_grid[:, 1]) or np.array_equal(o_win, in_grid[:, 1]):		
		return 'Win has been found'
	#check third row
	if np.array_equal(x_win, in_grid[:, 2]) or np.array_equal(o_win, in_grid[:, 2]):		
		return 'Win has been found'
	
	#vertical wins
	#check first column
	if np.array_equal(x_win, in_grid[0, :]) or np.array_equal(o_win, in_grid[0, :]):		
		return 'Win has been found'
	if np.array_equal(x_win, in_grid[1, :]) or np.array_equal(o_win, in_grid[1, :]):		
		return 'Win has been found'
	if np.array_equal(x_win, in_grid[2, :]) or np.array_equal(o_win, in_grid[2, :]):		
		return 'Win has been found'

	#diagonal wins
	if np.array_equal(np.diag(in_grid), x_win) or np.array_equal(np.diag(in_grid), o_win):
		return 'Win has been found'
	if np.array_equal(np.diag(np.fliplr(in_grid)), x_win) or np.array_equal(np.diag(np.fliplr(in_grid)), o_win):
		return 'Win has been found'

	#base case
	return 'No wins found!'


if (len(sys.argv) != 10):
	print ("Usage:\tcheck_tictactoe.py (x|o) (x|o) (x|o) (x|o) (x|o) (x|o) (x|o) (x|o) (x|o) (x|o)\nWhere the 9 positions indicate the spot to the corresponding tic tac toe matrix starting at 1,1 1,2...3,3")
	exit()

grid = np.array([[sys.argv[1], sys.argv[2], sys.argv[3]],
	[sys.argv[4], sys.argv[5], sys.argv[6]],
	[sys.argv[7], sys.argv[8], sys.argv[9]]])

#print to check layout of tic tac toe board for debugging purposes
print(grid)

print(check_tictactoe(grid))


