package Kattis.COMP321.A2;

import java.util.ArrayList;
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
        for (int i = 0; i < testCases; i++) {
            // Get new friendships
            numFriendshipsFormed = scanner.nextInt();
            for (int j = 0; j < numFriendshipsFormed; j++) {
                friendshipsFormed.add(scanner.nextLine());
            }

            // Check new friendships
            for (String friendship: friendshipsFormed) {
                String[] friends = friendship.split("\\s");
                // Check if tuple already existed, and ignore if yes
                // Check if friends already exist in other groups, if not create new group, otherwise add to other group
                // Output group size
            }
        }
    }
}
