package Kattis.COMP321.A2;

import java.util.Scanner;

public class A {
    private enum Sex {
        MALE, FEMALE, NONE;

        public static Sex getSex(char c) {
            switch (c) {
                case ('M'):
                    return MALE;
                case ('W'):
                    return FEMALE;
                case ('N'):
                    return NONE;
                default:
                    throw new IllegalArgumentException("Error: char must be 'M', 'W' or 'N'");
            }
        }
    }
    public static void main(String[] args) {
        System.out.println(doorMan());
    }

    private static int doorMan() {
        // Read input
        Scanner scanner = new Scanner(System.in);
        int maxDifference = scanner.nextInt();
        scanner.nextLine(); // Get rid of carriage return
        String queue = scanner.nextLine();

        // In case he cannot do nothing
        if (maxDifference == 0)
            return 0;

        // In case he can do everything
        if (maxDifference >= queue.length())
            return queue.length();

        // Get first person
        int difference = 1, peopleIn = 1;
        char next = queue.charAt(0);
        Sex onHold = Sex.NONE, dominantSex = Sex.getSex(next);

        // Letting people in
        for (int i = 1; i < queue.length(); i++) {
            next = queue.charAt(i);

            // Check if about to lose track of count
            if (difference >= maxDifference && Sex.getSex(next) == dominantSex) {
                // About to lose track of count
                if (onHold == dominantSex)
                    return peopleIn;
                else if (onHold == Sex.NONE)
                    onHold = dominantSex;
                else { // Opposite sex
                    onHold = Sex.NONE;
                    peopleIn++;
                    difference--;
                    if (difference == 0) {
                        dominantSex = Sex.NONE;
                    }
                }
            } else {
                peopleIn++;
                if (Sex.getSex(next) == dominantSex) {
                    difference++;
                } else {
                    if (dominantSex == Sex.NONE) {
                        dominantSex = Sex.getSex(next);
                        assert difference == 0: "Error: sex tied but difference is not 0";
                        difference = 1;
                    } else {
                        difference--;
                        if (difference == 0) {
                            dominantSex = Sex.NONE;
                        }
                    }
                }
            }
        }
        assert peopleIn == queue.length(): "Error: everyone got in but incorrect value";
        scanner.close();
        return peopleIn;
    }
}
