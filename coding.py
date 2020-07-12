# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        mid = self.findmid(head)
        node = TreeNode(mid.val)

        if mid == head:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

    def findmid(self, head):
        tail = None
        slowptr = head
        fastptr = head
        while fastptr and fastptr.next:
            tail = slowptr
            slowptr = slowptr.next
            fastptr = fastptr.next.next
        if tail:
            tail.next = None
        return slowptr

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
    A= Solution()
    A.sortedListToBST(a)