class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:  
            return 0

        queue = [root]
        depth = 0

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                current_node = queue.pop(0)
            
                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right: 
                    queue.append(current_node.right)

            depth += 1

        return depth

        

        
        