package Kattis.COMP321.A2;

import java.util.Scanner;

public class A {
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
        char next = queue.charAt(0), onHold = 'N', dominantSex = next == 'M'? 'M': 'W';

        // Letting people in
        for (int i = 1; i < queue.length(); i++) {
            next = queue.charAt(i);
            if (dominantSex == 'M') {
                if (difference >= maxDifference && next == 'M') {
                    if (onHold == 'M') {
                        return peopleIn;
                    } else if (onHold == 'W') {
                        onHold = 'N';
                        peopleIn++;
                        difference--;
                        if (difference == 0) {
                            dominantSex = 'N';
                        }
                    } else { // onHold == 'N'
                        onHold = next;
                    }
                } else {
                    peopleIn++;
                    if (next == 'M') {
                        difference++;
                    } else { // next == 'W'
                        difference--;
                        if (difference == 0) {
                            dominantSex = 'N';
                        }
                    }
                }
            } else if (dominantSex == 'W') {
                if (difference >= maxDifference && next == 'W') {
                    if (onHold == 'W') {
                        return peopleIn;
                    } else if (onHold == 'M') {
                        onHold = 'N';
                        peopleIn++;
                        difference--;
                        if (difference == 0) {
                            dominantSex = 'N';
                        }
                    } else { // onHold == 'N'
                        onHold = next;
                    }
                } else {
                    peopleIn++;
                    if (next == 'W') {
                        difference++;
                    } else { // next == 'M'
                        difference--;
                        if (difference == 0) {
                            dominantSex = 'N';
                        }
                    }
                }
            } else { // dominantSex == 'N'
                assert difference == 0: "Error: difference should be 0";
                peopleIn++;
                difference++;
                dominantSex = next;
            }
        }
        assert peopleIn == queue.length(): "Error: everyone got in but incorrect value";
        return peopleIn;
    }
}
