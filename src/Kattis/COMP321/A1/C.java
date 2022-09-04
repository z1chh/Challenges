package Kattis.COMP321.A1;

import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        oddity();
    }

    private static void oddity() {
        Scanner scanner = new Scanner(System.in);
        int cases, input;
        String output = "";
        if (scanner.hasNextInt()) {
            cases = scanner.nextInt();
            assert cases > 0 && cases <= 20: "Error: must have between 1 and 20 cases (included)";
            for (int i = 0; i < cases; i++) {
                if (scanner.hasNextInt()) {
                    input = scanner.nextInt();
                    output += String.format("%d is %s%n", input, input % 2 == 0? "even": "odd");
                } else {
                    throw new IllegalArgumentException("Error: input must be an int");
                }
            }
            System.out.println(output);
        } else {
            throw new IllegalArgumentException("Error: input must be an int");
        }
    }
}