# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            self.successor = None
            return self.recurse(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    def recurse(self, head, n):
        if n == 1:
            return head
        last = self.recurse(head.next, n - 1)
        successor = head.next.next  # 后继节点，被反转之前的链表的头节点的下一个节点
        head.next.next = head
        head.next = successor       # successor 在被不断的更新，更新为新的头节点的后继节点, 实际上都是同一个
        return last


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
    A.reverseBetween(a, 2, 5)
    aa = 1
