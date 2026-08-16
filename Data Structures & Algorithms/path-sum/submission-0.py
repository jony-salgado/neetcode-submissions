# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def backtracking(node, sum_) -> bool:
            if not node:
                return False

            sum_ += node.val
            if not node.left and not node.right:
                return sum_ == targetSum

            left = backtracking(node.left, sum_)
            right = backtracking(node.right, sum_)
            
            return left or right
        
        return backtracking(root, 0)