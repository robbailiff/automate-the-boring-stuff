
def printTable(tableData):
    rows = len(max(tableData))
    columns = len(tableData)    # Number of columns
    colWidth = [0] * len(tableData) 
    for i in range(columns): # Check max string length in each column
        print len(max(tableData[i]))
        if len(max(tableData[i])) < 10: # Output does not return correctly unless rjust value is over 10
            colWidth[i] = 10
        else:
            colWidth[i] = (len(max(tableData[i])) + 1)

    # Now print the table
    print(sum(colWidth) * '-')
    for y in range(rows):
        print(tableData[0][y].rjust(colWidth[0], ' ') + tableData[1][y].rjust(colWidth[1], ' ') + tableData[2][y].rjust(colWidth[2], ' '))
        #print(tableData[0][y].rjust(10, ' ') + ' ' + tableData[1][y].rjust(10, ' ') + ' ' + tableData[2][y].rjust(10, ' ')) 
    print(sum(colWidth) * '-')


tableData = [
            ['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']
            ]

printTable(tableData)