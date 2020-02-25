## [两数相加](https://leetcode.com/problems/add-two-numbers/)

## 思路
- 先看下给的数据结构
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
```
## 看下example
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```
## 分析相加的过程
List结构实际上是个链表，低位在前。但是在相加的过程中要注意好进位的处理。应该同时遍历节点。开辟新内存，或者是复用其中的一个ListNode.考虑时间复杂度，空间复杂度上的优化。

## 存在的问题。
- 一开始设计了一个感觉对的思路。导致在一些特殊case上，失败
- 写代码之前要先考虑好边界条件
- 增加链表节点的时候要记得添加到链表上去，而不是单纯的创建一个节点
- while True 的情况下注意好跳循环的时机
- 多输出一些中间结果的信息，帮助自己了解程序运行中间的结果

## 代码
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        index = 0  # 用于记录进位
        node_1 = l1
        node_2 = l2
        while True:

            sum = int((node_1.val+node_2.val+index) % 10)
            index = int((node_1.val+node_2.val+index)//10)
            node_1.val = sum

            if node_1.next is None and node_2.next is None and index == 0:
                break
            if node_1.next:
                node_1 = node_1.next
            else:
                node_1.next = ListNode(0)
                node_1 = node_1.next

            if node_2.next:
                node_2 = node_2.next
            else:
                node_2.next = ListNode(0)
                node_2 = node_2.next

        return l1
```
## 结果
```
Runtime: 68 ms, faster than 74.53% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
```

## 总结
- 这道题不难，基本一看题就会有思路，主要是没考虑好情况就开始动手写了。实际上花了很长时间， 大约是一小时， 我本来觉得十几分钟就可以ac的。