# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, lst1, lst2):
        d = ListNode(0)
        c = d
        while lst1 and lst2:
            if lst1.val <= lst2.val:
                c.next = lst1
                lst1 = lst1.next
            else:
                c.next = lst2
                lst2 = lst2.next
            c = c.next
        if lst1:
            c.next = lst1
        else:
            c.next = lst2
        return d.next


