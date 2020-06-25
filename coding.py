class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix: return False

        def binary_search(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        # find row
        first_col = [matrix[j][0] for j in range(len(matrix))]
        end_col = [matrix[j][-1] for j in range(len(matrix))]
        index = zip(first_col, end_col)
        for _index, (x, y) in enumerate(index):
            if x <= target and target <= y:
                break
        nums = [matrix[_index][i] for i in range(len(matrix[0]))]
        position = binary_search(nums, target)
        if position is False:
            return False
        return True


if __name__ == '__main__':
    A = Solution()
    # print(A.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13))
    # print(A.searchMatrix([[1]], 1))
    print(A.searchMatrix([[-10,-8,-6,-4,-3],[0,2,3,4,5],[8,9,10,10,12]], 0))