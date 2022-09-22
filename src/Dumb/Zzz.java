package Dumb;

public class Zzz {
    public static void main(String[] args) {
        try {
            System.out.println("START");
            Thread.sleep(4000);
            System.out.println("WRONG");
        } catch (InterruptedException e) {
            System.out.println("Error: InterruptedException");
        }
    }
}
