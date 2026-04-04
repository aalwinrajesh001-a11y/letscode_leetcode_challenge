class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for i in sentences:
            k=len(i.split(" "))
            if k>m:
                m=k
        return m
            

        
