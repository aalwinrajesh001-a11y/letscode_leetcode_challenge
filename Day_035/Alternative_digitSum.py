class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=0
        c=0
        N=int(str(n)[::-1])
        while N!=0:
            num=(N%10)*(-1)**c
            s+=num
            N=N//10
            c+=1
        return s
      
