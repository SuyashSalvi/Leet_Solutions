class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            cur_row = [None for _ in range(row_num + 1)]
            cur_row[0], cur_row[-1] = 1, 1
            for i in range(1, len(cur_row) - 1):
                cur_row[i] = triangle[row_num - 1][i - 1] + triangle[row_num - 1][i]
            triangle.append(cur_row)
        return triangle