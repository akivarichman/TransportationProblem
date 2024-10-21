from NWCM import NWCM
from LCM import LCM
from VAM import VAM

supply = [175, 200, 400, 225]
demand = [50, 175, 225, 175, 300, 75]
costs = [[17, 18, 10, 10, 5, 13], [6, 11, 13, 5, 10, 8], [9, 10, 4, 4, 3, 5], [13, 8, 6, 14, 9, 11]]
solution = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
total = 1000
rows = len(supply)
columns = len(demand)

# Code for NWCM is complete and works
# print("NWCM")
# NWCM(supply, demand, costs, solution, total)

# Code for LCM is (almost) complete and works (check the note in that file)
# print("LCM")
# LCM(supply, demand, costs, solution, total)

# print("VAM")
# VAM(supply, demand, costs, solution, total)






penalties = {}
creatingPenalties = True
row_num = 0
col_num = 0

# penalty dictionary
def updatePenalties(penaltydict):
    for row in range(rows):
        if(creatingPenalties or penaltydict['r', row] >= 0):
            min1 = 100 # really max int
            min2 = 100 # really max int
            for col in range(columns):
                if(creatingPenalties or penaltydict['c', col] >= 0):
                    if(costs[row][col] < min1):
                        min2 = min1
                        min1 = costs[row][col]
                    elif(costs[row][col] < min2):
                        min2 = costs[row][col]
            penaltydict["r",row] = min2 - min1
    for col in range(columns):
        if(creatingPenalties or penaltydict['c', col] >= 0):
            min1 = 100 # really max int
            min2 = 100 # really max int
            for row in range(rows):
                if(creatingPenalties or penaltydict['r', row] >= 0):
                    if(costs[row][col] < min1):
                        min2 = min1
                        min1 = costs[row][col]
                    elif(costs[row][col] < min2):
                        min2 = costs[row][col]
            penaltydict["c",col] = min2 - min1

# find where to place allocation based on min cost
def identifyCellToAllocate(direction, costs, row_num, col_num, penalties):
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


while total > 0:
    #determining the penalties of each row and column
    updatePenalties(penalties)
    creatingPenalties = False
    # finding the maximum penatly
    largest_penalty_key = max(penalties, key=penalties.get)
    direction, num = largest_penalty_key
    if(direction == 'r'):
        row_num = num
        penalties['r', num] = -1
    else:
        col_num = num
        penalties['c', num] = -1
    # allocating to min cost cell in that row / col with max penalty
    row_num, col_num = identifyCellToAllocate(direction, costs, row_num, col_num, penalties)
    allocation = min(supply[row_num], demand[col_num])
    solution[row_num][col_num] = allocation
    supply[row_num] = supply[row_num] - allocation
    demand[col_num] = demand[col_num] - allocation
    total = total - allocation

print(solution)



# even checks ones that were cancelled out already