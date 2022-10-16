package Kattis.COMP321.A1;

import java.util.ArrayList;
import java.util.Scanner;

public class E {
    public static void main(String[] args) {
        quickBrownFox();
    }

    private static void quickBrownFox() {
        Scanner scanner = new Scanner(System.in);
        int cases;
        ArrayList<String> phrases = new ArrayList<>();
        if (scanner.hasNextInt()) {
            cases = scanner.nextInt();
            scanner.nextLine(); // Because of nextInt() - get rid of carriage return
            assert cases > 0 && cases <= 50: "Error: must have between 1 and 50 cases (included)";
            for (int i = 0; i < cases; i++) {
                if (scanner.hasNextLine()) {
                    phrases.add(scanner.nextLine());
                } else {
                    throw new IllegalArgumentException("Error: must input a sentence");
                }
            }
            ArrayList<Character> ascii, missing;
            for(String phrase: phrases) {
                ascii = getLetters(phrase);
                if (ascii.size() == 26)
                    System.out.println("pangram");
                else {
                    // Output missing letters
                    missing = getMissingLetters(ascii);
                    System.out.print("missing ");
                    missing.forEach(System.out::print);
                    System.out.println();
                }
            }
        } else {
            throw new IllegalArgumentException("Error: input must be an int");
        }
    }

    private static ArrayList<Character> getLetters(String phrase) {
        assert phrase != null && phrase.length() > 0 && phrase.length() <= 100: "Error: invalid phrase";
        ArrayList<Character> ascii = new ArrayList<>();
        for (int i = 0; i < phrase.length(); i++) {
            char c = phrase.charAt(i);
            if (c >= 'A' && c <= 'Z')
                c = (char) ( c + 32);
            if (!ascii.contains(c) && c >= 'a' && c <= 'z')
                ascii.add(c);
        }
        return ascii;
    }

    private static ArrayList<Character> getMissingLetters(ArrayList<Character> letters) {
        assert letters != null: "Error: array cannot be null";
        ArrayList<Character> missing = new ArrayList<>();
        for (int i = 'a'; i <= 'z'; i++) {
            if (!letters.contains((char) i))
                missing.add((char) i);
        }
        return missing;
    }
}
