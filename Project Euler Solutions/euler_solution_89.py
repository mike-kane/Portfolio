##############################################################################################################################################################################################################################################
#                                                                                                       Project Euler Problem 89 Solution -- Roman Numerals
#                                                                                                                           By Mike Kane
#   
#  For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" 
#
#  way of writing a particular number.
#
#  For example, it would appear that there are at least six ways of writing the number sixteen:
#
#  IIIIIIIIIIIIIIII
#  VIIIIIIIIIII
#  VVIIIIII
#  XIIIIII
#  VVVI
#  XVI
#
#  However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.
#
#  The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the 
#
#  definitive rules for this problem.
#
#  Find the number of characters saved by writing each of these in their minimal form.
#
#  Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
#
##############################################################################################################################################################################################################################################

#  this function works, but upon further examination, isn't necessary since the numbers are already sorted.  The question doesnt ask for the total of the
#  numbers themselves--just the difference between the current length and the length of the correctly written values. Therefore, this problem can be solved by identifying the incorrect syntax 
#  and making the total count reflect the changes as necessary.  

#def getRomanNumeralValue(strNumber):                                    
#    ''' Expects string of roman numerals as input. '''                
#    total = 0
#    numeralValues = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#    for numeral in strNumber:
#        total += numeralValues[numeral]
#    return total
import re, urllib2


def getAnswer():
    wrongTotal = 0
    rightTotal = 0
    diff = wrongTotal - rightTotal
    numeralsList = []
    nums = ''
    with open('p089_roman.txt', 'r') as f:
        for line in f:
            numeralsList.append(line.rstrip('\n').split(" "))
    for line in numeralsList:
        for numeral in line:
            nums += numeral
    
    
    print len(nums) 
    

def getAnswer2():
    file_url = 'http://projecteuler.net/project/resources/p089_roman.txt'
    rows = urllib2.urlopen(file_url).read()
    
    print len(rows)
        
            
        
    
    
        

