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
        LinkedList<Integer> stack, queue, priorityQueue;

        while (scanner.hasNext()) {
            numOperations = scanner.nextInt();
            scanner.nextLine(); // Get rid of carriage return

            // Reset data structures
            stack = new LinkedList<>();
            queue = new LinkedList<>();
            priorityQueue = new LinkedList<>();

            // Reset booleans
            isStack = true;
            isQueue = true;
            isPriorityQueue = true;

            for (int i = 0; i < numOperations; i++) {
                operation = scanner.nextLine().split("\\s");

                // Skip and do nothing with input if already impossible
                if (!isStack && !isQueue && !isPriorityQueue)
                    if (i + 1 < numOperations)
                        continue;
                    else {
                        System.out.println("impossible");
                        continue;
                    }

                // Check operation type
                operationType = Integer.parseInt(operation[0]);
                amount = Integer.parseInt(operation[1]);
                if (operationType == 1) {
                    // Add
                    if (isStack)
                        stack.addLast(amount);
                    if (isQueue)
                        queue.addLast(amount);
                    if (isPriorityQueue) {
                        priorityQueue.add(amount);
                    }

                } else { // operationType == 2
                    // Remove

                    // Check for stack
                    if (isStack)
                        if (stack.isEmpty() || amount != stack.removeLast())
                            isStack = false;

                    // Check for queue
                    if (isQueue)
                        if (queue.isEmpty() || amount != queue.removeFirst())
                            isQueue = false;

                    // Check for priority queue
                    if (isPriorityQueue)
                        if (priorityQueue.isEmpty() || amount != removeMax(priorityQueue))
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

    private static int removeMax(List<Integer> arr) {
        int max = arr.get(0), size = arr.size(), cur, curIndex = 0;
        if (size == 1)
            return arr.remove(0);
        for (int i = 1; i < size; i++) {
            cur = arr.get(i);
            if (cur > max) {
                max = cur;
                curIndex = i;
            }
        }
        return arr.remove(curIndex);
    }
}
