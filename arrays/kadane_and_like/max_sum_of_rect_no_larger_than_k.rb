
 # Write a program to find maximum sum rectangle in give 2D matrix.
 # Assume there is at least one positive number in the 2D matrix.
 # 
 # Solution:
 # Keep temp array with size as number of rows. Start left and right from 0
 # and keep adding values for each row and maintain them in this temp array.
 # Run Kadane's algorithm to find max sum subarray in temp. Now increment right by
 # 1. When right reaches last column reset right to 1 and left to 1.
 # 
 # Space complexity of this algorithm is O(row)
 # Time complexity of this algorithm is O(row*col*col)
 # 
 # References
 # http://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/

