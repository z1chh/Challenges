package Kattis.COMP321.A2;

import java.util.*;

public class D {
    public static void main(String[] args) {
        guess();
    }

    private static void guess() {
        // Create scanner object
        Scanner scanner = new Scanner(System.in);

        // Variables
        int numOperations, operationType, amount;
        String[] operation;
        boolean isStack = true, isQueue = true, isPriorityQueue = true;

        // Data Structures
        Stack<Integer> stack = new Stack<>();
        LinkedList<Integer> queue = new LinkedList<>();
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());

        while (scanner.hasNext()) {
            numOperations = scanner.nextInt();
            scanner.nextLine(); // Get rid of carriage return

            for (int i = 0; i < numOperations; i++) {
                operation = scanner.nextLine().split("\\s");

                // Check operation type
                operationType = Integer.parseInt(operation[0]);
                amount = Integer.parseInt(operation[1]);
                if (operationType == 1) {
                    // Add
                    stack.add(amount);
                    queue.addLast(amount);
                    priorityQueue.add(amount);

                } else { // operationType == 2
                    // Remove

                    // Check for stack
                    if (stack.isEmpty())
                        isStack = false;
                    else  if (amount != stack.pop())
                            isStack = false;

                    // Check for queue
                    if (queue.isEmpty())
                        isQueue = false;
                    else  if (amount != queue.removeFirst())
                            isQueue = false;

                    // Check for priority queue
                    if (priorityQueue.isEmpty())
                        isPriorityQueue = false;
                    else  if (amount != priorityQueue.poll())
                            isPriorityQueue = false;
                }
            }

            // Check which one is valid
            if ((isStack && isQueue) || (isStack && isPriorityQueue) || (isQueue && isPriorityQueue))
                System.out.println("not sure");
            else  if (isStack)
                System.out.println("stack");
            else if (isQueue)
                System.out.println("queue");
            else if (isPriorityQueue)
                System.out.println("priority queue");
            else
                System.out.println("impossible");
        }

        // Close scanner
        scanner.close();
    }
}
