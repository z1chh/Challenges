import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class pot {
    public static void main(String[] args) {
        System.out.println(pot());
    }

    public static int pot() {
        Scanner scanner = new Scanner(System.in);
        if (scanner.hasNextInt()) {
            int nb = scanner.nextInt();
            assert 1 <= nb && nb <= 10: "Error: input must be between 1 and 10 (inclusive)";
            scanner.nextLine(); // Consume the newline
            ArrayList<Integer> inputs = new ArrayList<>();
            for (int i = 0; i < nb; i++) {
                if (scanner.hasNext()) {
                    try {
                        inputs.add(Integer.parseInt(scanner.nextLine()));
                    } catch (NumberFormatException nfe) {
                        throw new NumberFormatException("Error: NaN");
                    }
                } else {
                    throw new IllegalArgumentException("Error: missing arguments");
                }
            }
            int answer = 0;
            for (int input: inputs) {
                int base = input / 10;
                int pow = input % 10;
                answer += Math.pow(base, pow);
            }
            return answer;
        } else {
            throw new IllegalArgumentException("Error: input must be a number");
        }
    }
}
