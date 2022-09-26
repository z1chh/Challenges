package Kattis.COMP321.A4;

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        radioCommercials();
    }

    private static void radioCommercials() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        String[] input;
        int numBreaks, breakPrice;
        int[] studentsPerBreak;

        // Get input
        input = scanner.nextLine().split("\\s");
        numBreaks = Integer.parseInt(input[0]);
        breakPrice = Integer.parseInt(input[1]);
        studentsPerBreak = new int[numBreaks];

        for (int i = 0; i < numBreaks; i++) {
            studentsPerBreak[i] = scanner.nextInt();
        }

        // Find best sequence
        // UH DP?
    }
}
