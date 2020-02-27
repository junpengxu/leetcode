[//]: # (@Author  : xu.junpeng)
[//]: # (@Time    : 2020-02-26 12:34)

## [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

## 思路
- 这是一道最长回文字符串的题，大学的时候曾经用过暴力求解体的方法处理。但是现在是0202年了。暴力法的话应该是n的三次方时间复杂度。所以我考虑直接从n的二次方时间复杂度去解决问题

## 分析过程
1. 找最长，开辟一个空间，用于保存已知最长的结果
2. 写一个方法，用于判断当前字符串是否是回文字符串，以及长度
3. 是否可以考虑上递归呢，先从第一个字符开始判断，然后逐步向两边扩张，这样会不会又回到了n的三次方呢。先写写看吧

## 存在的问题
- 没想到别的办法，只是想到了暴力法
## 代码
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        end = 0
        max_len_string = ''
        while True:

            if end == len(s):
                break

            end += 1
            start = 0

            while True:
                if Solution.isPalindrome(s[start:end]):
                    max_len_string = max_len_string if end - start < len(max_len_string) else s[start:end]
                start += 1
                if start == end:
                    break

        return max_len_string

    @staticmethod
    def isPalindrome(s):
        if s == s[::-1]:
            return True
        return False


assert Solution().longestPalindrome('s') == 's'
assert Solution().longestPalindrome('sss') == 'sss'
assert Solution().longestPalindrome('saas') == 'saas'

```

## 结果
```
Runtime: 8680 ms, faster than 5.00% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
```

## 总结
- 分析下哪里可以进行优化
1. 从重复的计算开始看，确定下哪里有重复的部分。
- 通过两次遍历，把字符串所有的可能情况都重新的判断了一遍，在这个过程中，存在可以不进行判断的地方么？
- 没想到。我觉得如果使用到递归后，可能会节省一些时间，不过会占用更多的内存。
- 我的做法相当于是使用了滑动窗口，窗口既为最长的长度。
- 那么反过来想，如果我是先找个最大的窗口，然后缩小呢。第一个找到的一定是最大的长度了。类似于分治，那么怎么分呢？
- 


## 其他解法

### Manacher's Algorithm(马拉车算法)
https://cloud.tencent.com/developer/article/1536016
https://blog.csdn.net/Charles_Zaqdt/article/details/79747073
其实还是没看太懂，整体上给我的感觉是跟kmp是类似的通过辅助数组来避免重复的计算。

```python
def manacher(self):
    s = '#' + '#'.join(self) + '#'  # 字符串处理，用特殊字符隔离字符串，方便处理偶数子串
    lens = len(s)
    p = [0] * lens  # p[i]表示i作中心的最长回文子串的半径，初始化p[i]
    mx = 0  # 之前最长回文子串的右边界
    id = 0  # 之前最长回文子串的中心位置
    for i in range(lens):  # 遍历字符串
        if mx > i:
            p[i] = min(mx - i, p[int(2 * id - i)])  # 由理论分析得到
        else:  # mx <= i
            p[i] = 1
        while i - p[i] >= 0 and i + p[i] < lens and s[i - p[i]] == s[i + p[i]]:  # 满足回文条件的情况下
            p[i] += 1  # 两边扩展
        if (i + p[i]) > mx:  # 新子串右边界超过了之前最长子串右边界
            mx, id = i + p[i], i  # 移动之前最长回文子串的中心位置和边界，继续向右匹配
    i_res = p.index(max(p))  # 获取最终最长子串中心位置
    s_res = s[i_res - (p[i_res] - 1):i_res + p[i_res]]  # 获取最终最长子串，带"#"

```