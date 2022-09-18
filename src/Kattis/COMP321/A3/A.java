package Kattis.COMP321.A3;

import java.util.ArrayList;
import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        pebble();
    }

    private static void pebble() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        int testCases, smallest;
        String input;
        char[] game;
        ArrayList<Integer> scores;
        int[] bestScores;

        // Get number of test cases
        testCases = scanner.nextInt();
        scanner.nextLine(); // Get rid of carriage return
        bestScores = new int[testCases];

        // Get games and their score
        for (int i = 0; i < testCases; i++) {
            // Get input
            input = scanner.nextLine().toLowerCase();

            // Convert into char array
            game = new char[12];
            for (int j = 0; j < 12; j++) {
                game[j] = input.charAt(j);
            }

            // Update score array
            scores = new ArrayList<>();
            getScore(game, scores);

            // Get smallest score
            smallest = scores.get(0);
            for (int score: scores) {
                if (score < smallest)
                    smallest = score;
            }

            // Display result
            bestScores[i] = smallest;
        }

        // Output scores
        for (int score: bestScores) {
            System.out.println(score);
        }
    }

    private static void getScore(char[] game, ArrayList<Integer> scores) {
        // Variables
        char[] cur;
        ArrayList<char[]> moves = new ArrayList<>();
        int pebbles = 0;

        // Check for valid moves
        for (int i = 0; i < 12 - 2; i++) {
            if (game[i] == 'o' && game[i + 1] == 'o' && game[i + 2] == '-') {
                cur = game.clone();
                cur[i] = '-';
                cur[i + 1] = '-';
                cur[i + 2] = 'o';
                moves.add(cur);
            } else if (game[i] == '-' && game[i + 1] == 'o' && game[i + 2] == 'o') {
                cur = game.clone();
                cur[i] = 'o';
                cur[i + 1] = '-';
                cur[i + 2] = '-';
                moves.add(cur);
            }
        }

        // Add current score
        for (int i = 0; i < 12; i++) {
            if (game[i] == 'o')
                pebbles++;
        }
        scores.add(pebbles);

        // Add score of playable moves
        for (char[] move: moves) {
            getScore(move, scores);
        }
    }
}
