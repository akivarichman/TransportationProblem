from queue import PriorityQueue

# what about tiebreaker of adding most units to
# checks all cells even if already crossed out
def LCM(supply, demand, costs, solution, total):
    pq = PriorityQueue()
    for row in range(len(costs)):
        for col in range(len(costs[row])):
            pq.put((costs[row][col], [row, col]))
    while total > 0:
        cell = pq.get()
        supplyIndex = cell[1][0]
        demandIndex = cell[1][1]
        allocation = min(supply[supplyIndex], demand[demandIndex])
        if allocation != 0:
            solution[supplyIndex][demandIndex] = allocation
            supply[supplyIndex] = supply[supplyIndex] - allocation
            demand[demandIndex] = demand[demandIndex] - allocation
            total = total - allocation
    return solution