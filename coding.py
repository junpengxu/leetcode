# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 1
        queue = [root]
        while queue:
            cnt = len(queue)
            for _ in range(cnt):
                node = queue.pop(0) # NOTE 这里不能按照索引位置去pop，因为queue在变化，要一直pop第一个位置
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth


if __name__ == '__main__':
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)
    a6 = TreeNode(6)
    a7 = TreeNode(7)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.left = a6
    a3.right = a7

    A = Solution()
    print(A.minDepth(a1))