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

# 
print("VAM")
VAM(supply, demand, costs, solution, total, rows, columns)