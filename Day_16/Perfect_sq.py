class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root=int(sqrt(num))
        return root**2==num
        
