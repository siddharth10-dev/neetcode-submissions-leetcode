class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for i in nums:
            if i not in counts:
                counts[i]=1
            else:
                counts[i]+=1

        sorted_numbers = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)

        return sorted_numbers[:k]