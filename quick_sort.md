[//]: # (@Author  : xu.junpeng)
[//]: # (@Time    : 2020/6/26 2:33 下午)
## [题目链接]()

## 思路
记录两个快排
## 分析过程

## 存在的问题

## 代码
```python
def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)
 
def partition(array, l, r):
    x = array[r]
    i = l - 1   # 此时需要交换的位置
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            # j 索引后面的位置元素都是大于x的，可以用于交换， i索引后面的元素都是小于x的
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i+1]
    return i + 1
```

```python
def quick_sort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high]) # 此时的带排序列表被分成了两段
```

## 结果
```

```
## 总结

