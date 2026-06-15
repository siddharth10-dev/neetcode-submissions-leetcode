class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 1. Define the helper function right here inside the main function
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Mismatch! Use the helper function to test our two options
                return check_palindrome(s, left + 1, right) or check_palindrome(s, left, right - 1)
            
            # 2. If the letters match, move the pointers inward to keep checking
            left += 1
            right -= 1
            
        # 3. If we make it through the whole loop without issues, it's a valid palindrome
        return True

        