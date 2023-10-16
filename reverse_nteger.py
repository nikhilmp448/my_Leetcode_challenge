class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            reversed_x = int(str(x)[::-1])
        else:
            reversed_x = -int(str(-x)[::-1])

        return reversed_x
        