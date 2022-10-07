package Kattis.COMP321.A1;

import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        sortTwoNumbers();
    }

    private static void sortTwoNumbers() {
        Scanner scanner = new Scanner(System.in);
        int input1, input2;
        if (scanner.hasNextInt()) {
            input1 = scanner.nextInt();
            if (scanner.hasNextInt()) {
                input2 = scanner.nextInt();
                System.out.printf("%d%n%d%n", Math.min(input1, input2),
                        Math.max(input1, input2));
            } else {
                throw new IllegalArgumentException("Error: input must be an int");
            }
        } else {
            throw new IllegalArgumentException("Error: input must be an int");
        }
    }
}
