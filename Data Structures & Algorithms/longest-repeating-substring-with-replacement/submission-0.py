class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}
        l = 0
        max_freq = 0
        longest = 0
        
        for r in range(len(s)):
            count_map[s[r]] = count_map.get(s[r], 0) + 1
            max_freq = max(max_freq, count_map[s[r]])
            
            if (r - l + 1) - max_freq > k:
                count_map[s[l]] -= 1
                l += 1
                
            longest = max(longest, r - l + 1)
            
        return longest