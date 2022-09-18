package Kattis.COMP321.A3;

import java.util.Scanner;

public class D {
    public static void main(String[] args) {
        fruitBaskets();
    }

    private static void fruitBaskets() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        int fruitKinds;
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

        // Print total sum of all baskets
        System.out.println(getAllBaskets(fruitWeights, fruitKinds));
    }

    private static int getAllBaskets(int[] fruitWeights, int fruitKinds) {
        int allBaskets = 0, curWeight;
        // Get the C(n, r) possible combinations of fruits
        int[] arr = new int[fruitKinds];
        int ct = fruitKinds - 1;
        while (true) {
            if (arr[ct] == 0) {
                arr[ct] = 1;
            } else {
                int c = 1;
                while (ct - c >= 0)
                    if (arr[ct - c] == 0) {
                        arr[ct - c] = 1;
                        for (int i = ct - c + 1; i < fruitKinds; i++) {
                            arr[i] = 0;
                        }
                        break;
                    } else {
                        c++;
                    }
                if (ct - c < 0)
                    break;
            }

            // Compute weight for current combination
            curWeight = 0;
            for (int i = 0; i < fruitKinds; i++) {
                if (arr[i] == 1) {
                    curWeight += fruitWeights[i];
                }
            }

            // Check if current combination is at least 200g
            if (curWeight >= 200)
                allBaskets += curWeight;
        }
        return allBaskets;
    }
}
