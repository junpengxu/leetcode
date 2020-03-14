import itertools
from typing import List


# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         phone = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
#         return [''.join(_) for _ in itertools.product(*(phone.get(int(_)) for _ in digits))] if digits else []


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        if len(digits)==0:
            return []
        res = ['']

        def dfs(nums, res):
            result = []
            if not nums:
                return res
            num = nums[0]
            for i in list(phone[int(num)]):
                for j in res:
                    result.append(j+i)
            return dfs(nums[1:], result)

        a =  dfs(digits, res)
        return a
print(Solution().letterCombinations('23'))