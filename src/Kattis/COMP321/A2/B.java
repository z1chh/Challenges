package Kattis.COMP321.A2;

import java.util.LinkedList;
import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        System.out.println(backspace());
    }

    private static String backspace() {
        // Get input
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        StringBuilder output = new StringBuilder();

        // Format input
        LinkedList<Character> outputList = new LinkedList<>();
        int size = 0; // To avoid computing outputList.size() many times
        char cur;
        for (int i = 0; i < input.length(); i++) {
            cur = input.charAt(i);
            if (cur == '<' && size > 0) {
                outputList.removeLast();
                size--;
            } else if (cur != '<') {
                outputList.addLast(cur);
                size++;
            }
        }

        // Create output
        for (char c: outputList) {
            output.append(c);
        }

        return output.toString();
    }
}
