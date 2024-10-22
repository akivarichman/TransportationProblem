# penalty dictionary
def updatePenalties(penalties, costs, rows, columns, creatingPenalties):
    for row in range(rows):
        if(creatingPenalties or penalties['r', row] >= 0):
            min1 = 100 # really max int
            min2 = 100 # really max int
            for col in range(columns):
                if(creatingPenalties or penalties['c', col] >= 0):
                    if(costs[row][col] < min1):
                        min2 = min1
                        min1 = costs[row][col]
                    elif(costs[row][col] < min2):
                        min2 = costs[row][col]
            penalties["r",row] = min2 - min1
    for col in range(columns):
        if(creatingPenalties or penalties['c', col] >= 0):
            min1 = 100 # really max int
            min2 = 100 # really max int
            for row in range(rows):
                if(creatingPenalties or penalties['r', row] >= 0):
                    if(costs[row][col] < min1):
                        min2 = min1
                        min1 = costs[row][col]
                    elif(costs[row][col] < min2):
                        min2 = costs[row][col]
            penalties["c",col] = min2 - min1

# find where to place allocation based on min cost
def identifyCellToAllocate(direction, costs, row_num, col_num, penalties, rows, columns, creatingPenalties):
    if(direction == 'r'):
        mini = 100 # really max int
        for col in range(columns):
            if(penalties['c', col] >= 0 and costs[row_num][col] < mini):
                col_num = col
                mini = costs[row_num][col]
    if(direction == 'c'):
        mini = 100 # really max int
        for row in range(rows):
            if(penalties['r', row] >= 0 and costs[row][col_num] < mini):
                row_num = row
                mini = costs[row][col_num]
    return [row_num, col_num]

# what about tiebreaker of adding most units to
def VAM(supply, demand, costs, solution, total, rows, columns):
    penalties = {}
    creatingPenalties = True
    while total > 0:
        #determining the penalties of each row and column
        updatePenalties(penalties, costs, rows, columns, creatingPenalties)
        creatingPenalties = False
        # finding the maximum penatly
        largest_penalty_key = max(penalties, key=penalties.get)
        direction, num = largest_penalty_key
        if(direction == 'r'):
            row_num = num
            col_num = None
            penalties['r', num] = -1
        else:
            row_num = None
            col_num = num
            penalties['c', num] = -1
        # allocating to min cost cell in that row / col with max penalty
        row_num, col_num = identifyCellToAllocate(direction, costs, row_num, col_num, penalties, rows, columns, creatingPenalties)
        allocation = min(supply[row_num], demand[col_num])
        solution[row_num][col_num] = allocation
        supply[row_num] = supply[row_num] - allocation
        demand[col_num] = demand[col_num] - allocation
        total = total - allocation

    for row in solution:
        for col in row:
            print(col, end=" ")
        print()
    print()