package Dumb;

public class ArraysTest {
    public static void main(String[] args) {
        test();
    }

    private static void test() {
        int x = 10, y = 3;
        char[][] arr = new char[y][x];
        for (int i = 0; i < y; i++) {
            for (int j = 0; j < x; j++) {
                arr[i][j] = '#';
            }
        }
        arr[0][2] = '-';
        arr[2][2] = '-';
        arr[1][1] = '-';
        arr[1][2] = '-';
        arr[1][3] = '-';
        arr[1][4] = '-';
        System.out.println("Initial Sky:");
        printArr(arr, x, y);

        System.out.println();
        System.out.println("Modified Sky:");
        eraseStar(arr, 1, 2, y, x);
        printArr(arr, x, y);
    }

    private static void printArr(char[][] arr, int x, int y) {
        for (int i = 0; i < y; i++) {
            for (int j = 0; j < x; j++) {
                System.out.print(arr[i][j]);
            }
            System.out.println();
        }
    }

    private static void eraseStar(char[][] sky, int x, int y, int lines, int lineLength) {
        // Erase current star piece
        sky[x][y] = '#';

        // Check left piece
        if (y > 0)
            if (sky[x][y - 1] == '-')
                eraseStar(sky, x, y - 1, lines, lineLength);

        // Check right piece
        if (y + 1 < lineLength)
            if (sky[x][y + 1] == '-')
                eraseStar(sky, x, y + 1, lines, lineLength);

        // Check top piece
        if (x > 0)
            if (sky[x - 1][y] == '-')
                eraseStar(sky, x - 1, y, lines, lineLength);

        // Check bottom piece
        if (x + 1 < lines)
            if (sky[x + 1][y] == '-')
                eraseStar(sky, x + 1, y, lines, lineLength);
    }
}
