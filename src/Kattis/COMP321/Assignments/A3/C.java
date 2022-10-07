package Kattis.COMP321.A3;

import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        telephones();
    }

    private static void telephones() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        int numCalls, numIntervals, operators, start, duration, startOfCall, endOfCall;
        String[] input;
        int[][] calls;

        // Get test case
        input = scanner.nextLine().split("\\s");

        // Get number of phone calls and intervals
        numCalls = Integer.parseInt(input[0]);
        numIntervals = Integer.parseInt(input[1]);

        while (numCalls != 0 && numIntervals != 0) {
            // Get phone calls
            calls = new int[numCalls][];
            for (int i = 0; i < numCalls; i++) {
                input = scanner.nextLine().split("\\s");
                start = Integer.parseInt(input[2]);
                duration = Integer.parseInt(input[3]);

                // Increment number of active phone calls during [start, start + duration[
                calls[i] = new int []{start, start + duration};
            }

            // Get interval values
            for (int i = 0; i < numIntervals; i++) {
                input = scanner.nextLine().split("\\s");
                start = Integer.parseInt(input[0]);
                duration = Integer.parseInt(input[1]);
                operators = 0;

                for (int[] call: calls) {
                    startOfCall = call[0];
                    endOfCall = call[1];
                    if (startOfCall < start && start < endOfCall)
                        operators++;
                    else if (start <= startOfCall && startOfCall < start + duration)
                        operators++;
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
