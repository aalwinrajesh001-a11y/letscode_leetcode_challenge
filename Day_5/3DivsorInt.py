class Solution:
    def isThree(self, n: int) -> bool:
        num=(sqrt(n))
        if int(num)**2==n and n>2:
            for i in range (2,int(num)):
                if int(num)%i==0:
                    return False
            else:
                return True
        else:
            return False
          
