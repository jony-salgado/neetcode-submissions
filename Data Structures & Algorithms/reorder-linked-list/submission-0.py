# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def revertList(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        new_head = self.revertList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        second = slow.next
        slow.next = None
        second = self.revertList(second)

        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        