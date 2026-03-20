class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sm=min(prices)
        prices.remove(sm)
        sm=sm+min(prices)
        if sm<=money:
            return money-sm
        else:
             return money
                    
                
        
