[//]: # (@Author  : xu.junpeng)
[//]: # (@Time    : ${DATE} ${TIME})

## [题目链接](https://leetcode.com/problems/reverse-integer/)

## 思路
看题目是一个数字反转的。第一个想到的是位运算，补码=源码取反+1。又看了下题目，觉得不行。不能这么做。
给出的是一个有符号整数，那么就要先注意一下符号的问题了。所以可以考虑首先把符号拿出来。其次，判断结尾是否为0。如果是0的话，要去掉一位。
想到了不断的模10。

## 分析过程
1. 判断符号位
2. 判断有多少个0
## 存在的问题
第一次提交错了。 因为说是32位的有符号数字，也就是说，我要判断数字的绝对值小于2的31次方.
题目也给出提示了：Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2<<31,  2<<31 − 1]
## 代码
```python
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x > 0:
            flag = 1
        else:
            flag = 0
            x = -x

        # 去掉末尾的0
        while x:
            if x % 10:
                break
            x = x // 10

        while x:
            res = res * 10
            res += x % 10
            x = x // 10
        if res > 2**31:
            return 0
        return res if flag else -res
```

## 结果
```
Runtime: 28 ms, faster than 77.71% of Python3 online submissions for Reverse Integer.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Integer.
```
## 总结
- 某一次提交错误的代码
```python
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if not (-1<<32 <= x and x <= (1<<32) -1):
            return 0
        elif x > 0:
            flag = 1
        else:
            flag = 0
            x = -x

        # 去掉末尾的0
        while x:
            if x % 10:
                break
            x = x // 10

        while x:
            res = res * 10
            res += x % 10
            x = x // 10

        return res if flag else -res
```
出错了几次， 实际上就是没弄好32位有符号整数的边界.

```
In [75]: 1<<32-1
Out[75]: 2147483648

In [76]: 1<<31
Out[76]: 2147483648

满足要求的范围   -1<<32 <= x <= (1<<32) -1      = >      -1<<32 <= x and x <= (1<<32) -1 
那么我对这个式子烦着判断呢？
其实我对上面的结果目前我心里也是没底的。
很坑自己，相当于取leetcode线上debug了，无数个错误答案，最后我也不先判断是否符合了题目的限制了，先计算出结果来。
```


## 大佬的答案
- 时间最少
```python
class Solution:
    def reverse(self, x):
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        return s*r * (r < 2**31)
```
- 占用内存最少
```python
class Solution:
    def reverse(self, x: int) -> int:
        y = list(str(abs(x)))
        y.reverse()
        y = int(''.join(y))
        if x < 0:
            y *= -1
        if y < -2**31 or y > 2**31-1:
            y = 0
        return y
```
不失为一种方法，但是我觉得这么做就没什么意义了 


## 后记
```python
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if not (-2147483648 <= x and x <= 2147483648):
            return 0
        elif x > 0:
            flag = 1
        else:
            flag = 0
            x = -x

        # 去掉末尾的0
        while x:
            if x % 10:
                break
            x = x // 10

        while x:
            res = res * 10
            res += x % 10
            x = x // 10

        return res if flag else -res
```
上面的这个代码也是错的。
不死心的我最后提交了这个代码才发现错在了哪里。是因为 反转之后的数字超过了2的32次方
