class Solution:
    def subsets(self, nums):
        res = []
        subset = []

        def dfs(i):
            # Base case: processed all elements
            if i == len(nums):
                res.append(subset.copy())
                return

            # Choice 1: include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Undo the choice (backtrack)
            subset.pop()

            # Choice 2: exclude nums[i]
            dfs(i + 1)

        dfs(0)
        return res