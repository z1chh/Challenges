package Dumb;

import java.util.ArrayList;
import java.util.Arrays;

public class IncrementArray {
    public static void main(String[] args) {
        incrementArray(4);
    }

    private static void incrementArray(int n) {
        // TO-DO
        ArrayList<int[]> toReturn = new ArrayList<>();
        boolean[] arr = new boolean[n];
        for (int i = 0; i < n; i++) {

        }

        toReturn.forEach(a -> System.out.println(Arrays.toString(a)));
    }

    private static boolean done(boolean[] arr) {
        for (boolean b: arr) {
            if (!b)
                return false;
        }
        return true;
    }

    private static void test() {
        ArrayList<int[]> toReturn = new ArrayList<>();
        int[] arr = new int[]{1, 2, 3};
        toReturn.add(arr.clone());
        arr[0] += 2;
        toReturn.add(arr);
        toReturn.forEach(n -> System.out.println(Arrays.toString(n)));
    }
}
