class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket={}
        for word in strs:
            signature="".join(sorted(word))
            
            if signature not in bucket:
                bucket[signature]=[]

            bucket[signature].append(word)
        return list(bucket.values())