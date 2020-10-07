[//]: # (@Author  : xu.junpeng)
[//]: # (@Time    : ${DATE} ${TIME})

## [题目链接](https://leetcode.com/problems/string-to-integer-atoi/)

## 思路
1. 判断开始的字符是否为 "-"， " "， "数字"
2. 数字有限制为32位有符号整数

## 分析过程
1. 边界条件的判断
2. 数字是否超过了大小
3. 符号位的拍断

## 存在的问题
1. 忘了加号的情况
2. 没有注意输入进来只有一个符号的情况
## 代码
```python
class Solution:
    def myAtoi(self, str: str) -> int:

        # 1. 判断输入的边界条件
        if not str:
            return 0
        # 判断全空格
        elif not str.lstrip():
            return 0

        if len(str) == 1:
            if str.isdigit():
                return str
            else:
                return 0
        flag = 1
        res = 0
        # 2. 去除空格
        str = str.lstrip()
        str = str.rstrip()

        if '-' == str[0]:
            str = str[1:]
            flag = 0
        elif '+' == str[0]:
            str = str[1:]

        if str[0].isdigit():
            for i in str:
                if i.isdigit():
                    res *= 10
                    res += int(i)
                    if res >= 2 ** 31:
                        return 2 ** 31 -1 if flag else - 2 ** 31
                else:
                    return res if flag else -res
        else:
            return 0

        return res if flag else -res
```

## 结果
```
Runtime: 32 ms, faster than 68.56% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for String to Integer (atoi).
```
## 总结
写的代码丑， 行数太多。
2147483648 这个数字32位有符号存不到，只能存到 2147483648-1

## 参考代码
```python
class Solution:
    aviable_list=['0','1','2','3','4','5','6','7','8','9']
    def myAtoi(self, str: str) -> int:
        str=list(str)
        if not str:
            return 0
        while str[0]==' ':
            str.pop(0)
            if not str:
                return 0
        
        if str[0]=='-':
            sign_digit=-1
            str.pop(0)
        elif str[0]=='+':
            sign_digit=1
            str.pop(0)
        elif not (str[0] in self.aviable_list):
            return 0
        else:
            sign_digit=1
            
        res=0
        if not str:
            return 0
        s=str.pop(0)
        while s in self.aviable_list:
            temp=self.aviable_list.index(s)
            res=res*10+temp
            if str:
                s=str.pop(0)
            else:
                break
        out = res*sign_digit
        if out>2**31-1:
            return 2**31-1
        elif out<-2**31:
            return -2**31
        else:
            return res*sign_digit
        
```

-  利用辅助数组，可以代替使用isdigit()