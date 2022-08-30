import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class ofugsnuid {
    public static void main(String[] args) {
        reverse();
    }

    public static void reverse() {
        Scanner scanner = new Scanner(System.in);
        if (scanner.hasNextInt()) {
            int nb = scanner.nextInt();
            scanner.nextLine(); // Consume the newline
            ArrayList<Integer> ints = new ArrayList<>();
            for (int i = 0; i < nb; i++) {
                if (scanner.hasNextInt()) {
                    ints.add(scanner.nextInt());
                } else {
                    throw new IllegalArgumentException("Error: input must be a number");
                }
            }
            Collections.reverse(ints);
            ints.forEach(System.out::println);
        } else {
            throw new IllegalArgumentException("Error: input must be a number");
        }
    }
}
