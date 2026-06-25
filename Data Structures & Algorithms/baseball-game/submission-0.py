class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        for i in operations:

            if i=="+":
                new_score=s[-1]+s[-2]
                s.append(new_score)

            elif i=="D":
                new_score=2*s[-1]
                s.append(new_score)

            elif i=="C":
                s.pop()

            else:
                s.append(int(i))

        return sum(s)