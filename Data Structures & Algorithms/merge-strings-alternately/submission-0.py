class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1=0
        ptr2=0
        res=[]
        w1=len(word1)
        w2=len(word2)
        while (ptr1<w1)or(ptr2<w2):
            if ptr1<w1:
                res.append(word1[ptr1])
                ptr1+=1
            if ptr2<w2:
                res.append(word2[ptr2])
                ptr2+=1

        return"".join(res)
        