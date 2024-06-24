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