package Kattis.COMP321.A2;

import java.util.LinkedList;
import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        doorMan();
    }

    private static void doorMan() {
        // Read input
        Scanner scanner = new Scanner(System.in);
        int maxDifference = scanner.nextInt(), totalLength, length;
        scanner.nextLine(); // Get rid of carriage return
        String input = scanner.nextLine();
        totalLength = input.length();
        length = totalLength;

        // In case he cannot do nothing
        if (maxDifference == 0) {
            System.out.println(0);
            return;
        }

        // In case he can do everything
        if (maxDifference >= totalLength) {
            System.out.println(input.length());
            return;
        }

        // Variables
        int men = 0, women = 0;
        char c, next;
        LinkedList<Character> line = new LinkedList<>();

        // Initialize line
        for (int i = 0; i < totalLength; i++) {
            line.add(input.charAt(i));
        }

        while (length > 0) {
            c = line.getFirst();
            if (c == 'M') {
                // Check if threshold reached
                if (men - women >= maxDifference) {
                    if (line.size() < 2) {
                        // No one in line to go in before
                        System.out.println(men + women);
                        return;
                    }
                    next = line.get(1);
                    if (next == 'W') {
                        // Let the woman go in first
                        line.remove(1);
                        women++;
                        length--;
                    } else { // (next == 'M')
                        // Screwed
                        System.out.println(men + women);
                        return;
                    }
                } else { // Not lost yet
                    men++;
                    line.removeFirst();
                    length--;
                }
            } else {
                // Check if threshold reached
                if (women - men >= maxDifference) {
                    if (line.size() < 2) {
                        // No one in line to go in before
                        System.out.println(men + women);
                        return;
                    }
                    next = line.get(1);
                    if (next == 'M') {
                        // Let the man go in first
                        line.remove(1);
                        men++;
                        length--;
                    } else { // (next == 'M')
                        // Screwed
                        System.out.println(men + women);
                        return;
                    }
                } else { // Not lost yet
                    women++;
                    line.removeFirst();
                    length--;
                }
            }
        }
        assert men + women == totalLength: "Error: everyone got in but wrong value";
        System.out.println(men + women);
    }
}
