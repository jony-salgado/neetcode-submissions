# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()

        queue.append(root)
        ans = []
        while queue:
            curr = []
            for _ in range(len(queue)):
                element = queue.popleft()
                curr.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)

            ans.append(curr)
        
        return ans