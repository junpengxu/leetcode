import better_exceptions


class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def dfs(candidates, index, cnt_list):
            if sum(cnt_list) > target:
                return
            elif sum(cnt_list) < target:
                for i in range(index, len(candidates)):
                    dfs(candidates, i, cnt_list + [candidates[i]])
            else:
                res.append(cnt_list)

        dfs(candidates, 0, [])
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.combinationSum([2, 3, 5], 8))
    print(A.combinationSum([], 8))
    print(A.combinationSum([2,3,6,7], 7))
