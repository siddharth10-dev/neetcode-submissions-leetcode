# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q=deque()
        q.append(root)
        res=[]

        while q :
            level_size=len(q)
            curr=[]
            for i in range(level_size):
                front=q.popleft()
                curr.append(front.val)
               

                if front.left:
                    q.append(front.left)

                if front.right:
                    q.append(front.right)

            res.append(curr)
            

        return res

            


