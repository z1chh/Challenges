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
        scanner.nextLine(); // Get rid of carriage return

        // Test case
        int numFriendshipsFormed;
        ArrayList<String> friendshipsFormed = new ArrayList<>();
        HashMap<String, ArrayList<String>> connections = new HashMap<>();
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
                // Check if tuple already existed, and ignore if yes
                // Check if friends already exist in other groups, if not create new group, otherwise add to other group
                // Output group size
                updateFriends(friend1, friend2, connections);
                updateFriends(friend2, friend1, connections);
                System.out.println(connections.get(friend1).size());
            }
        }
    }

    private static void updateFriends(String name, String friend, HashMap<String, ArrayList<String>> connections) {
        ArrayList<String> friends;
        if (connections.containsKey(name)) {
            friends = connections.get(name);
            if (!friends.contains(friend)) {
                friends.add(friend);
                for (String f: friends) {
                    updateFriends(f, friend, connections);
                }
            }
        } else {
            friends = new ArrayList<>();
            friends.add(friend);
            friends.add(name);
            connections.put(name, friends);
        }
    }
}
