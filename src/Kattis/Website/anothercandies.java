package Kattis.Website;

import java.util.ArrayList;
import java.util.Scanner;

public class anothercandies {
    public static void main(String[] args) {
        candies();
    }

    public static void candies() {
        Scanner scanner = new Scanner(System.in);
        if (scanner.hasNextInt()) {
            int nb = scanner.nextInt();
            int candies;
            ArrayList<String> answers = new ArrayList<>();
            for (int i = 0; i < nb; i++) {
                scanner.nextLine(); // Consume the newline
                candies = 0;
                if (scanner.hasNextInt()) {
                    int children = scanner.nextInt();
                    for (int j = 0; j < children; j++) {
                        candies += scanner.nextInt() % children;
                    }
                    if (candies % children == 0)
                        answers.add("YES");
                    else
                        answers.add("NO");
                } else {
                    throw new IllegalArgumentException("Error: input must be a number");
                }
            }
            assert answers.size() == nb;
            answers.forEach(System.out::println);
        } else {
            throw new IllegalArgumentException("Error: input must be a number");
        }
    }
}
