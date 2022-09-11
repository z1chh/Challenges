package Dumb;

import java.util.ArrayList;
import java.util.Scanner;

public class Dumb {
    public static void main(String[] args) {
        dumb1();
    }

    private static void dumb1() {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        int testCases = 0;
        ArrayList<ArrayList<String>> allData = new ArrayList<>();
        while (!input.equals("")) {
            testCases++;
            ArrayList<String> info = new ArrayList<>();
            for (int i = 0; i < Integer.parseInt(input.split("\\s")[0]); i++) {
                info.add("scanner.nextLine() = " + scanner.nextLine());
            }
            allData.add(info);
            input = scanner.nextLine();
        }
        allData.forEach(l -> l.forEach(System.out::println));
        System.out.println("testCases = " + testCases);
    }
}
