# penalty dictionary
def updatePenalties(penalties, costs, rows, columns, creatingPenalties):
    for row in range(rows):
        if(creatingPenalties or penalties['r', row] >= 0):
            min1 = float('inf')
            min2 = float('inf')
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
            min1 = float('inf')
            min2 = float('inf')
            for row in range(rows):
                if(creatingPenalties or penalties['r', row] >= 0):
                    if(costs[row][col] < min1):
                        min2 = min1
                        min1 = costs[row][col]
                    elif(costs[row][col] < min2):
                        min2 = costs[row][col]
            penalties["c",col] = min2 - min1

# find where to place allocation based on min cost
def identifyCellToAllocate(direction, costs, row_num, col_num, penalties, rows, columns):
    if(direction == 'r'):
        minCost = float('inf')
        for col in range(columns):
            if(penalties['c', col] >= 0 and costs[row_num][col] < minCost):
                col_num = col
                minCost = costs[row_num][col]
    if(direction == 'c'):
        minCost = float('inf')
        for row in range(rows):
            if(penalties['r', row] >= 0 and costs[row][col_num] < minCost):
                row_num = row
                minCost = costs[row][col_num]
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
        row_num, col_num = identifyCellToAllocate(direction, costs, row_num, col_num, penalties, rows, columns)
        allocation = min(supply[row_num], demand[col_num])
        solution[row_num][col_num] = allocation
        supply[row_num] = supply[row_num] - allocation
        demand[col_num] = demand[col_num] - allocation
        total = total - allocation
    return solution