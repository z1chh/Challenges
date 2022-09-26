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
        int numBreaks, breakPrice, startIndex, size, curProfit, bestProfit;
        int[] studentsPerBreak, pricePerBreak;

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

        // Initialize pricePerBreak array
        pricePerBreak = new int[numBreaks];
        for (int i = 0; i < numBreaks; i++) {
            pricePerBreak[i] = studentsPerBreak[i] - breakPrice;
        }

        for (int i = 0; i < numBreaks; i++) {
            for (int j = i; j < numBreaks; j++) {
                startIndex = j;
                size = i;
                curProfit = 0;
                while (size-- >= 0) {
                    curProfit += pricePerBreak[startIndex--];
                }
                if (curProfit > bestProfit)
                    bestProfit = curProfit;
            }
        }

        // Output result
        System.out.println(bestProfit);
    }
}
