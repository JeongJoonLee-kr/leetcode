class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if target > nums[m]:
                l = m +1
            else:
                if target == nums[m] and nums[m-1] != target:
                    return m
                else:
                    r = m-1
        return l
