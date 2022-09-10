package Kattis.COMP321.A2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class E {
    public static void main(String[] args) {
        virtualFriends();
    }

    private static void virtualFriends() {
        // Get number of test cases
        Scanner scanner = new Scanner(System.in);
        int testCases = scanner.nextInt();
        scanner.nextLine(); // Get rid of carriage return

        // Test case
        String friend1, friend2;
        int numFriendshipsFormed;
        ArrayList<String> friendshipsFormed;
        for (int i = 0; i < testCases; i++) {
            // Get new friendships
            numFriendshipsFormed = scanner.nextInt();
            friendshipsFormed = new ArrayList<>();
            HashMap<String, ArrayList<String>> friendCircles = new HashMap<>();
            scanner.nextLine(); // Get rid of carriage return
            for (int j = 0; j < numFriendshipsFormed; j++) {
                friendshipsFormed.add(scanner.nextLine());
            }

            // Check new friendships
            for (String friendship: friendshipsFormed) {
                String[] friends = friendship.split("\\s");
                friend1 = friends[0];
                friend2 = friends[1];
                boolean f1InCircle = friendCircles.containsKey(friend1);
                boolean f2InCircle = friendCircles.containsKey(friend2);

                // Update HashMap
                if (!f1InCircle && !f2InCircle) {
                    // Two new people
                    ArrayList<String> newCircle = new ArrayList<>(List.of(friend1, friend2));
                    friendCircles.put(friend1, newCircle);
                    friendCircles.put(friend2, newCircle);
                } else if (f1InCircle && f2InCircle) {
                    // Two existing people
                    ArrayList<String> circle1 = friendCircles.get(friend1);
                    ArrayList<String> circle2 = friendCircles.get(friend2);
                    assert circle1 != null && circle2 != null: "Error: both friends should have a circle";
                    // Check if it is the same circle
                    if (circle1 != circle2) {
                        // Merge the two ArrayLists
                        circle1.addAll(circle2);
                        friendCircles.put(friend2, circle1);
                    }
                } else if (f1InCircle) {
                    // One new person
                    friendCircles.get(friend1).add(friend2);
                    friendCircles.put(friend2, friendCircles.get(friend1));
                } else {
                    // One new person
                    friendCircles.get(friend2).add(friend1);
                    friendCircles.put(friend1, friendCircles.get(friend2));
                }
                ArrayList<String> circle = friendCircles.get(friend1);
                assert circle != null: "Error: circle is null but shouldn't be";
                System.out.println(circle.size());
            }
        }
    }
}
