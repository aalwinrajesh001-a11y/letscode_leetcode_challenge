class Solution:
    def countEven(self, num: int) -> int:
        def digsum(nu):
            su=0
            while nu!=0:
                su+=nu%10
                nu=nu//10
            return su%2==0
        count=0
        for i in range (2,num+1):
            if digsum(i):
                count+=1
        return count
        


        
