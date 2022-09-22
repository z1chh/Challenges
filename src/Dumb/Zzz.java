package Dumb;

public class Zzz {
    public static void main(String[] args) {
        try {
            System.out.println("START");
            Thread.sleep(1000);
            System.out.println("1 SEC");
            Thread.sleep(1000);
            System.out.println("2 SEC");
        } catch (InterruptedException e) {
            System.out.println("Error: InterruptedException");
        }
    }
}
