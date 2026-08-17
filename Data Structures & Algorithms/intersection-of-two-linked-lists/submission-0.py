
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB
        while pa != None and pb != None:
            pa = pa.next
            pb = pb.next

        if pb != None and pa == None:
            pa, pb = pb, pa
            headA, headB = headB, headA

        count = 0
        while pa:
            pa = pa.next
            count += 1

        pa = headA
        pb = headB
        for _ in range(count):
            pa = pa.next

        while pa != None and pb != None:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next

        return None