class Solution:
    def climbStairs(self, n: int) -> int:
        a=0
        b=1
        if n<=3:
            return n
        else:
            for i in range(n):
                t=a+b
                a=b
                b=t
            return t
