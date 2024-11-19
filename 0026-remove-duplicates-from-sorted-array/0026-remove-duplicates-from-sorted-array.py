class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seem = set()
        len_nums = len(nums)
        i = 0
        while i < len_nums:
            if nums[i] not in seem:
                seem.add(nums[i])
                i += 1
            else:
                nums.pop(i)
                len_nums -= 1
        return len(nums)