# -*- coding: utf-8 -*-
##############################################################################################################################
#                           Project Euler Problem 22 Solution
#                                   By Mike Kane
#
#
#  Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into 
#
#  alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
#  For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
#  What is the total of all the name scores in the file?
#
##############################################################################################################################

def getAlphaNumericScore(name):
    name = name.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    score = 0
    for letter in name:
        if letter in alphabet:
            score += alphabet.index(letter) + 1
    return score

def populateNamesList():
     with open('p022_names.txt') as f:
        names = f.read().split(',')
     names.sort()
     
     return names

def getAnswer():
    totalScore = 0
    score = 0
    index = 0
    namesList = populateNamesList()
    for name in namesList:
        name = name.strip("'")
        score = getAlphaNumericScore(name)
        print "Name Score:  " + str(score)
        index = namesList.index(name) + 1
        print "Index position: " + str(index)
        score = score * index
        print "name score * index: " + str(score)
        totalScore += score
        print index
        score += index
        print 
    print "total score with index: " + str(totalScore)
    print namesList.index(namesList[0])
     
     


            


    
    
    
    
    
        
