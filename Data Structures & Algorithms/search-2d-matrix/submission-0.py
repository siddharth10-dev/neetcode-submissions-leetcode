class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        left=0
        right=(rows*cols)-1
        while left <= right:
            m=(left+right)//2
            row=m//cols
            col=m%cols
            if(matrix[row][col]==target):
                return True
            elif(matrix[row][col]<target):
                left=m+1
            else:
                right=m-1
            
        return False
        