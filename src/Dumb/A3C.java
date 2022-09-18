package Dumb;

import java.util.Scanner;

public class A3C {
    public static void main(String[] args) {
        telephones();
    }

    private static void telephones() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        int numCalls, numIntervals, operators, curOperators, start, end;
        String[] input;
        int[][] phoneCalls, intervals;
        int[] call, interval;

        // Get test case
        input = scanner.nextLine().split("\\s");
        while (!input[0].equals("0") && !input[1].equals("0")) {
            // Get number of phone calls and intervals
            numCalls = Integer.parseInt(input[0]);
            numIntervals = Integer.parseInt(input[1]);

            // Get phone calls
            phoneCalls = new int[numCalls][];
            for (int i = 0; i < numCalls; i++) {
                input = scanner.nextLine().split("\\s");
                call = new int[4];
                for (int j = 0; j < 4; j++) {
                    call[j] = Integer.parseInt(input[j]);
                }
                phoneCalls[i] = call;
            }

            // Get spying intervals
            intervals = new int[numIntervals][];
            for (int i = 0; i < numIntervals; i++) {
                input = scanner.nextLine().split("\\s");
                interval = new int[2];
                for (int j = 0; j < 2; j++) {
                    interval[j] = Integer.parseInt(input[j]);
                }
                intervals[i] = interval;
            }

            // Get number of operators required
            for (int[] curInterval: intervals) {
                operators = 0;
                for (int i = curInterval[0]; i < curInterval[0] + curInterval[1]; i++) {
                    curOperators = 0;
                    for (int[] curCall: phoneCalls) {
                        start = curCall[2];
                        end = start + curCall[3];
                        if (i >= start && i < end)
                            curOperators++;
                    }
                    if (curOperators > operators)
                        operators = curOperators;
                    if (operators >= numCalls)
                        break;
                }
                System.out.println(operators);
            }

            // Get next test case
            input = scanner.nextLine().split("\\s");
        }
    }
}
