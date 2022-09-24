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
        String input;
        String[] numbersArray;
        int totalStones, numbers;
        int[] removedStones;

        while (!(input = scanner.nextLine()).equals("")) {
            // Get input
            numbersArray = input.split("\\s");
            totalStones = Integer.parseInt(numbersArray[0]);
            numbers = Integer.parseInt(numbersArray[1]);
            removedStones = new int[numbers];
            for (int i = 0; i < numbers; i++) {
                removedStones[i] = Integer.parseInt(numbersArray[i + 2]);
            }
        }
    }
}
