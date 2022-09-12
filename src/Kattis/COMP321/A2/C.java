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
        char[][] sky;

        while(scanner.hasNextLine()) {
            inputSize = scanner.nextLine();
            if (inputSize.equals(""))
                break;
            sizeValues = inputSize.split("\\s");
            lines = Integer.parseInt(sizeValues[0]);
            lineLength = Integer.parseInt(sizeValues[1]);

            // Get input
            input = new ArrayList<>();
            for (int i = 0; i < lines; i++) {
                input.add(scanner.nextLine());
            }

            // Create sky matrix
            sky = new char[lines][lineLength];
            for (int i = 0; i < lines; i++) {
                for (int j = 0; j < lineLength; j++) {
                    sky[i][j] = input.get(i).charAt(j);
                }
            }

            // Count stars
            stars = 0;
            for (int i = 0; i < lines; i++) {
                for (int j = 0; j < lineLength; j++) {
                    c = sky[i][j];
                    if (c == '-') {
                        stars++;
                        eraseStar(sky, i, j, lines, lineLength);
                    }
                }
            }

            // Add test case results
            output.add(String.format("Case %d: %d", testCase++, stars));
        }
        output.forEach(System.out::println);
    }

    private static void eraseStar(char[][] sky, int x, int y, int lines, int lineLength) {
        // Erase current star piece
        sky[x][y] = '#';

        // Check left piece
        if (y > 0)
            if (sky[x][y - 1] == '-')
                eraseStar(sky, x, y - 1, lines, lineLength);

        // Check right piece
        if (y + 1 < lineLength)
            if (sky[x][y + 1] == '-')
                eraseStar(sky, x, y + 1, lines, lineLength);

        // Check top piece
        if (x > 0)
            if (sky[x - 1][y] == '-')
                eraseStar(sky, x - 1, y, lines, lineLength);

        // Check bottom piece
        if (x + 1 < lines)
            if (sky[x + 1][y] == '-')
                eraseStar(sky, x + 1, y, lines, lineLength);
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
