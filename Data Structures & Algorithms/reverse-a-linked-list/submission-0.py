# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def reverse_list(head):
            if not head.next:
                return head, head
            
            new_head, last_element = reverse_list(head.next)
            head.next = None
            last_element.next = head
            return new_head, head


        head, _ = reverse_list(head)

        return head