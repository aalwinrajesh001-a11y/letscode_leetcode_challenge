class Solution:
    def reverseWords(self, s: str) -> str:
        l=list()
        l=s.split(" ")
        st=""
        for i in l:
            st=st+i[::-1]+" "
        return st[:-1]
        
