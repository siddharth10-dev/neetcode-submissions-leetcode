class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(remaining, start, path):
            if remaining == 0:
                result.append(list(path))
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(remaining - candidates[i], i, path)
                path.pop()
        
        backtrack(target, 0, [])
        return result