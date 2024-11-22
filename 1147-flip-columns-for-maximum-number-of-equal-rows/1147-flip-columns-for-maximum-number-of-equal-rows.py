class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hm = {}

        for cr in matrix:
            curPat = ''.join('T' if cr[0] == cur else 'F' for cur in cr)
            hm[curPat] = hm.get(curPat,0) + 1

        return max(hm.values(),default=0)