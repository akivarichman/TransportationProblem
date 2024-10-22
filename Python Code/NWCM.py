def NWCM(supply, demand, costs, solution, total):
    s = 0
    d = 0
    while total > 0:
        allocation = min(supply[s], demand[d])
        solution[s][d] = allocation
        supply[s] = supply[s] - allocation
        demand[d] = demand[d] - allocation
        total = total - allocation
        if supply[s] == 0:
            s = s + 1
        if demand[d] == 0:
            d = d + 1
    return solution