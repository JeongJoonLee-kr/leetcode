class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strX = str(x)
        for i in range(len(strX)//2):
            if strX[i] == strX[len(strX)-(1+i)]:
                continue
            else:
                return False
        return True