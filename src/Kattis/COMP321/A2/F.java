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
        for (int i = 0; i < testCases; i++) {
            // Get input
            scanner.nextLine(); // Get rid of carriage return
            input = scanner.nextLine().split("\\s");
            seq = new int[input.length];
            for (int j = 0; j < input.length; j++) {
                seq[j] = Integer.parseInt(input[j]);
            }

            // Uh idk
        }
    }
}
