class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = 0
        head = self.head.next
        while head != self.tail and curr < index:
            head = head.next
            curr += 1
        
        if head != self.tail and curr == index:
            return head.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head.next
        new_head.prev = self.head
        self.head.next.prev = new_head
        self.head.next = new_head
        

    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val)
        new_tail.prev = self.tail.prev
        new_tail.next = self.tail
        self.tail.prev.next = new_tail
        self.tail.prev = new_tail
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index == 0:
            new_node = ListNode(val)

            new_node.next = curr
            new_node.prev = curr.prev

            curr.prev.next = new_node
            curr.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index == 0 and curr != self.tail:
            curr.next.prev = curr.prev
            curr.prev.next = curr.next
            del curr



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)