# -*- coding: utf-8 -*-
#####################################################################################################################################
#                                   Project Euler Problem 39 Solution -- Integer Right Triangles
#                                                           By Mike Kane
#
#  If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
#  {20,48,52}, {24,45,51}, {30,40,50}
#
#  For which value of p ≤ 1000, is the number of solutions maximised?
#
#####################################################################################################################################
import math


def getRightTriangles():
    trianglePerimeters = []
    
    for a in range(1000):
        for b in range(1000):
           c = math.sqrt((a**2) + (b**2))
           perimeter = a + b + c
           if perimeter % 1 == 0 and perimeter <= 1000:
               trianglePerimeters.append(perimeter)
    occurenceCounter = 0
    answerSoFar = 0
    rightTriSet = set(trianglePerimeters)
    for triangle in rightTriSet:
        counter = 0
        for occurence in trianglePerimeters:
            if triangle == occurence:
                counter += 1
        if counter > occurenceCounter: 
            occurenceCounter = counter
            answerSoFar = triangle
    return answerSoFar, occurenceCounter
    