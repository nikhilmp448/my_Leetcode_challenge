from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []

        row = [1]
        for i in range(1, rowIndex + 1):
            # Calculate the next element using combinations
            next_element = row[-1] * (rowIndex - i + 1) // i
            row.append(next_element)

        return row
    
x=Solution()


for i in range(10):
    print(x.getRow(i))
