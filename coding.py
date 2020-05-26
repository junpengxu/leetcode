import better_exceptions


class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def dfs(candidates, index, cnt_list):
            if sum(cnt_list) > target:
                return
            elif sum(cnt_list) < target:
                for i in range(index+1, len(candidates)):
                    dfs(candidates, i, cnt_list + [candidates[i]])
            else:
                if cnt_list not in res:
                    res.append(cnt_list)
        dfs(candidates, -1, [])
        return res

if __name__ == '__main__':
    A = Solution()
    print(A.combinationSum2([10,1,2,7,6,1,5], 8))
