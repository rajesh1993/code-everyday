'''
Input : Array containing heights of students.
Problem:
Given an array containing the heights of students, allot each student into a row where 
all other students are of greater height. If not possible to insert, then add a new row
and insert it into it.

Output:
Return the minimum number of rows that are required to accomodate all students.
'''

import numpy as np

def countRows(students):
	rows = []
	result = 0

	for idx, height in enumerate(students):
		minRow = 10001
		minIndex = -1
		minDiff = 100001
		# Find the row with height less than current height that has minimum difference
		for row_idx, row in enumerate(rows):
			if height < row and row - height < minDiff:
				minRow = row
				minIndex = row_idx 
				minDiff = row - height
		if minIndex != -1:
			rows[minIndex] = height
		# If no height is less, then add the height as a new row
		else:
			rows.append(height)
			result += 1
		
	return result

def main():
	a = [5,4,5,4,5]
	print(countRows(a))
	# for i in range(5):
	# 	test_case = np.random.randint(low=1, high=50, size=6)
	# 	print(list(test_case), countRows(list(test_case)))

if __name__ == "__main__":
	main()