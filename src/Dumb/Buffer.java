package Dumb;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;

public class Buffer {
    public static void main(String[] args) throws IOException {
        test();
    }

    private static void test() throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String input;
        while (!Objects.equals(input = br.readLine(), "")) {
            sb.append(input).append(" ");
        }

        System.out.println(sb);
    }
}
