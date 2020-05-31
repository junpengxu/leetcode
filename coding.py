class Solution:
    def permute(self, nums):
        res = []
        buf = [([], nums)]  # 存放了所有的
        while buf:
            tmp_list, nums = buf.pop(0)
            if not nums:
                res.append(tmp_list)
            else:
                for i in range(len(nums)):
                    buf.append((tmp_list + [nums[i]], nums[:i] + nums[i + 1:]))
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.permute([1, 2, 3]))


