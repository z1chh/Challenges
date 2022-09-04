package Kattis.Website;

import java.util.Scanner;

public class heimavinna {
    public static void main(String[] args) {
        System.out.println(homework());
    }

    public static int homework() {
        Scanner scanner = new Scanner(System.in);
        if (scanner.hasNext()) {
            String input = scanner.nextLine();
            StringBuilder nb = new StringBuilder();
            StringBuilder nb2 = new StringBuilder();
            int problems = 0;
            boolean range = false;

            // Assume input must start with a number
            assert (input.charAt(0) >= 48 && input.charAt(0) <= 57): "Error: must start with a number";

            // Main
            for (int i = 0; i < input.length(); i++) {
                char c = input.charAt(i);
                if (c >= 48 && c <= 57) {
                    if (range)
                        nb2.append(c);
                    else
                        nb.append(c);
                } else if (c == 59) {
                    if (range) {
                        problems += Integer.parseInt(nb2.toString()) - Integer.parseInt(nb.toString()) + 1;
                        nb = new StringBuilder();
                        nb2 = new StringBuilder();
                        range = false;
                    } else {
                        nb = new StringBuilder();
                        problems++;
                    }
                } else if (c == 45) {
                    assert !range: "Error: cannot have two dashes in a row";
                    range = true;
                } else {
                    throw new IllegalArgumentException("Error: invalid input");
                }
            }

            // Last input
            if (range)
                problems += Integer.parseInt(nb2.toString()) - Integer.parseInt(nb.toString()) + 1;
            else
                problems++;

            return problems;
        } else {
            throw new IllegalArgumentException("Error: input missing");
        }
    }
}
