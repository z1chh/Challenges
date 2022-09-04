package Kattis.COMP321.A1;

import java.util.Scanner;

public class F {
    public static void main(String[] args) {
        erase();
    }

    private static void erase() {
        // TO-DO
        Scanner scanner = new Scanner(System.in);
        int switches;
        String original, deleted;
        if (scanner.hasNextInt()) {
            switches = scanner.nextInt();
            scanner.nextLine(); // get rid of carriage return
            assert switches > 0 && switches <= 20: "Error: must switch between 1 and 20 times (included)";
            if (scanner.hasNextLine()) {
                original = scanner.nextLine();
                if (scanner.hasNextLine()) {
                    deleted = scanner.nextLine();

                    // If switches is even, then original = deleted. Otherwise, bits must be flipped.
                    int length = original.length();
                    if (length != deleted.length())
                        System.out.println("Deletion failed");
                    else {
                        assert length > 0 && length <= 1000:
                                "Error: file must contain between 1 and 1000 bits (included)";
                        char o, d;
                        for (int i = 0; i < length; i++) {
                            o = original.charAt(i);
                            d = deleted.charAt(i);
                            assert o == '0' || o == '1': "Error: invalid file";
                            assert d == '0' || d == '1': "Error: invalid file";
                            if (o == d && switches % 2 == 1) {
                                System.out.println("Deletion failed");
                                return;
                            }
                            if (o != d && switches % 2 == 0) {
                                System.out.println("Deletion failed");
                                return;
                            }
                        }
                        System.out.println("Deletion succeeded");
                    }
                } else {
                    throw new IllegalArgumentException("Error: input must be an int");
                }
            } else {
                throw new IllegalArgumentException("Error: input must be an int");
            }
        } else {
            throw new IllegalArgumentException("Error: input must be an int");
        }
    }
}
