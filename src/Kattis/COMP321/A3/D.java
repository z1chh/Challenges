package Kattis.COMP321.A3;

import java.util.Scanner;

public class D {
    public static void main(String[] args) {
        closestSums();
    }

    private static void closestSums() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        int fruitKinds, curWeight, allBaskets = 0;
        String[] input;
        int[] fruitWeights;

        // Get number of fruit kinds
        fruitKinds = scanner.nextInt();
        scanner.nextLine(); // Get rid of carriage return

        // Get fruit weights
        input = scanner.nextLine().split("\\s");
        fruitWeights = new int[fruitKinds];
        for (int i = 0; i < fruitKinds; i++) {
            fruitWeights[i] = Integer.parseInt(input[i]);
        }

        // Get baskets
        for (int i = 0; i < fruitKinds - 1; i++) {
            curWeight = fruitWeights[i];
            if (curWeight >= 200) {
                allBaskets += curWeight;
            }
            for (int j = i + 1; j < fruitKinds; j++) {
                curWeight += fruitWeights[j];
                if (curWeight >= 200) {
                    allBaskets += curWeight;
                }
            }
        }

        // Check for single fruit itself
        if (fruitWeights[fruitKinds - 1] >= 200)
            allBaskets += fruitWeights[fruitKinds - 1];

        // Print total sum of all baskets
        System.out.println(allBaskets);
    }
}
