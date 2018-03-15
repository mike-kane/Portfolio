#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
#
#contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.



'''
Pseudocode for solution:
    
Hard code the letter values for:
    
    0-19
    multiples of 10
    multiples of 100
    add 3 for "and" to all numbers over 100
    add value for "One Thousand"
    
    for number in range (1, 1001):
        convert to string
        get letter values for each number, dependent upon values for each spot
        add letter values to total
        if len(number) == 3: add 3 to total (for 'and')
    return total

'''


def getLetterValue(number):
    total = 0
    strNumber = str(number)
    onesValues = {'1':3, '2': 3, '3':5, '4':4, '5':4, '6':3, '7':5, '8':5, '9':4, '0': 0}
    teensValues = {'1':6, '2':6, '3':8, '4':8, '5':7, '6':7, '7':9, '8':8, '9':8, '0': 0}
    tensValues = {'2':6, '3':6, '4':5, '5':5, '6':5, '7':7, '8':6, '9':6, '0': 0}  #twenty thirty forty fifty sixty seventy eighty ninety
    hundredAnd = 10
    hundred = 7
    
    
    if len(strNumber) == 3:
        if  strNumber[1] == '0' and strNumber[2] == '0':
            total += onesValues[strNumber[0]] + hundred
        else:
            if strNumber[1] == '1':
                total += onesValues[strNumber[0]] + hundredAnd + teensValues[strNumber[2]]
            else:
                total += onesValues[strNumber[0]] + hundredAnd + tensValues[strNumber[1]] + onesValues[strNumber[2]]
    elif len(strNumber) == 2:
        if strNumber[0] == '1':
            if strNumber[1] == '0':
                total += 3
            else:
                total += teensValues[strNumber[1]]
        else:
            total += tensValues[strNumber[0]] + onesValues[strNumber[1]]
    else:
        total += onesValues[strNumber]
    return total
    
      
     
def getAnswer(start, stop):
    answer = 0
    for number in range(start, stop + 1):
        if number == 1000:
            answer += 11
        else:
            answer += getLetterValue(number)
            print "number: " + str(number) + "     letter value: " + str(answer)
    return answer
             