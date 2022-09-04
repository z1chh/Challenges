package Kattis.COMP321.A1;

import java.util.ArrayList;
import java.util.Scanner;

public class G {
    public static void main(String[] args) {
        timeBomb();
    }

    private static void timeBomb() {
        // Get input
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> lines = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            if (scanner.hasNextLine())
                lines.add(scanner.nextLine());
            else
                throw new IllegalArgumentException("Error: input must have 5 lines");
        }
        assert lines.size() == 5: "Error: input must have 5 lines";
        int length = lines.get(0).length();
        for (String line: lines)
            assert line.length() == length: "Error: all lines must have same length";

        // Organize into numbers
        ArrayList<String> numbers = new ArrayList<>();
        StringBuilder number;
        int pos = 0;
        while (pos < length) {
            number = new StringBuilder();
            for (int i = 0 ; i < 5; i++)
                number.append(lines.get(i), pos, pos + 3);
            numbers.add(number.toString());
            pos += 4;
        }

        // Get the actual number
        int value = 0, curValue, counter = numbers.size() - 1;
        boolean firstDigit = true;
        for (String nb: numbers) {
            curValue = getNumber(nb);
            if (curValue == -1) {
                System.out.println("BOOM!!");
                return;
            } else {
                if (!firstDigit || curValue != 0) {
                    value += curValue * Math.pow(10, counter);
                    firstDigit = false;
                }
                counter--;
            }
        }

        // Check if number divisible by 6
        if (value % 6 == 0)
            System.out.println("BEER!!");
        else
            System.out.println("BOOM!!");
    }

//    private static int getNumber(String number) {
//        if (number == null || number.length() != 15)
//            return -1;
//        switch (number) {
//            case ("**** ** ** ****"):
//                return 0;
//            case ("  *  *  *  *  *"):
//                return 1;
//            case ("***  *****  ***"):
//                return 2;
//            case ("***  ****  ****"):
//                return 3;
//            case ("* ** ****  *  *"):
//                return 4;
//            case ("****  ***  ****"):
//                return 5;
//            case ("****  **** ****"):
//                return 6;
//            case ("***  *  *  *  *"):
//                return 7;
//            case ("**** ***** ****"):
//                return 8;
//            case ("**** ****  ****"):
//                return 9;
//            default: return -1;
//        }
//    }

    private static int getNumber(String number) {
        if (number == null || number.length() != 15)
            return -1;
        return switch (number) {
            case ("**** ** ** ****") -> 0;
            case ("  *  *  *  *  *") -> 1;
            case ("***  *****  ***") -> 2;
            case ("***  ****  ****") -> 3;
            case ("* ** ****  *  *") -> 4;
            case ("****  ***  ****") -> 5;
            case ("****  **** ****") -> 6;
            case ("***  *  *  *  *") -> 7;
            case ("**** ***** ****") -> 8;
            case ("**** ****  ****") -> 9;
            default -> -1;
        };
    }
}
