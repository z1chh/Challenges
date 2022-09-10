package Kattis.COMP321.A2;

import java.util.ArrayList;
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
        int numFriendshipsFormed;
        ArrayList<String> friendshipsFormed = new ArrayList<>();
        ArrayList<ArrayList<String>> friendCircles = new ArrayList<>();
        String friend1, friend2;
        for (int i = 0; i < testCases; i++) {
            // Get new friendships
            numFriendshipsFormed = scanner.nextInt();
            scanner.nextLine(); // Get rid of carriage return
            for (int j = 0; j < numFriendshipsFormed; j++) {
                friendshipsFormed.add(scanner.nextLine());
            }

            // Check new friendships
            for (String friendship: friendshipsFormed) {
                String[] friends = friendship.split("\\s");
                friend1 = friends[0];
                friend2 = friends[1];
                boolean f1InCircle = inCircle(friend1, friendCircles);
                boolean f2InCircle = inCircle(friend2, friendCircles);
                if (!f1InCircle && !f2InCircle) {
                    ArrayList<String> newCircle = new ArrayList<>(List.of(friend1, friend2));
                    friendCircles.add(newCircle);
                } else if (f1InCircle && f2InCircle) {
                    // Merge the two ArrayLists
                    ArrayList<String> circle1 = getCircle(friend1, friendCircles);
                    ArrayList<String> circle2 = getCircle(friend2, friendCircles);
                    assert circle1 != null && circle2 != null: "Error: both friends should have a circle";
                    // Check if it is the same circle
                    if (circle1 != circle2) {
                        circle1.addAll(circle2);
                        friendCircles.remove(circle2);
                    }
                } else if (f1InCircle) {
                    updateCircles(friend1, friend2, friendCircles);
                } else {
                    updateCircles(friend2, friend1, friendCircles);
                }
                ArrayList<String> circle = getCircle(friend1, friendCircles);
                assert circle != null: "Error: circle is null but shouldn't be";
                System.out.println(circle.size());
            }
        }
    }

    private static boolean inCircle(String name, ArrayList<ArrayList<String>> friendCircles) {
        for (ArrayList<String> circle: friendCircles) {
            if (circle.contains(name)) {
                return true;
            }
        }
        return false;
    }

    private static void updateCircles(String name, String friend, ArrayList<ArrayList<String>> friendCircles) {
        for (ArrayList<String> circle: friendCircles) {
            if (circle.contains(name)) {
                circle.add(friend);
                return;
            }
        }
    }

    private static ArrayList<String> getCircle(String name, ArrayList<ArrayList<String>> friendCircles) {
        for (ArrayList<String> circle: friendCircles) {
            if (circle.contains(name))
                return circle;
        }
        assert false: String.format("%s has a circle but it couldn't be found", name);
        return null;
    }
}
