package Kattis.COMP321.A1;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class H {
    public static void main(String[] args) {
        t9Spelling();
    }

    private static final HashMap<Character, Integer> LETTERS = new HashMap<>();

    static {
        // Initialize the hashmap
        LETTERS.put('a', 2);
        LETTERS.put('b', 22);
        LETTERS.put('c', 222);
        LETTERS.put('d', 3);
        LETTERS.put('e', 33);
        LETTERS.put('f', 333);
        LETTERS.put('g', 4);
        LETTERS.put('h', 44);
        LETTERS.put('i', 444);
        LETTERS.put('j', 5);
        LETTERS.put('k', 55);
        LETTERS.put('l', 555);
        LETTERS.put('m', 6);
        LETTERS.put('n', 66);
        LETTERS.put('o', 666);
        LETTERS.put('p', 7);
        LETTERS.put('q', 77);
        LETTERS.put('r', 777);
        LETTERS.put('s', 7777);
        LETTERS.put('t', 8);
        LETTERS.put('u', 88);
        LETTERS.put('v', 888);
        LETTERS.put('w', 9);
        LETTERS.put('x', 99);
        LETTERS.put('y', 999);
        LETTERS.put('z', 9999);
        LETTERS.put(' ', 0);
    }

    private static void t9Spelling() {
        // Get input messages
        Scanner scanner = new Scanner(System.in);
        int cases;
        if (scanner.hasNextInt()) {
            cases = scanner.nextInt();
            scanner.nextLine(); // get rid of carriage return
            assert cases > 0 && cases <= 100: "Error: must have between 1 and 100 cases (included)";
            ArrayList<String> messages = new ArrayList<>();
            for (int i = 0; i < cases; i++) {
                if (scanner.hasNextLine()) {
                    messages.add(scanner.nextLine());
                } else {
                    throw new IllegalArgumentException("Error: input must another message");
                }
            }

            // Check that each message is valid
            char c;
            int lastInt, code;
            String msg;
            StringBuilder output;
            for (int i = 0; i < messages.size(); i++) {
                msg = messages.get(i);
                code = LETTERS.get(msg.charAt(0));
                output = new StringBuilder(String.valueOf(code));
                lastInt = code % 10;
                for (int j = 1; j < msg.length(); j++) {
                    c = msg.charAt(j);
                    assert c == ' ' || (c >= 'a' && c <= 'z'): "Error: invalid message";
                    code = LETTERS.get(c);
                    if (lastInt == code % 10)
                        output.append(" ");
                    output.append(code);
                    lastInt = code % 10;
                }
                System.out.printf("Case #%d: %s%n", i + 1, output);
            }
        } else {
            throw new IllegalArgumentException("Error: input must be an int");
        }
    }
}
