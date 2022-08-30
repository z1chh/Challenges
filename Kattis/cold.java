import java.util.ArrayList;
import java.util.Scanner;

public class cold {
    public static void main(String[] args) {
        System.out.println(negTemps());
    }

    public static int negTemps() {
        Scanner scanner = new Scanner(System.in);
        if (scanner.hasNextInt()) {
            int nb = scanner.nextInt();
            scanner.nextLine(); // Consume the newline
            if (scanner.hasNext()) {
                String[] inputs = scanner.nextLine().split(" ");
                ArrayList<Integer> temps = new ArrayList<>();
                for (String temp : inputs) {
                    try {
                        temps.add(Integer.parseInt(temp));
                    } catch (NumberFormatException nfe) {
                        throw new NumberFormatException("Error: must input numbers only");
                    }
                }
                assert temps.size() == nb: String.format("Error: must input %d %s", nb, nb > 1? "temperatures": "temperature");
                int neg = 0;
                for (int temp: temps) {
                    if (temp < 0)
                        neg++;
                }
                return neg;
            } else {
                throw new IllegalArgumentException("Error: input must be numbers separated by space");
            }
        } else {
            throw new IllegalArgumentException("Error: input must be a number");
        }
    }
}
