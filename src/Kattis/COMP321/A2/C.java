package Kattis.COMP321.A2;

import java.util.ArrayList;
import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        countingStars();
    }

    private static void countingStars() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        ArrayList<String> input, output = new ArrayList<>();
        int lines, lineLength, stars, testCase = 1;
        char c;
        String inputSize = scanner.nextLine();
        String[] sizeValues;

        while(!inputSize.equals("")) {
            sizeValues = inputSize.split("\\s");
//            System.out.println("testCase = " + testCase);
            // Get input size
            lines = Integer.parseInt(sizeValues[0]);
            lineLength = Integer.parseInt(sizeValues[1]);
//            System.out.println("lines = " + lines);
//            System.out.println("lineLength = " + lineLength);

            // Get input
            input = new ArrayList<>();
            for (int i = 0; i < lines; i++) {
                input.add(scanner.nextLine());
            }

            // Look for stars
            stars = 0;
            for (String line: input) {
                for (int i = 0; i < lineLength; i++) {
                    c = line.charAt(i);
                    if (c == '-') {
                        // Check if star was already counted
                        stars++; // TO CHANGE
                    }
                }
            }
            output.add(String.format("Case %d: %d", testCase++, stars));
            System.out.println("NEXT LINE?");
            if (scanner.hasNextLine()) {
                System.out.println("YES");
                inputSize = scanner.nextLine();
            } else
                break;
        }
        output.forEach(System.out::println);
        scanner.close();
    }
}
