from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cnt = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[cnt]
            cnt += 1
            if cnt == n:
                break

        quickSort = lambda array: array if len(array) <= 1 else quickSort(
            [item for item in array[1:] if item <= array[0]]) + [array[0]] + quickSort(
            [item for item in array[1:] if item > array[0]])
        new_list = quickSort(nums1[:m + n])
        for item in range(m + n):
            nums1[item] = new_list[item]
        return nums1


if __name__ == '__main__':
    A = Solution()
    print(A.merge([1, 2, 3, 0, 0, 0, 0, 0], 3, [2, 5, 6], 3))
