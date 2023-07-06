import java.util.Arrays;
import java.util.Stack;

// notes:
//  - learn to use debugger
//   - currently hard coded for a 3x3 only
//   - look up more problems online to test
//   - clean up the code
// Cases where this code doesnt work:
//   - when you need 2 0's in the u and v (UandV function) i.e. placing the first zero doesn't necessarily dictate all the other values

public class transportationProblem {
    
    static void fillOrigSolution(int[] supply, int[] demand, int[][] solution) { // checked
        int[] s = Arrays.copyOf(supply, supply.length);
        int[] d = Arrays.copyOf(demand, demand.length);
        for(int i = 0; i < solution.length; i++) {
            for(int j = 0; j < solution.length; j++) {
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

    static void reset(int[][] solution, int[][] copy, int[] row, int[] col, int[] myPath) { // checked
        for(int i = 0; i < solution.length; i++) {
            for(int j = 0; j < solution.length; j++) {
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

    static boolean check(boolean[] row, boolean[] col) { // checked
        for(int x = 0; x < row.length; x++) { // this condition will have to be changed when we change the size from just 3x3
            if(row[x] == false || col[x] == false) {
                return true;
            }
        }
        return false;
    }

    static void UandV(int[] row, int[] col, int[][] cost, int[][] solution) { // checked
        /* Determining where to put the 0 */
        boolean[] colbool = {false, false, false};
        boolean[] rowbool = {false, false, false};
        int[] rowNum = {0, 0, 0};
        int[] colNum = {0, 0, 0};
        for(int i = 0; i < solution.length; i++) {
            for(int j = 0; j < solution.length; j++) {
                if(solution[i][j] != 0) {
                    rowNum[i]++;
                    colNum[j]++;
                }
            }
        }
        int max = 0;
        String direction= "not sure yet";
        int index = -1;
        for(int x = 0; x < solution.length; x++) { // the condition here will have to be changed when we make it work for not just 3x3
            if(rowNum[x] > max) {
                max = rowNum[x];
                direction = "Row";
                index = x;
            }
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
                for(int j = 0; j < solution.length; j++) {
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

    static void fill(int[][] copy, int[] row, int[] col, int[][] cost) { // checked
        for(int i = 0; i < copy.length; i++) {
            for(int j = 0; j < copy.length; j++) {
                if(copy[i][j] == 0) {
                    copy[i][j] = cost[i][j] - (row[i] + col [j]);
                }
            }
        }
    }

    static int[] checkIfDoneOrFindMinBox(int[][] copy) { // checked
        int min = 0, r = -1, c = -1;
        for(int i = 0; i < copy.length; i++) {
            for(int j = 0; j < copy.length; j++) {
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

    static void findPath(int row, int col, int[][] solution, int[] myPath) { // checked
        Stack<Integer> path = new Stack<Integer>();
        int rloc = row;
        int cloc = (col + 1) % 3; // will have to change 3 to be whatever size needed
        int count = 1; // also will depend on rows/cols
        String direction = "horizontal";

        while(!(rloc == row && cloc == col)) {
            if(solution[rloc][cloc] == 0) {
                if(direction == "horizontal") {
                    cloc = (cloc + 1) % 3;
                }
                else if(direction == "vertical") {
                    rloc = (rloc + 1) % 3;
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
                    cloc = (cloc + 1) % 3;
                }
                else if(direction == "vertical") {
                    rloc = (rloc + 1) % 3;
                }
                count++;
            }
            if(count == 3) {
                count = path.pop();
                if(direction == "horizontal") {
                    direction = "vertical";
                }
                else if(direction == "vertical") {
                    direction = "horizontal";
                }
                if(direction == "horizontal") {
                    cloc = (cloc + 1) % 3;
                }
                else if(direction == "vertical") {
                    rloc = (rloc + 1) % 3;
                }
                count++;
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
        /* Finding the value we add and subtract by */
        int min = 100;
        int i = 0;
        while(myPath[i] != -1) {
            if(i % 2 == 0) {
                c = (c + myPath[i]) % 3;
                if(solution[r][c] < min) {
                    min = solution[r][c];
                }
            }
            else {
                r = (r + myPath[i]) % 3;
            }
            i++;
        }
        /* editing solution */
        i = 0;
        while(myPath[i] != -1) {
            if(i % 2 == 0) {
                c = (c + myPath[i]) % 3;
                solution[r][c] = solution[r][c] - min;
            }
            else {
                r = (r + myPath[i]) % 3;
                solution[r][c] = solution[r][c] + min;
            }
            i++;
        }
    }
    
    public static void main(String[] args){
        int[] supply = {100, 150, 120};
        int[] demand = {80, 120, 170};
        int[][] cost = {{5, 8, 6}, {7, 9, 4}, {6, 5, 7}};
        int[][] solution = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        int[][] copy = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        int row[] = new int[supply.length];
        int col[] = new int[demand.length];
        int myPath[] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
        int box[] = new int[2];
        int count = 0;

        fillOrigSolution(supply, demand, solution);
        reset(solution, copy, row, col, myPath);
                    System.out.println();
                    System.out.println("Iteration " + ++count + ":");
                    for(int i = 0; i < solution.length; i++) {
                        for(int j = 0; j < solution.length; j++) {
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
                        for(int j = 0; j < copy.length; j++) {
                            System.out.print(copy[i][j] + " ");
                        }
                        System.out.println();
                    }
                    System.out.println();
        box = checkIfDoneOrFindMinBox(copy); // I can probably find a better way to end the code if done
                    System.out.println("Min is at row " + box[0] + " col " + box[1]);

        while(box[0] != -1) {
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
                            for(int j = 0; j < solution.length; j++) {
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
                            for(int j = 0; j < copy.length; j++) {
                                System.out.print(copy[i][j] + " ");
                            }
                            System.out.println();
                        }
                        System.out.println();
            box = checkIfDoneOrFindMinBox(copy);
                        System.out.println("Min is at row " + box[0] + " col " + box[1]);
                        
        }

    }
}