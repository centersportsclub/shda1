class Solution:
    def reverseList(self,head):
        p = None
        c = head
        while c:
            nxt = c.next
            c.next = p
            p = c
            c = nxt
        return p