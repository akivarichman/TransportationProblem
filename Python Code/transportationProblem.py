print("\nHello World\n")

supply = [175, 200, 400, 225]
demand = [50, 175, 225, 175, 300, 75]
costs = [[17, 18, 10, 10, 5, 13], [6, 11, 13, 5, 10, 8], [9, 10, 4, 4, 3, 5], [13, 8, 6, 14, 9, 11]]
solution = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
total = 1000

def LCM(supply, demand, costs, solution, total):
    from queue import PriorityQueue
    pq = PriorityQueue()
    for row in range(len(costs)):
        for col in range(len(costs[row])):
            pq.put([costs[row][col], row, col], costs[row][col])

    while total > 0:
        cell = pq.get()
        supplyIndex = cell[1]
        demandIndex = cell[2]
        allocation = min(supply[supplyIndex], demand[demandIndex])
        solution[supplyIndex][demandIndex] = allocation
        supply[supplyIndex] = supply[supplyIndex] - allocation
        demand[demandIndex] = demand[demandIndex] - allocation
        total = total - allocation

    for row in solution:
        for col in row:
            print(col, end=" ")
        print()
    print()

def NWCM(supply, demand, costs, solution, total):
    s = 0
    d = 0
    while total > 0:
        allocation = min(supply[s], demand[d])
        solution[s][d] = allocation
        supply[s] = supply[s] - allocation
        demand[d] = demand[d] - allocation
        if supply[s] == 0:
            s = s + 1
        else:
            d = d + 1
        total = total - allocation
    for row in solution:
        for col in row:
            print(col, end=" ")
        print()
    print()

# print("NWCM")
# NWCM(supply, demand, costs, solution, total)

print("LCM")
LCM(supply, demand, costs, solution, total)

print()