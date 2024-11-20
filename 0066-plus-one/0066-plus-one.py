class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if set(digits) == {9}:
            n_zero = len(digits)
            ls = [1]
            for i in range(n_zero):
                ls.append(0)
            return ls
        if digits[len(digits)-1] == 9:
            for i in range(1, len(digits)+1):
                if digits[len(digits)-i] != 9:
                    digits[len(digits)-i] += 1
                    return digits
                else:
                    digits[len(digits)-i] = 0
        else:
            digits[len(digits)-1] += 1
        return digits