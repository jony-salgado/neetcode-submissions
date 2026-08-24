# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return ans

        deque = collections.deque([(root, root.val)])

        while deque:
            n = len(deque)
            for i in range(n):
                node, current_max = deque.popleft()
                if node.val >= current_max:
                    ans += 1
                
                new_max = max(current_max, node.val)
                if node.left:
                    deque.append((node.left, new_max))
                if node.right:
                    deque.append((node.right, new_max))
        
        return ans
                    