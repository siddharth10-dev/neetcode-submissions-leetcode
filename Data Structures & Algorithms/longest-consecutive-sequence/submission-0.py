class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if it's a starting point (num - 1 is NOT in the set)
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Keep counting as long as the next consecutive number exists
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                # Update our record if this new streak is the longest one we've seen
                if current_streak > longest_streak:
                    longest_streak = current_streak

        return longest_streak