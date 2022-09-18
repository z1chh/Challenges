package Kattis.COMP321.A3;

import java.util.Arrays;
import java.util.Scanner;

public class D {
    public static void main(String[] args) {
        //fruitBaskets();
        combinations(4);
        combinations(9);
    }

    private static void fruitBaskets() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        int fruitKinds, allBaskets;
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
        allBaskets = getAllBaskets(fruitWeights, fruitKinds);

        // Print total sum of all baskets
        System.out.println(allBaskets);
    }

    private static int getAllBaskets(int[] fruitWeights, int fruitKinds) {
        int allBaskets = 0, curWeight;
        // To-Do
        // C(n, r) = n! / ((n-r)! r!)
        // Get the C(n, r) possible combinations of fruits
        int[][] combs = combinations(fruitKinds);

        // Check if each combination exceeds 200g
        for (int[] comb : combs) {
            curWeight = 0;
            for (int index: comb) {
                curWeight += fruitWeights[index];
                if (curWeight >= 200) {
                    allBaskets += curWeight;
                }
            }
        }

        return allBaskets;
    }

    private static int[][] combinations(int n) {
        // C(n, r) = n! / ((n-r)! r!)
        int total = 0, cur, combs, ct = 0;
        int[] nCr = new int[n];
        for (int i = 1; i <= n / 2; i++) {
            // Reset variables
            cur = n;
            combs = 1;

            // Get total number of possible combinations
            if (i > n - i) {
                while (cur > i)
                    combs *= cur--;
                cur = n - i;
            } else {
                while (cur > n - i)
                    combs *= cur--;
                cur = i;
            }

            // Divide
            while (cur > 1)
                combs /= cur--;

            nCr[i - 1] = combs;
            nCr[n - 1 - i] = combs;
        }
        nCr[n - 1] = 1;

        for (int i = 0; i < n; i++) {
            total += nCr[i];
        }

        // Get each combination
        int[][] toReturn = new int[total][];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < nCr[i]; j++) {
                toReturn[ct++] = new int[]{j};
            }
        }

        return toReturn;
    }
}
