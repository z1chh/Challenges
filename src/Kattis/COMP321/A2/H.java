package Kattis.COMP321.A2;

import java.util.ArrayList;
import java.util.Scanner;

public class H {
    public static void main(String[] args) {
        restaurant();
    }

    private static void restaurant() {
        Scanner scanner = new Scanner(System.in);
        int numOperations;
        while (true) {
            // Get input
            numOperations = scanner.nextInt();
            scanner.nextLine(); // Get rid of carriage return
            if (numOperations == 0)
                return;

            // Get operations
            ArrayList<String> operations = new ArrayList<>();
            for (int i = 0; i < numOperations; i++) {
                operations.add(scanner.nextLine());
            }

            //
        }

    }
}
