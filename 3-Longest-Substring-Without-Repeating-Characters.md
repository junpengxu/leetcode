## [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## 思路
- 题目要求说给出一个子串，找出最长的不重复字串。要求的输出是数字。
- 首先想到的是暴力穷举法。不到万不得已是不会这么做的。
- 想到的是使用滑动窗口，通过一个标志位记录历史最长的字串长度，然后开始从左到右滑动
- 可以确定的有， 终止条件，计算字串长度方法。可以先实现出来
- 判断输入的边界条件

## 代码
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        start = max_len = end = 0

        while True:

            #end 向右滑动，直到内部有重复的元素
            if s[end] not in s[start:end]:
                end += 1
            else:
                max_len = max_len if max_len > end - start else end - start
                #start滑动到重复元素位置+1
                start = s[start:end].index(s[end]) + start + 1
                end += 1

            # 结束条件, end 遍历到结尾, 一定会出现最长字串
            if end == len(s):
                # 如果一直是不重复的话，max_len 是不会被计算
                return max_len if max_len > end - start else end - start
```

## 存在的问题
1. 计算字符串长度。 处于不断的搞混的状态,s[0:1]长度为1, s[0:2]长度为2, s[2:4]长度为2
2. 预先判断需要计算的下一个字符串是否重复，导致计算长度出现混乱。
3. 首先要拆分好。 那些是明确对的。解开耦合。不要改一个地方导致其他位置也要跟着变动

## 结果
```
Runtime: 48 ms, faster than 92.76% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
```
## 不得不说的一点
`s[end] not in s[start:end]` 与 `s[end+1] not in s[start:end]` 还能分的清么。一开始的思路是对的。只是因为这一步没有想清楚。导致多花了1个小时。