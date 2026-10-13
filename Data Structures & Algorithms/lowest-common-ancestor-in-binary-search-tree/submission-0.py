# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def link_(a,c):
            if a == c :
                return True
            elif a :
                return link_(a.right,c) or link_(a.left,c)
            else :
                return False
        left = link_(root.left,p) and link_(root.left,q)
        right = link_(root.right,p) and link_(root.right,q)
        if not right and not left:
            return root
        elif not right and left :
            return self.lowestCommonAncestor(root.left,p,q)
        else : 
            return self.lowestCommonAncestor(root.right,p,q)