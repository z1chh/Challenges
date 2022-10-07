package Kattis.COMP321.A1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class J {
    public static void main(String[] args) {
        busNumbers();
    }

    private static void busNumbers() {
        Scanner scanner = new Scanner(System.in);
        int nbBus, busNumber;
        ArrayList<Integer> busNumbers = new ArrayList<>();
        if (scanner.hasNextInt()) {
            nbBus = scanner.nextInt();
            assert nbBus > 0 && nbBus <= 1000: "Error: input must be between 1 and 1000 (included)";
            for (int i = 0; i < nbBus; i++) {
                if (scanner.hasNextInt()) {
                    busNumber = scanner.nextInt();
                    busNumbers.add(busNumber);
                } else {
                    throw new IllegalArgumentException("Error: input must be an int");
                }
            }
            Collections.sort(busNumbers);

            // Set element to -1 if it follows the previous one
            for (int i = busNumbers.size() - 1; i > 0; i--) {
                if (busNumbers.get(i) == busNumbers.get(i - 1) + 1) {
                    busNumbers.set(i, -1);
                }
            }

            // Combine negative values
            ArrayList<Integer> toPrint = new ArrayList<>();
            int cur, last;
            for (int i = 0; i < busNumbers.size() - 1; i++) {
                cur = busNumbers.get(i);
                if (cur == -1) {
                    last = toPrint.get(toPrint.size() - 1);
                    if (last < 0)
                        toPrint.set(toPrint.size() - 1, last - 1);
                    else
                        toPrint.add(-1);
                } else
                    toPrint.add(cur);
            }

            // Last element
            cur = busNumbers.get(busNumbers.size() - 1);
            if (cur == -1) {
                last = toPrint.get(toPrint.size() - 1);
                if (last < 0)
                    toPrint.set(toPrint.size() - 1, last - 1);
                else
                    toPrint.add(-1);
            }
            else
                toPrint.add(cur);

            // Print accordingly
            int next;
            for (int i = 0; i < toPrint.size() - 1; i++) {
                cur = toPrint.get(i);
                next = toPrint.get(i + 1);
                if (next >= 0) {
                    System.out.printf("%d ", cur);
                } else {
                    if (next == -1)
                        System.out.printf("%d %d ", cur, cur + 1);
                    else
                        System.out.printf("%d-%d ", cur, cur - next);
                    i++;
                }
            }

            // Print last if not a chain
            last = toPrint.get(toPrint.size() - 1);
            if (last >= 0)
                System.out.printf("%d", last);

            System.out.println();
        } else {
            throw new IllegalArgumentException("Error: input must be an int");
        }
    }
}
