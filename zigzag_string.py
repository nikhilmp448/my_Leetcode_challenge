class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        direction = 1  # 1 for moving down, -1 for moving up

        for char in s:
            rows[current_row] += char

            # Change direction if at the top or bottom row
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        result = ''.join(rows)
        return result
