package Kattis.COMP321.A2;

import java.util.ArrayList;
import java.util.Scanner;

public class G {
    public static void main(String[] args) {
        deDuplicate();
    }

    private static void deDuplicate() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        int numFiles, hashCollisions, size;
        ArrayList<String> files, output = new ArrayList<>();
        ArrayList<Integer> duplicateFiles;
        String f, tC;
        String[] file, toCompare;

        while ((numFiles = scanner.nextInt()) != 0) {
            // First get rid of carriage return
            scanner.nextLine();

            // Reset variables
            duplicateFiles = new ArrayList<>();
            files = new ArrayList<>();
            hashCollisions = 0;

            // Read files
            for (int i = 0; i < numFiles; i++) {
                files.add(scanner.nextLine());
            }
            size = files.size();

            // Compare files
            for (int i = 0; i < size; i++) {
                for (int j = i; j < size; j++) {
                    // Do not compare with itself
                    if (i == j)
                        continue;
                    f = files.get(i);
                    tC = files.get(j);

                    // Check if they're identical
                    if (f.equals(tC)) {
                        if (!duplicateFiles.contains(i))
                            duplicateFiles.add(i);
                        if (!duplicateFiles.contains(j))
                            duplicateFiles.add(j);
                    } else {
                        int f1Length, f2Length;
                        String w1, w2;

                        file = f.split("\\s");
                        toCompare = tC.split("\\s");
                        f1Length = file.length;
                        f2Length = toCompare.length;

                        // Check if they're same size
                        if (f1Length != f2Length)
                            continue;

                        for (int k = 0; k < f1Length; k++) {
                            w1 = file[k];
                            for (int l = 0; l < f2Length; l++) {
                               w2 = toCompare[l];
                               if (w1.equals(w2)) {
                                   toCompare[l] = "-1";
                                   break;
                               }
                            }
                            boolean same = true;
                            for (int l = 0; l < f2Length; l++) {
                                if (!toCompare[l].equals("-1")) {
                                    same = false;
                                    break;
                                }
                            }
                            if (same) {
                                if (!duplicateFiles.contains(i))
                                    duplicateFiles.add(i);
                                if (!duplicateFiles.contains(j))
                                    duplicateFiles.add(j);
                                hashCollisions++;
                            }
                        }
                    }
                }
            }

            // Store results
            output.add(String.format("%d %d%n", duplicateFiles.size(), hashCollisions));
        }

        // Output results
        output.forEach(System.out::println);
    }
}
