class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n1=s.count('1')
        n0=s.count('0')
        num=""
        num=('1'*(n1-1))+('0'*n0)+'1'
        return num
        
        
