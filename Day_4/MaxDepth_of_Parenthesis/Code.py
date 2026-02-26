class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        max=0
        n=len(s)
        for i in range (n):
            if s[i]=='(':
                count+=1
            elif s[i]==')':
                count-=1
            if count>max:
                max=count
        return max
      
