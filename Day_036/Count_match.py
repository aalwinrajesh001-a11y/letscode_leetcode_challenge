class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        l=["type","color","name"]
        c=0
        if ruleKey in l:
            j=l.index(ruleKey)
        for i,row in enumerate(items):
            if row[j]==ruleValue:
                c+=1
        return c
        
        

        
