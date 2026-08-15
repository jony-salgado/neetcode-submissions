# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [5, 4, 2, 1]
#.          f  
#.    s
class Solution:
    def revertList(self, head):
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

        
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return 0
        
        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next

        list1 = head
        list2 = self.revertList(s.next)

        ans = 0
        while list1 and list2:
            ans = max(ans, list1.val + list2.val)
            list1 = list1.next
            list2 = list2.next

        return ans
        