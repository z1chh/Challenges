package Kattis.COMP321.A3;

import java.util.ArrayList;
import java.util.Scanner;

class B {
    public static void main(String[] args) {
        closestSums();
    }

    private static void closestSums() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        int ints, sums, caseNumber = 1;
        int[] numList, sumList, answers;
        String input;
        StringBuilder output;
        ArrayList<String> outputs = new ArrayList<>();

        while (scanner.hasNextLine()) {
            // Check if there is another test case
            input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }

            ints = Integer.parseInt(input);

            // Get numbers
            numList = new int[ints];
            for (int i = 0; i < ints; i++) {
                numList[i] = scanner.nextInt();
                scanner.nextLine(); // Get rid of carriage return
            }

            // Get number of sums
            sums = scanner.nextInt();
            scanner.nextLine(); // Get rid of carriage return

            // Get sums
            sumList = new int[sums];
            for (int i = 0; i < sums; i++) {
                sumList[i] = scanner.nextInt();
                scanner.nextLine(); // Get rid of carriage return
            }

            // Get sums answers
            answers = new int[sums];
            output = new StringBuilder(String.format("Case %d:%n", caseNumber++));

            for (int i = 0; i < sums; i++) {
                answers[i] = closestSum(numList, ints, sumList[i]);
                output.append(String.format("Closest sum to %d is %d.%n", sumList[i], answers[i]));
            }
            outputs.add(output.toString());
        }

        // Print out output
        outputs.forEach(System.out::println);
    }

    private static int closestSum(int[] numList, int size, int sum) {
        int closest = numList[0] + numList[1], cur;
        for (int i = 0; i < size - 1; i++) {
            for (int j = i + 1; j < size; j++) {
                cur = numList[i] + numList[j];
                if (cur == sum)
                    return sum;
                if (Math.abs(cur - sum) < Math.abs(closest - sum))
                    closest = cur;
            }
        }
        return closest;
    }
}
