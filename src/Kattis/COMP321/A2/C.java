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
        String inputSize;
        String[] sizeValues;

        while(scanner.hasNextLine()) {
            inputSize = scanner.nextLine();
            if (inputSize.equals(""))
                break;
            System.out.println("inputSize = " + inputSize);
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
            for (int i = 0; i < lines; i++) {
                String line = input.get(i);
                for (int j = 0; j < lineLength; j++) {
                    c = line.charAt(j);
                    if (c == '-') {
                        // Check if star was already counted
                        if (j > 0 && line.charAt(j - 1) == '-')
                            continue;
                        if (i > 0 && input.get(i - 1).charAt(j) == '-')
                            continue;
                        if (i > 0 && j + 2 < lineLength && input.get(i - 1).charAt(j + 1) == '-')
                            continue;
                        stars++;
                    }
                }
            }
            output.add(String.format("Case %d: %d", testCase++, stars));
        }
        output.forEach(System.out::println);
        scanner.close();
    }
}

/*
INPUT
10 20
#################---
##-###############--
#---################
##-#################
########---#########
#######-----########
########---#########
##################--
#################---
##################-#
3 10
#-########
----------
#-########

 */
