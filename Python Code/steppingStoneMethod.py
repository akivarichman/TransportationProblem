import numpy as np
from collections import deque

def clean_path(path):
    row = 0
    col = 1
    index = 0
    direction = 'horizontal'
    if path[0][1] == path[1][1]:
        direction = 'vertical'
    while index < len(path) - 2:
        if direction == 'horizontal':
            while path[index][row] == path[index+2][row]:
                path.pop(index + 1)
            index += 1
            direction = 'vertical'
        else:
            while path[index][col] == path[index+2][col]:
                path.pop(index + 1)
            index += 1
            direction = 'horizontal'
    return path


def find_path(solution, start, end, basic_cells):
    """
    Find a path (loop) from start to end in the transportation matrix without recursion.
    The path alternates between horizontal and vertical moves.
    """
    rows = len(solution)
    columns = len(solution[0])
    
    # Stack to keep track of the path we are exploring
    path = []
    visited = set()
    stack = deque()
    stack.append((start, path, visited))  # (current position, path so far, visited cells)

    while stack:

        (i, j), path, visited = stack.pop()

        # If we reach the end and path is non-empty, return the complete loop
        if (i, j) == end and path:
            return path + [end]

        visited.add((i, j))  # Mark current cell as visited

        # Check horizontal moves (in the same row)
        for col in range(columns):
            if col != j and (i, col) in basic_cells and (i, col) not in visited:
                new_path = path + [(i, col)]  # Add this move to the path
                if col == end[1]:  # If the column matches the end cell's column, we can completed the loop
                    return clean_path([end] + new_path)
                # Push this move onto the stack for further exploration
                stack.append(((i, col), new_path, visited.copy())) # sending the set 'visited' into the stack with send a reference, we need to copy the set to avoid future changes from affecting this piece of the stack

        # Check vertical moves (in the same column)
        for row in range(rows):
            if row != i and (row, j) in basic_cells and (row, j) not in visited:
                new_path = path + [(row, j)]  # Add this move to the path
                if row == end[0]:  # If the row matches the end cell's row, we can completed the loop
                    return clean_path([end] + new_path)
                # Push this move onto the stack for further exploration
                stack.append(((row, j), new_path, visited.copy()))

    return None  # If no valid path is found, return None


def stepping_stone_method(costs, solution, rows, columns):

    basic_cells = set()
    for row in range(len(solution)):
        for col in range(len(solution[row])):
            if solution[row][col] > 0:
                basic_cells.add((row, col))

    while True:
        print()
        # calculating the opportunity costs
        opportunity_costs = np.full((rows, columns), np.inf)
        for i in range(rows):
            for j in range(columns):
                # if solution[i][j] == 0: # only find path and calculate opportunity cost for non-basic cells
                if (i, j) not in basic_cells:
                    path = find_path(solution, (i, j), (i, j), basic_cells)
                    print('----- [', i, '][ ', j, '] -----')
                    print(path)
                    if path:   ### not sure why this is needed
                        path_cost = 0
                        sign = 1
                        for (x, y) in path:
                            path_cost += sign * costs[x][y]
                            sign *= -1
                        opportunity_costs[i][j] = path_cost
                        print('Opportunity Cost', opportunity_costs[i][j])
                        # print()
                    else:
                        print('degenerate')
                    
        # Find lowest opportunity cost
        min_cost = np.min(opportunity_costs)
        if min_cost >= 0:
            # No improvement possible, optimal solution found
            break

        # Get the cell with the most negative opportunity cost
        i, j = np.unravel_index(np.argmin(opportunity_costs), opportunity_costs.shape)
        basic_cells.add((i, j))
        print("cell", i, j)

        # Find the loop for this cell
        path = find_path(solution, (i, j), (i, j), basic_cells)

        # Adjust the allocations
        if path:
            # Find the minimum value of the allocations along the path at odd positions
            allocations = [solution[x][y] for idx, (x, y) in enumerate(path) if idx % 2 == 1]
            min_allocation = min(allocations)

            # Adjust the solution along the path
            sign = 1
            replaced_cell_in_basis = False
            for (x, y) in path:
                if solution[x][y] == min_allocation and not replaced_cell_in_basis and sign == -1:
                    basic_cells.remove((x, y))
                    replaced_cell_in_basis = True
                solution[x][y] += sign * min_allocation
                sign *= -1
        else:
            print('degenerate2')
            break

        for row in solution:
            for col in row:
                print(col, end=" ")
            print()
    
    # Calculate the total cost for the final solution
    # total = calculate_total_cost(solution, costs)

    return solution