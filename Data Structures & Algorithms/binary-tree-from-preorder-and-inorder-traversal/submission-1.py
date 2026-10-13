# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
    
        preorder_iter = iter(preorder)
        
        
        def construct(in_left, in_right):
           
            if in_left > in_right:
                return None
            
            
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            
            mid = inorder_index_map[root_val]
            
           
            root.left = construct(in_left, mid - 1)
            root.right = construct(mid + 1, in_right)
            
            return root
            
        
        return construct(0, len(inorder) - 1)