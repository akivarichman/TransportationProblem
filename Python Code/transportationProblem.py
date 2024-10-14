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










# dictionary where key => the tuple (row, col) & value => the cost
costdict = {}
for row in range(rows):
    for col in range(columns):
        costdict[row, col] = costs[row][col]

# penalty dictionary
penaltydict = {}
for row in range(rows):
    min1 = 100 # really max int
    min2 = 100 # really max int
    for col in range(columns):
        if(costs[row][col] < min1):
            min2 = min1
            min1 = costs[row][col]
        elif(costs[row][col] < min2):
            min2 = costs[row][col]
    penaltydict["r",row] = min2 - min1
for col in range(columns):
    min1 = 100 # really max int
    min2 = 100 # really max int
    for row in range(rows):
        if(costs[row][col] < min1):
            min2 = min1
            min1 = costs[row][col]
        elif(costs[row][col] < min2):
            min2 = costs[row][col]
    penaltydict["c",col] = min2 - min1

print(penaltydict)

# find max from penatly dict
largest_key = max(penaltydict, key=penaltydict.get)
dir, num = largest_key

col_num = 1000
row_num = num

if(dir == 'r'):
    mini = 100 # really max int
    for col in range(columns):
        if(costdict[row_num, col] < mini):
            print(mini)
            message = 'we place allocation at row ', num, 'column ', col
            col_num = col
            mini = costdict[row_num, col]

print()

print(row_num)
print(col_num)

allocation = min(supply[row_num], demand[col_num])
solution[row_num][col_num] = allocation
supply[row_num] = supply[row_num] - allocation
demand[col_num] = demand[col_num] - allocation

print()
print(solution)
print(supply)
print(demand)

# while total > 0:
    



# even checks ones that were cancelled out already

print()