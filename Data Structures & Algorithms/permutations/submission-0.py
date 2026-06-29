class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(path, visited):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                visited[i] = True
                path.append(nums[i])
                
                backtrack(path, visited)
                
                path.pop()
                visited[i] = False
                
        backtrack([], [False] * len(nums))
        return res