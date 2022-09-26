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
        int numBreaks, breakPrice, tmp, bestProfit;
        int[] studentsPerBreak;
        int[][] sequences;

        // Get input
        input = scanner.nextLine().split("\\s");
        numBreaks = Integer.parseInt(input[0]);
        breakPrice = Integer.parseInt(input[1]);
        studentsPerBreak = new int[numBreaks];

        for (int i = 0; i < numBreaks; i++) {
            studentsPerBreak[i] = scanner.nextInt();
        }


        // Find best sequence
        bestProfit = -1;
        sequences = new int[numBreaks][numBreaks];

        // Initialize pricePerBreak array
        for (int i = 0; i < numBreaks; i++) {
            tmp = studentsPerBreak[i] - breakPrice;
            sequences[0][i] = tmp;
            if (tmp > bestProfit)
                bestProfit = tmp;
        }

        for (int i = 1; i < numBreaks; i++) {
            for (int j = i; j < numBreaks; j++) {
                tmp = sequences[i - 1][j - 1] + sequences[0][j];
                sequences[i][j] = tmp;
                if (tmp > bestProfit)
                    bestProfit = tmp;
            }
        }

        // Output result
        System.out.println(bestProfit);
    }
}
