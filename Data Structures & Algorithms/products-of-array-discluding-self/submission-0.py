class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        # LEFT PASS: Fill 'res' with prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # RIGHT PASS: Multiply 'res' by suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix   # Notice we use *= here to combine left and right!
            suffix *= nums[i]
            
        return res