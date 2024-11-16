class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_To_Integer = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result = 0
        for i in range(len(s)-1):
            if (roman_To_Integer.get(s[i]) < roman_To_Integer.get(s[i+1])):
                result -= roman_To_Integer.get(s[i])
            else:
                result += roman_To_Integer.get(s[i])
        result += roman_To_Integer.get(s[len(s)-1])
        return result