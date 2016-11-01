import java.lang.Override;
import java.util.PriorityQueue;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>(1, new Comparator<ListNode>() {
            public int compare(ListNode x, ListNode y) {
                return x.val-y.val;
            }
        });
        for (int i=0; i<lists.length; i++) {
            if (lists[i] != null) {
                pq.add(lists[i]);
            }
        }
        ListNode head = new ListNode(0);
        ListNode running = head;
        while (pq.size() > 1) {
            ListNode one = pq.poll();
            running.next = one;
            running = running.next;
            if (one.next != null) {
                pq.add(one.next);
            }
        }
        if (pq.size() == 1) {
            running.next = pq.poll();
        }
        return head.next;
    }
}