class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r: int, c: int) -> List[List[int]]:

        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        ans = [[r,c]]
        d, move = 0, 0
        while(len(ans)< rows * cols):
            if(d%2==0):
                move += 1
            for i in range(move):
                r += dir[d][0]
                c += dir[d][1]
                if(r>=0 and r<rows and c>=0 and c<cols):
                    ans.append([r,c])

            d = (d + 1) % 4
        return ans