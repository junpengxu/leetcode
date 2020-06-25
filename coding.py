# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head

        cur = head
        count = 1   # 链表长度

        # 1. 成环
        while cur.next:
            cur = cur.next
            count += 1
        cur.next = head

        # 2. 找到新的头前一个（这个就是新的尾巴）

        k = k % count # 断开的位置
        new_head = head

        for i in range(count - k - 1):
            new_head = new_head.next
        head = new_head.next
        new_head.next = None
        return head
