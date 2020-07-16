# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        tmp = head
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        if tmp.val == val:
            return tmp.next
        return tmp


if __name__ == '__main__':
    a = ListNode(2)
    b = ListNode(1)
    c = ListNode(1)
    d = ListNode(1)
    e = ListNode(1)
    f = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    A = Solution()
    cc = A.removeElements(a, 1)
    bbb = 1
