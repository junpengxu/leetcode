class Solution:
    def isValid(self, s: str) -> bool:
        parent_dict = {')': '(', '}': '{', ']': '['}
        tmp = []
        if len(s) == 1:
            return False
        for item in s:
            if item not in parent_dict:
                tmp.append(item)
            elif not tmp:
                return False
            elif tmp[-1] != parent_dict[item]:
                return False
            else:
                tmp.pop(-1)
        return tmp == []


if __name__ == '__main__':
    assert Solution().isValid('()(){}') == True
    assert Solution().isValid('()(){[}') == False
    assert Solution().isValid('()') == True
    assert Solution().isValid('(]') == False
    assert Solution().isValid('((') == False
    assert Solution().isValid('){') == False
