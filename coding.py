class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        L = ListNode(-1)
        L.next = head
        i = 0
        j = L
        k = L
        while j.next:
            i += 1
            j = j.next
            if i - n > 0:
                k = k.next
        k.next = k.next.next
        return L.next


head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
if __name__ == '__main__':
    res = Solution().removeNthFromEnd(head, 5)
    print(head.val)
    while head.next:
        head = head.next
        print(head.val)
