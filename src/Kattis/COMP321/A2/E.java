package Kattis.COMP321.A2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class E {
    public static void main(String[] args) {
        virtualFriends();
    }

    private static void virtualFriends() {
        // Get number of test cases
        Scanner scanner = new Scanner(System.in);
        int testCases = scanner.nextInt();

        // Test case
        int numFriendshipsFormed;
        ArrayList<String> friendshipsFormed = new ArrayList<>();
        HashMap<String, ArrayList<String>> connections = new HashMap<>();
        String friend1, friend2;
        for (int i = 0; i < testCases; i++) {
            // Get new friendships
            numFriendshipsFormed = scanner.nextInt();
            for (int j = 0; j < numFriendshipsFormed; j++) {
                friendshipsFormed.add(scanner.nextLine());
            }

            // Check new friendships
            for (String friendship: friendshipsFormed) {
                String[] friends = friendship.split("\\s");
                friend1 = friends[0];
                friend2 = friends[1];
                // Check if tuple already existed, and ignore if yes
                // Check if friends already exist in other groups, if not create new group, otherwise add to other group
                // Output group size
                if (connections.containsKey(friend1)) {
                    if (!connections.get(friend1).contains(friend2))
                        connections.get(friend1).add(friend2);
                } else {
                    connections.put(friend1, new ArrayList<>());
                    connections.get(friend1).add(friend2);
                }
                if (connections.containsKey(friend2)) {
                    if (!connections.get(friend2).contains(friend1))
                        connections.get(friend2).add(friend1);
                } else {
                    connections.put(friend2, new ArrayList<>());
                    connections.get(friend2).add(friend1);
                }
            }
        }
    }
}
