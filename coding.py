class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        closest = []

        for i, num in enumerate(nums[0:-2]):
            l, r = i + 1, length - 1

            # different with others' solution

            if num + nums[r] + nums[r - 1] < target:
                closest.append(num + nums[r] + nums[r - 1])
            elif num + nums[l] + nums[l + 1] > target:
                closest.append(num + nums[l] + nums[l + 1])
            else:
                while l < r:
                    sum = num + nums[l] + nums[r]
                    closest.append(sum)
                    if sum < target:
                        l += 1
                    elif sum > target:
                        r -= 1
                    else:
                        return target

        closest.sort(key=lambda x: abs(x - target))
        return closest[0]
        '''
        N = len(nums)
        nums.sort()
        res = float('inf') # sum of 3 number
        for t in range(N):
            i, j = t + 1, N - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if abs(_sum - target) < abs(res - target):
                    res = _sum
                if _sum > target:
                    j -= 1
                elif _sum < target:
                    i += 1
                else:
                    return target
        return res
        '''