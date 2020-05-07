class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return head
        cur = head
        while cur.next:
            p = cur
            q = cur.next
            p.val, q.val = q.val, p.val
            cur = cur.next.next if cur.next.next else cur.next
        return head


if __name__ == '__main__':
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    head = a1
    head.next = a2
    a2.next = a3
    a3.next = a4
    A = Solution()
    aa = A.swapPairs(head)
    aa = A.swapPairs(head)