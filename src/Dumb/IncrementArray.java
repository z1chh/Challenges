package Dumb;

import java.util.ArrayList;
import java.util.Arrays;

public class IncrementArray {
    public static void main(String[] args) {
        incrementArray(2);
        incrementArray(4);
    }

    private static void incrementArray(int n) {
        // TO-DO
        ArrayList<int[]> toReturn = new ArrayList<>();
        int[] arr = new int[n];
        int ct = n - 1;
        while (true) {
            if (arr[ct] == 0) {
                arr[ct] = 1;
            } else {
                int c = 1;
                while (ct - c >= 0)
                    if (arr[ct - c] == 0) {
                        arr[ct - c] = 1;
                        for (int i = ct - c + 1; i < n; i++) {
                            arr[i] = 0;
                        }
                        break;
                    } else {
                        c++;
                    }
                if (ct - c < 0)
                    break;
            }
            toReturn.add(arr.clone());
        }

        toReturn.forEach(a -> System.out.println(Arrays.toString(a)));
    }
}
