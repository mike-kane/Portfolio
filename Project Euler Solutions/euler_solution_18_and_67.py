import time

def recursiveRowSum(rowData, rowNum):
    
    for i in range(len(rowData[rowNum])):                   #loops through each position in row data.  Each row has list of items equal to row number.  Row 1 has 1, row 2 has 2, etc.
        rowData[rowNum][i] += max([rowData[rowNum+1][i], rowData[rowNum+1][i + 1]])
        
        if len(rowData[rowNum])  == 1:  # base case = top of pyramid.
        return rowData[rowNum][0]
    else:
        return recursiveRowSum(rowData, rowNum - 1)
            
rows = []

with open('P067_triangle.txt') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])

start = time.time()
answer = recursiveRowSum(rows, len(rows) - 2)
elapsed = time.time() - start

print 'answer {} found in {} seconds'.format(answer, elapsed)

# row data is variable name for total list of lists.
# row number is the index that allows us to select a specific row.
# i in for loop on line 5 stands in for specific number at each lattice point.  