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
        int numCalls, numIntervals, operators, curOperators;
        String[] input;
        int[][] phoneCalls, intervals;
        int[] call, interval;
        HashMap<Integer, Integer> dp;

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
                call = new int[2];
                for (int j = 2; j < 4; j++) {
                    call[j - 2] = Integer.parseInt(input[j]);
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

            // Get operator per time unit
            dp = new HashMap<>();
            for (int[] curCall: phoneCalls) {
                for (int i = curCall[0]; i < curCall[0] + curCall[1]; i++) {
                    if (dp.containsKey(i))
                        dp.put(i, dp.get(i) + 1);
                    else
                        dp.put(i, 1);
                }
            }

            // Get interval values
            int curTime;
            for (int[] curInterval: intervals) {
                curTime = curInterval[0];
                operators = dp.getOrDefault(curTime, 0);

                for (int i = curTime; i < curTime + curInterval[1]; i++) {
                    curOperators = dp.getOrDefault(i, 0);
                    if (curOperators > operators)
                        operators = curOperators;
                }
                System.out.println(operators);
            }

            // Get next test case
            input = scanner.nextLine().split("\\s");
        }
    }
}
