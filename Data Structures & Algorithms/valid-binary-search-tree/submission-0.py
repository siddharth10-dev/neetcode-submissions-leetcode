# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,low,high):
            if node is None:
                return True

            if node.val<=low or node.val>=high:
                return False

            is_left_valid=validate(node.left,low,node.val)

            is_right_valid=validate(node.right,node.val,high)

            return is_left_valid and is_right_valid


        return validate(root,float('-inf'),float('inf'))
        