package Leetcode;

public class AddTwoNumbers {
    public static void main(String[] args) {
        ex1();
        ex2();
        ex3();
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        assert l1 != null && l2 != null: "Error: input ListNode cannot be null";

        // Compute sum first
        int ct = 0;
        long n1 = 0, n2 = 0, sum;
        while (hasNext(l1)) {
            n1 += l1.val * Math.pow(10, ct++);
            l1 = l1.next;
        }
        n1 += l1.val * Math.pow(10, ct);
        ct = 0;
        while (hasNext(l2)) {
            n2 += l2.val * Math.pow(10, ct++);
            l2 = l2.next;
        }
        n2 += l2.val * Math.pow(10, ct);
        sum = n1 + n2;

        // Create new ListNode
        ListNode toReturn = new ListNode();
        ListNode cur = toReturn;
        while (true) {
            if (sum >= 10) {
                cur.next = new ListNode();
                cur.val = (int) sum % 10;
                sum = sum / 10;
                cur = cur.next;
            } else {
                cur.val = (int) sum;
                break;
            }
        }
        return toReturn;
    }

    private static boolean hasNext(ListNode l) {
        return l.next != null;
    }

    private static void ex1() {
        ListNode l1 = new ListNode(3);
        ListNode l2 = new ListNode(4, l1);
        ListNode l3 = new ListNode(2, l2);
        ListNode l4 = new ListNode(4);
        ListNode l5 = new ListNode(6, l4);
        ListNode l6 = new ListNode(5, l5);
        ListNode l = addTwoNumbers(l3, l6);
        System.out.println(l);
    }

    private static void ex2() {
        ListNode l1 = new ListNode(9);
        ListNode l2 = new ListNode(4, l1);
        ListNode l3 = new ListNode(2, l2);
        ListNode l4 = new ListNode(9);
        ListNode l5 = new ListNode(4, l4);
        ListNode l6 = new ListNode(6, l5);
        ListNode l7 = new ListNode(5, l6);
        ListNode l = addTwoNumbers(l3, l7);
        System.out.println(l);
    }

    private static void ex3() {
        ListNode l1 = new ListNode(9);
        ListNode l2 = new ListNode(9);
        ListNode l3 = new ListNode(9, l2);
        ListNode l4 = new ListNode(9, l3);
        ListNode l5 = new ListNode(9, l4);
        ListNode l6 = new ListNode(9, l5);
        ListNode l7 = new ListNode(9, l6);
        ListNode l8 = new ListNode(9, l7);
        ListNode l9 = new ListNode(9, l8);
        ListNode l10 = new ListNode(9, l9);
        ListNode l11 = new ListNode(1, l10);
        ListNode l = addTwoNumbers(l1, l11);
        System.out.println(l);
    }
}
