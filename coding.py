# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        gte_link = ListNode(-1)
        gte = gte_link
        lt_link = ListNode(-1)
        lt = lt_link
        while head:
            new_node = ListNode(head.val)
            if head.val < x:
                lt_link.next = new_node
                lt_link = lt_link.next
            else:
                gte_link.next = new_node
                gte_link = gte_link.next
            head = head.next
        curr = lt
        while curr and curr.next:
            curr = curr.next
        curr.next = gte.next
        return lt


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(5)
    f = ListNode(2)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    A = Solution()
    A.partition(a,3)
