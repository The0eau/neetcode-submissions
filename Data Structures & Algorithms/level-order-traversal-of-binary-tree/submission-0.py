# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def maxDepth(root):
            if not root :
                return 0
            else : 
                return max(maxDepth(root.left),maxDepth(root.right))+1
        max_depth = maxDepth(root)
        result = [[] for _ in range(max_depth)]
        index = 0
        def dfs(root,index):
            if not root :
                return None
            else : 
                result[index].append(root.val)
                dfs(root.left,index+1)
                dfs(root.right,index+1)
        dfs(root, index)
        return result

        
                