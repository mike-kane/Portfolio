# -*- coding: utf-8 -*-
####################################################################################################
#                                       Project Euler Problem 15 Solution -- Lattice Paths
#                                                       By Mike Kane
#                                                   (BRUTE FORCE RECURSIVE SOLUTION -- CAN BE IMPROVED LATER!)                                                          
#
# 
#  Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#  How many such routes are in a 20X20 grid?
#
#
#####################################################################################################
import time

start = time.time()
gridSize = [20,20]

def getPaths(gridSize):
    
    
    totalPaths = 0
    if gridSize == [0, 0]:return 1
    
    if gridSize[0] > 0:
        totalPaths += getPaths([gridSize[0] -1, gridSize[1]])
    if gridSize[1] > 0: 
        totalPaths += getPaths([gridSize[0], gridSize[1] - 1])
    return totalPaths
    
print getPaths([20,20])
print "Total Runtime:  " + str(time.time() - start)
    
    
    

 

 
 

 

    
    