package Kattis.COMP321.A3;

import java.util.HashMap;
import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        telephones();
    }

    private static void telephones() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        int numCalls, numIntervals, operators, curOperators, start, duration, curTime;
        String[] input;
        HashMap<Integer, Integer> dp;

        // Get test case
        input = scanner.nextLine().split("\\s");

        // Get number of phone calls and intervals
        numCalls = Integer.parseInt(input[0]);
        numIntervals = Integer.parseInt(input[1]);

        while (numCalls != 0 && numIntervals != 0) {
            // Get phone calls
            dp = new HashMap<>();
            for (int i = 0; i < numCalls; i++) {
                input = scanner.nextLine().split("\\s");
                start = Integer.parseInt(input[2]);
                duration = Integer.parseInt(input[3]);

                // Increment number of active phone calls during [start, start + duration[
                for (int j = start; j < start + duration; j++) {
                    if (dp.containsKey(j))
                        dp.put(j, dp.get(j) + 1);
                    else
                        dp.put(j, 1);
                }
            }

            // Get interval values
            for (int i = 0; i < numIntervals; i++) {
                input = scanner.nextLine().split("\\s");
                start = Integer.parseInt(input[0]);
                duration = Integer.parseInt(input[1]);
                curTime = start;
                operators = dp.getOrDefault(curTime, 0);

                // Look for minute with most phone calls
                for (int j = start; j < start + duration; j++) {
                    curOperators = dp.getOrDefault(j, 0);
                    if (curOperators > operators)
                        operators = curOperators;
                }

                // Output result
                System.out.println(operators);
            }

            // Get next test case
            input = scanner.nextLine().split("\\s");

            // Get number of phone calls and intervals
            numCalls = Integer.parseInt(input[0]);
            numIntervals = Integer.parseInt(input[1]);
        }
    }
}
