class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        l=dimensions
        m=0
        pmax=0
        for i in range(len(l)):
            diag=l[i][0]**2+l[i][1]**2
            pdct=l[i][0]*l[i][1]
            if diag>m:
                m=diag
                pmax=pdct
            elif diag==m:
                pmax=max(pmax,pdct)
        return pmax
