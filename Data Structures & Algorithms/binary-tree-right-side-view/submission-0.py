# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        lvl=[]
        q=[root]
        while q !=[] and root is not None:
            for node in q:
                if node.left:
                    lvl.append(node.left)

                if node.right:
                    lvl.append(node.right)
                
            res.append(node.val)
            q=lvl
            lvl=[]

        return res


        