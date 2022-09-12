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
        boolean isStack, isQueue, isPriorityQueue;

        // Data Structures
        LinkedList<Integer> stack, queue;
        ArrayList<Integer> priorityQueue;

        while (scanner.hasNext()) {
            numOperations = scanner.nextInt();
            scanner.nextLine(); // Get rid of carriage return

            // Reset data structures
            stack = new LinkedList<>();
            queue = new LinkedList<>();
            priorityQueue = new ArrayList<>();

            // Reset booleans
            isStack = true;
            isQueue = true;
            isPriorityQueue = true;

            for (int i = 0; i < numOperations; i++) {
                operation = scanner.nextLine().split("\\s");

                // Check operation type
                operationType = Integer.parseInt(operation[0]);
                amount = Integer.parseInt(operation[1]);
                if (operationType == 1) {
                    // Add
                    stack.addLast(amount);
                    queue.addLast(amount);
                    priorityQueue.add(amount);
                    Collections.sort(priorityQueue);

                } else { // operationType == 2
                    // Remove

                    // Check for stack
                    if (stack.isEmpty() || amount != stack.removeLast())
                            isStack = false;

                    // Check for queue
                    if (queue.isEmpty() || amount != queue.removeFirst())
                            isQueue = false;

                    // Check for priority queue
                    if (priorityQueue.isEmpty() || amount != priorityQueue.remove(priorityQueue.size() - 1))
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
