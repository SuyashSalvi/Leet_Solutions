class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = [1]

        for row_num in range(1, rowIndex + 1):
            cur_row = [None for _ in range(row_num + 1)]
            cur_row[0], cur_row[-1] = 1, 1
            for i in range(1, len(cur_row) - 1):
                cur_row[i] = prev_row[i - 1] + prev_row[i]

            prev_row = cur_row
        return prev_row