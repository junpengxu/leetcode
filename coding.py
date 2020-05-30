# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        elif len(lists) > 2:
            a = self.mergeKLists(lists[0:len(lists) // 2])
            b = self.mergeKLists(lists[len(lists) // 2:])
            return self.merge_two_list(a, b)
        elif len(lists) == 2:
            return self.merge_two_list(lists[0], lists[1])
        else:
            return self.merge_two_list(lists[0], None)

    def merge_two_list(self, list_a, list_b):
        if not list_a:
            return list_b
        if not list_b:
            return list_a

        new_list = ListNode()
        tmp = new_list

        while list_a and list_b:
            if list_a.val <= list_b.val:
                tmp.next = ListNode(list_a.val)
                list_a = list_a.next
            else:
                tmp.next = ListNode(list_b.val)
                list_b = list_b.next
            tmp = tmp.next
        if list_a:
            tmp.next = list_a
        if list_b:
            tmp.next = list_b
        return new_list.next


if __name__ == '__main__':
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    list_a = ListNode(0)
    list_a.next = node_1
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    A = Solution()
    res = A.mergeKLists([[]])
    a = res
