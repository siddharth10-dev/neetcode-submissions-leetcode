class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26
        window_freq = [0] * 26

        for ch in s1:
            s1_freq[ord(ch) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):
            window_freq[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > len(s1):
                window_freq[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if window_freq == s1_freq:
                return True

        return False