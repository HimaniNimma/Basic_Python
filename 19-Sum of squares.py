#Sum of squares upto given number
class Solution:
    def sumOfSquares(self, n):
        res=0
        for i in range(1,n+1):
            res=res+i**2
        return res
