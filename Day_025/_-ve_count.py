class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        col=len(grid[0])
        row=len(grid)
        r,c=row-1,col-1
        while (r>=0):
            if grid[r][c]<0:
                count+=1
                c-=1
                if (c==0):
                    r-=1
                    c=col-1
            else:
                r-=1
                c=col-1
        return count

