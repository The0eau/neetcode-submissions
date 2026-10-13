# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node, level):
            if not node:
                return
            
            if level == len(result):
                result.append([])
                
            result[level].append(node.val)
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
        final_result = []
        for i in result :
            final_result.append(i[-1])
        return final_result