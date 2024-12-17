class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {}
        dic[1] = "1"
        dic[2] = "2"
        for i in range(3, n+1):
            dic[i] = str(int(dic[i-1]) + int(dic[i-2]))
        return int(dic[n])