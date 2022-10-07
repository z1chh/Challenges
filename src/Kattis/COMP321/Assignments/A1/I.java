package Kattis.COMP321.A1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class I {
    public static void main(String[] args) {
        permutationEncryption();
    }

    private static final Scanner SCANNER = new Scanner(System.in);

    private static void permutationEncryption() {
        int encryptionsDone = 0;
        String newMessage;
        ArrayList<String> newMessages = new ArrayList<>();
        while(SCANNER.hasNextLine()) {
            newMessage = singleEncryption();
            if (newMessage == null)
                break;
            newMessages.add(newMessage);
            if (++encryptionsDone > 150)
                throw new IllegalArgumentException("Error: can only encrypt 150 messages at a time");
        }
        newMessages.forEach(System.out::println);
    }

    private static String singleEncryption() {
        String keyString, message, digit;
        StringBuilder newMessage = new StringBuilder(), substring;
        int keyLength;
        if (SCANNER.hasNextLine()) {
            keyString = SCANNER.nextLine();

            // Extract key
            String[] digits = keyString.split(" ");

            // Check that key length is valid
            try {
                keyLength = Integer.parseInt(digits[0]);
                assert keyLength >= 0 && keyLength <= 20: "Error: key length must be between 1 and 20 (included)";
                if (keyLength == 0)
                    return null;
                assert digits.length == keyLength + 1: "Error: invalid key length";
            } catch (NumberFormatException nfe) {
                throw new NumberFormatException("Error: invalid key length");
            }
            if (SCANNER.hasNextLine()) {
                message = SCANNER.nextLine();

                // Check that key itself is valid
                ArrayList<Integer> key = new ArrayList<>();
                for (int i = 1; i < digits.length; i++) {
                    try {
                        digit = digits[i];
                        key.add(Integer.parseInt(digit));
                    } catch (NumberFormatException nfe) {
                        throw new NumberFormatException("Error: invalid key value");
                    }
                }
                ArrayList<Integer> toCheckValidity = new ArrayList<>(key);
                Collections.sort(toCheckValidity);
                for (int i = 0; i < toCheckValidity.size(); i++) {
                    assert i + 1 == toCheckValidity.get(i):
                            String.format("Error: key must contain integers between 1 and %d", toCheckValidity.size());
                }

                // Create new message
                int diff;
                for (int i = 0; i < message.length(); i += keyLength) {
                    diff = i + keyLength - message.length();
                    if (diff >= 0) {
                        substring = new StringBuilder(message.substring(i));
                        substring.append(" ".repeat(diff));
                    } else
                        substring = new StringBuilder(message.substring(i, i + keyLength));
                    for (int j = 0; j < keyLength; j++) {
                        if (key.get(j) - 1 >= substring.length())
                            newMessage.append(" ");
                        else
                            newMessage.append(substring.charAt(key.get(j) - 1));
                    }
                }
                return String.format("'%s'", newMessage);
            } else {
                throw new IllegalArgumentException("Error: must input message");
            }
        } else {
            throw new IllegalArgumentException("Error: must input key");
        }
    }
}
