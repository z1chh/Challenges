package Kattis.COMP321.A1;

import java.util.ArrayList;
import java.util.Scanner;

public class D {
    public static void main(String[] args) {
        cold();
    }

    private static void cold() {
        Scanner scanner = new Scanner(System.in);
        int cases, negs = 0;
        ArrayList<Integer> temps = new ArrayList<>();
        if (scanner.hasNextInt()) {
            cases = scanner.nextInt();
            assert cases > 0 && cases <= 100: "Error: must have between 1 and 100 cases (included)";
            for (int i = 0; i < cases; i++) {
                if (scanner.hasNextInt()) {
                    temps.add(scanner.nextInt());
                } else {
                    throw new IllegalArgumentException("Error: input must be an int");
                }
            }
            for(Integer temp: temps)
                if (temp < 0)
                    negs++;
            System.out.println(negs);
        } else {
            throw new IllegalArgumentException("Error: input must be an int");
        }
    }
}
