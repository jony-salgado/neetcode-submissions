# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        aux = node

        while list1 and list2:
            if list1.val < list2.val:
                aux.next = list1
                list1 = list1.next
            else:
                aux.next = list2
                list2 = list2.next
            aux = aux.next

        if list1:
            aux.next = list1
        if list2:
            aux.next = list2

        return node.next