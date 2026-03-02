class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b,a%b)
        mi=min(nums)
        ma=max(nums)
        return gcd(mi,ma)
      
