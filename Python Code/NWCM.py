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