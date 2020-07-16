# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def recurse(head):
            if not head.next:
                return head
            tmp = recurse(head.next)
            head.next.next = head
            head.next = None
            return tmp
        head = recurse(head)
        return head

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    A = Solution()
    cc = A.reorderList(a)
    bbb = 1
