import java.util.Arrays;
import java.util.Stack;

// notes:
//   - learn to use debugger
//   - look up more problems online to test
//   - clean up the code
//   - present solution better in terminal
//   - user input
//   - check problem is feasible
//      - if error, note the error
//      - supply = demand
//       - inputs exist and are valid
//   - (using int has a max value) 
// Cases where this code doesnt work:
//   - when you need 2 0's in the u and v (UandV function) i.e. placing the first zero doesn't necessarily dictate all the other values
//

public class transportationProblem {

    static boolean isFeasible(int[] supply, int[] demand, int[][] cost) {
        if(supply.length == 0) {
            System.out.print("This problem is infeasible: You need at least 1 warehouse to deliver the supply.");
            return false;
        }
        if(demand.length == 0) {
            System.out.print("This problem is infeasible: You need at least 1 store to recieve the supply.");
            return false;
        }
        if(cost.length != supply.length) {
            System.out.print("This problem is infeasible: Please enter a cost for shipping from every warehouse.");
            return false;
        }
        for(int x = 0; x < cost.length; x++) {
            if(cost[x].length != demand.length) {
                System.out.print("This problem is infeasible: Please enter a cost for shipping to every store.");
                return false;
            }
        }
        for(int i = 0; i < cost.length; i++) {
            for(int j = 0; j < cost[0].length; j++) {
                if(cost[i][j] < 0) {
                    System.out.print("This problem is infeasible: The cost of shipping supplies cannot be negative.");
                    return false;
                }
            }
        }
        int totalSupply = 0;
        int totalDemand = 0;
        for(int x = 0; x < supply.length; x++) {
            totalSupply += supply[x];
        }
        for(int x = 0; x < demand.length; x++) {
            totalDemand += demand[x];
        }
        if(totalSupply != totalDemand) {
            System.out.print("This problem is infeasible: The total supply must equal the total demand.");
            return false;
        }
        return true;
    }
    
    static void fillOrigSolution(int[] supply, int[] demand, int[][] solution) {
        int[] s = Arrays.copyOf(supply, supply.length);
        int[] d = Arrays.copyOf(demand, demand.length);
        for(int i = 0; i < solution.length; i++) {
            for(int j = 0; j < solution[0].length; j++) {
                if(s[i] < d[j]){
                    solution[i][j] = s[i];
                    d[j] = d[j] - s[i];
                    s[i] = 0;
                }
                else {
                    solution[i][j] = d[j];
                    s[i] = s[i] - d[j];
                    d[j] = 0;
                }
            }
        }
    }

    static void reset(int[][] solution, int[][] copy, int[] row, int[] col, int[] myPath) {
        for(int i = 0; i < solution.length; i++) {
            for(int j = 0; j < solution[0].length; j++) {
                copy[i][j] = solution[i][j];
            }
        }
        for(int i = 0; i < row.length; i++) {
            row[i] = 0;
        }
        for(int i = 0; i < col.length; i++) {
            col[i] = 0;
        }
        for(int i = 0; i < myPath.length; i++) {
            myPath[i] = -1;
        }
    }

    static boolean check(boolean[] row, boolean[] col) {
        for(int x = 0; x < row.length; x++) {
            if(row[x] == false) {
                return true;
            }
        }
        for(int x = 0; x < col.length; x++) {
            if(col[x] == false) {
                return true;
            }
        }
        return false;
    }

    static void UandV(int[] row, int[] col, int[][] cost, int[][] solution) {
        /* Determining where to put the 0 */
        boolean rowbool[] = new boolean[row.length];
        boolean colbool[] = new boolean[col.length];
        Arrays.fill(rowbool, false);
        Arrays.fill(colbool, false);
        int rowNum[] = new int[row.length];
        int colNum[] = new int[col.length];
        for(int i = 0; i < solution.length; i++) {
            for(int j = 0; j < solution[0].length; j++) {
                if(solution[i][j] != 0) {
                    rowNum[i]++;
                    colNum[j]++;
                }
            }
        }
        int max = 0;
        String direction= "not sure yet";
        int index = -1;
        for(int x = 0; x < rowNum.length; x++) { 
            if(rowNum[x] > max) {
                max = rowNum[x];
                direction = "Row";
                index = x;
            }
        }
        for(int x = 0; x < colNum.length; x++) {
            if(colNum[x] > max) {
                max = colNum[x];
                direction = "Col";
                index = x;
            }
        }
        /* Placing the 0 */
        if(direction == "Row") {
            row[index] = 0;
            rowbool[index] = true;
        }
        if(direction == "Col") {
            col[index] = 0;
            colbool[index] = true;
        }
        /* Filling in the rest */
        while(check(rowbool, colbool)) {
            for(int i = 0; i < solution.length; i++) {
                for(int j = 0; j < solution[0].length; j++) {
                    if(solution[i][j] != 0) {
                        if(colbool[j] == false && rowbool[i] == true) {
                            col[j] = cost[i][j] - row[i];
                            colbool[j] = true;
                        }
                        if(colbool[j] == true && rowbool[i] == false) {
                            row[i] = cost[i][j] - col[j];
                            rowbool[i] = true;
                        }
                    }
                }
            }
        }
    }

    static void fill(int[][] copy, int[] row, int[] col, int[][] cost) {
        for(int i = 0; i < copy.length; i++) {
            for(int j = 0; j < copy[0].length; j++) {
                if(copy[i][j] == 0) {
                    copy[i][j] = cost[i][j] - (row[i] + col [j]);
                }
            }
        }
    }

    static int[] checkIfDoneOrFindMinBox(int[][] copy) {
        int min = 0, r = -1, c = -1;
        for(int i = 0; i < copy.length; i++) {
            for(int j = 0; j < copy[0].length; j++) {
                if(copy[i][j] < min) {
                    min = copy[i][j];
                    r = i;
                    c = j;
                }
            }
        }
        int[] toReturn = {r, c};
        return toReturn;
    }

    static void findPath(int row, int col, int[][] solution, int[] myPath) {
        Stack<Integer> path = new Stack<Integer>();
        int rowMod = solution.length;
        int colMod = solution[0].length;
        int rloc = row;
        int cloc = (col + 1) % colMod;
        int count = 1;
        String direction = "horizontal";

        while(!(rloc == row && cloc == col)) {
            if(solution[rloc][cloc] == 0) {
                if(direction == "horizontal") {
                    cloc = (cloc + 1) % colMod;
                }
                else if(direction == "vertical") {
                    rloc = (rloc + 1) % rowMod;
                }
                count++;
            }
            else {
                if((direction == "horizontal" && count == colMod) || (direction == "vertical" && count == rowMod)) {
                    count = path.pop();
                    if(direction == "horizontal") {
                        direction = "vertical";
                    }
                    else if(direction == "vertical") {
                        direction = "horizontal";
                    }
                    if(direction == "horizontal") {
                        cloc = (cloc + 1) % colMod;
                    }
                    else if(direction == "vertical") {
                        rloc = (rloc + 1) % rowMod;
                    }
                    count++;
                }
                else {
                    path.push(count);
                    if(direction == "horizontal") {
                        direction = "vertical";
                    }
                    else if(direction == "vertical") {
                        direction = "horizontal";
                    }
                    count = 0;
                    if(direction == "horizontal") {
                        cloc = (cloc + 1) % colMod;
                    }
                    else if(direction == "vertical") {
                        rloc = (rloc + 1) % rowMod;
                    }
                    count++;
                }
            }
        }
        path.push(count);

        Stack<Integer> path2 = new Stack<Integer>(); // I probably dont need to do this and can probably figure out a way to work with original path
        while(!path.empty()) {
            path2.push(path.pop());
        }
        
        int x = 0;
        while(!path2.empty()) {
            myPath[x] = path2.pop();
            x++;
        }
        // printStack(path2, myPath, 0);
    }

    // static void printStack(Stack<Integer> path, int[] myPath, int i) {
    //     if(path.empty()) {
    //         return;
    //     }
    //     myPath[i] = path.pop();
    //     printStack(path, myPath, i+1);
    // }

    static void edit(int r, int c, int[][] solution, int[] myPath) {
        int rowMod = solution.length;
        int colMod = solution[0].length;
        /* Finding the value we add and subtract by */
        int min = Integer.MAX_VALUE;
        int i = 0;
        while(myPath[i] != -1) {
            if(i % 2 == 0) {
                c = (c + myPath[i]) % colMod;
                if(solution[r][c] < min) {
                    min = solution[r][c];
                }
            }
            else {
                r = (r + myPath[i]) % rowMod;
            }
            i++;
        }
        /* editing solution */
        i = 0;
        while(myPath[i] != -1) {
            if(i % 2 == 0) {
                c = (c + myPath[i]) % colMod;
                solution[r][c] = solution[r][c] - min;
            }
            else {
                r = (r + myPath[i]) % rowMod;
                solution[r][c] = solution[r][c] + min;
            }
            i++;
        }
    }
    
    public static void main(String[] args){
        int[] supply = {7, 12, 11};
        int[] demand = {10, 10, 10};
        int[][] cost = {{1, 2, 6}, {0, 4, 2}, {3, 1, 5}};
        int solution[][] = new int[cost.length][cost[0].length];
        int copy[][] = new int[cost.length][cost[0].length];
        int row[] = new int[supply.length];
        int col[] = new int[demand.length];
        int myPath[] = new int[(supply.length * demand.length)];
        Arrays.fill(myPath, -1);
        int box[] = new int[2];
        int count = 0;

        if(!isFeasible(supply, demand, cost)) {
            return;
        }
        
        fillOrigSolution(supply, demand, solution);
        reset(solution, copy, row, col, myPath);
                    System.out.println();
                    System.out.println("Iteration " + ++count + ":");
                    for(int i = 0; i < solution.length; i++) {
                        for(int j = 0; j < solution[0].length; j++) {
                            System.out.print(solution[i][j] + " ");
                        }
                        System.out.println();
                    }
                    System.out.println();
        UandV(row, col, cost, solution);
                    System.out.print("V: ");
                    for(int x = 0; x < row.length; x++) {
                        System.out.print(row[x] + " ");
                    }
                    System.out.println();
                    System.out.print("U: ");
                    for(int x = 0; x < col.length; x++) {
                        System.out.print(col[x] + " ");
                    }
                    System.out.println();
        fill(copy, row, col, cost);
                    System.out.println();
                    for(int i = 0; i < copy.length; i++) {
                        for(int j = 0; j < copy[0].length; j++) {
                            System.out.print(copy[i][j] + " ");
                        }
                        System.out.println();
                    }
                    System.out.println();
        box = checkIfDoneOrFindMinBox(copy); // I can probably find a better way to end the code if done
                    System.out.println("Min is at row " + box[0] + " col " + box[1]);

        while(box[0] != -1) {
        // while(count < 2) {
            findPath(box[0], box[1], solution, myPath);
                        System.out.print("Path: ");
                        for(int x = 0; x < myPath.length; x++) {
                            System.out.print(myPath[x] + " ");
                        }
                        System.out.println();
            edit(box[0], box[1], solution, myPath);
            reset(solution, copy, row, col, myPath);
                        System.out.println();
                        System.out.println("Iteration " + ++count + ":");
                        for(int i = 0; i < solution.length; i++) {
                            for(int j = 0; j < solution[0].length; j++) {
                                System.out.print(solution[i][j] + " ");
                            }
                            System.out.println();
                        }
                        System.out.println();
            UandV(row, col, cost, solution);
                        System.out.print("V: ");
                        for(int x = 0; x < row.length; x++) {
                            System.out.print(row[x] + " ");
                        }
                        System.out.println();
                        System.out.print("U: ");
                        for(int x = 0; x < col.length; x++) {
                            System.out.print(col[x] + " ");
                        }
                        System.out.println();
            fill(copy, row, col, cost);
            System.out.println();
                        for(int i = 0; i < copy.length; i++) {
                            for(int j = 0; j < copy[0].length; j++) {
                                System.out.print(copy[i][j] + " ");
                            }
                            System.out.println();
                        }
                        System.out.println();
            box = checkIfDoneOrFindMinBox(copy);
                        System.out.println("Min is at row " + box[0] + " col " + box[1]);       
        }
        System.out.println();
        System.out.println("Solution:");
        for(int i = 0; i < solution.length; i++) {
            for(int j = 0; j < solution[0].length; j++) {
                System.out.print(solution[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}