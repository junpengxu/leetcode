# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node_record = []
        index = 0
        new_head = head

        while new_head not in node_record and new_head.next:
            node_record.append(new_head)
            new_head = new_head.next
            index += 1
        if not new_head.next:
            return None
        return new_head


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
    e.next = a
    A = Solution()
    print(A.detectCycle(a))
