class Solution:
    def swapPairs(self, head):
        d = ListNode(0)
        d.next = head
        p = d
        while head and head.next:
            f = head
            s = head.next
            p.next = s
            f.next = s.next
            s.next = f
            p = f
            head = f.next
        return d.next