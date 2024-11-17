class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        list = []
        prefix = ""
        list_len = []
        shortest_len = 0
        for i in range(len(strs)):
            list_len.append(len(strs[i]))
        shortest_len = min(list_len)
        for i in range(shortest_len):
            for j in range(len(strs)):
                list.append(strs[j][i])
            if len(set(list)) == 1:
                prefix += list[0]
                list = []
        return prefix
        