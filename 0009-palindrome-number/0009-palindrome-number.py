class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        len_a = len(a)
        for x in range(len_a):
            if a[x] != a[-(x+1)]:
                return False
        return True