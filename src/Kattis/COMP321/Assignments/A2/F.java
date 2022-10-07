package Kattis.COMP321.A2;

import java.util.Scanner;

public class F {
    public static void main(String[] args) {
        subSeq();
    }

    private static void subSeq() {
        // Get number of test cases
        Scanner scanner = new Scanner(System.in);
        int testCases = scanner.nextInt();
        scanner.nextLine(); // Get rid of carriage return

        // Test cases
        int[] seq;
        String[] input;
        int length;
        for (int i = 0; i < testCases; i++) {
            // Get input
            scanner.nextLine(); // Get rid of carriage return
            scanner.nextLine(); // Get rid of carriage return
            input = scanner.nextLine().split("\\s");
            length = input.length;
            seq = new int[length];
            for (int j = 0; j < length; j++) {
                seq[j] = Integer.parseInt(input[j]);
            }

            // UH IDK
            // Lazy long inefficient implementation
            int ct = 0, curSum, count = 0;
            while (ct < length) {
                curSum = 0;
                for (int j = ct; j < length; j++) {
                    // TO-DO
                    curSum += seq[j];
                    if (curSum == 47)
                        count++;
                }
                ct++;
            }
            System.out.println(count);
        }
        scanner.close();
    }
}
