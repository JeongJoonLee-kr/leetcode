class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end   = x // 2
        if x == 0:
            return 0
        if x == 1:
            return 1
        while start <= end:
            medium = (start + end) // 2
            if medium**2 == x:
                return medium
            elif medium**2 > x:
                end = medium - 1
            elif medium**2 < x:
                start = medium + 1
        return start - 1
        