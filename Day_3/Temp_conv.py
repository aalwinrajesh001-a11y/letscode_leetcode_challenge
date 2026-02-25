class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k=float(f'{(celsius+273.15):.5f}')
        f=float(f'{(celsius*1.80+32.00):.5f}')
        t=[k,f]
        return t
      
