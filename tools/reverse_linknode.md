[//]: # (@Author  : xu.junpeng)
[//]: # (@Time    : 2020/7/12 11:05 上午)
## [题目链接]()

## 思路
反转链表
## 分析过程

## 存在的问题

## 代码
递归反转单链表
```python
class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None


class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def isEmpty(self):
        return self.head == None

    def traverse(self):
        current = self.head
        while current:
            if current.next:
                print(current.data, end="->")
            else:
                print(current.data)
            current = current.next

    def reverse(self, item):
        if item.next == None:
            self.head = item
            return
        self.reverse(item.next)
        item.next.next = item
        item.next = None


if __name__ == '__main__':
    a = Node(1)
    b = Node(4)
    c = Node(3)
    d = Node(2)
    e = Node(5)
    f = Node(2)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    A = LinkedList(a)
    A.reverse(a)
    A.traverse()

```

## 结果
```

```
## 总结

