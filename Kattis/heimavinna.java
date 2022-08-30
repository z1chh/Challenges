import java.util.ArrayList;
import java.util.Scanner;

public class heimavinna {
    public static void main(String[] args) {
        System.out.println(homework());
    }

    public static int homework() {
        Scanner scanner = new Scanner(System.in);
        if (scanner.hasNext()) {
            String input = scanner.nextLine();
            String nb = "";
            String nb2 = "";
            int problems = 0;
            boolean range = false;

            // Assume input must start with a number
            assert (input.charAt(0) >= 48 && input.charAt(0) <= 57): "Error: must start with a number";

            // Main
            for (int i = 0; i < input.length(); i++) {
                char c = input.charAt(i);
                if (c >= 48 && c <= 57) {
                    if (range)
                        nb2 += c;
                    else
                        nb += c;
                } else if (c == 59) {
                    if (range) {
                        problems += Integer.parseInt(nb2) - Integer.parseInt(nb) + 1;
                        nb = "";
                        nb2 = "";
                        range = false;
                    } else {
                        nb = "";
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
                problems += Integer.parseInt(nb2) - Integer.parseInt(nb) + 1;
            else
                problems++;

            return problems;
        } else {
            throw new IllegalArgumentException("Error: input missing");
        }
    }
}
