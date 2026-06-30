class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def canShip(capacity):
            current_weight = 0
            required_days = 1
            for weight in weights:
                if current_weight + weight > capacity:
                    required_days += 1
                    current_weight = 0
                current_weight += weight
            return required_days <= days

        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            if canShip(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans