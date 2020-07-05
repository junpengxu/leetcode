# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         curr = head
#
#         while curr and curr.next:
#
#             if curr.val == curr.next.val:
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next
#
#         return head

if __name__ == '__main__':
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(1)
    d = ListNode(2)
    e = ListNode(3)
    f = ListNode(3)
    f1 = ListNode(4)
    f2 = ListNode(5)
    f3 = ListNode(5)
    f4 = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = f1
    f1.next = f2
    f2.next = f3
    f3.next = f4
    A = Solution()
    A.deleteDuplicates(a)
    while a.next:
        print(a.val)
        a = a.next
    print(a.val)
