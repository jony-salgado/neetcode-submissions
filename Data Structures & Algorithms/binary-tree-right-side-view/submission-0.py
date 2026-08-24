# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        deque = collections.deque()
        deque.append(root)
        ans = []
        while deque:
            get_this_level = False
            for i in range(len(deque)):
                node = deque.popleft()
                if not get_this_level:
                    ans.append(node.val)
                    get_this_level = True
                
                if node.right:
                    deque.append(node.right)
                if node.left:
                    deque.append(node.left)
        
        return ans