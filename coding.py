from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights) + 2
        stack = [0]
        heights = [0] + heights + [0]
        max_area = 0
        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]  # 从栈中pop出来的是递减的， 刚好符合使用短边计算乘长度
                width = i - stack[-1] - 1  # why
                max_area = max(max_area, width * height)
            stack.append(i)
        return max_area


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]

    solution = Solution()
    res = solution.largestRectangleArea(heights)
    print(res)
