class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        currentIndex = 0
        answer = list()
        while currentIndex < len(nums):
            newTarget = target - nums[currentIndex]
            newNums = nums[currentIndex+1:]
            for i in newNums:
                if i == newTarget:
                    offset = newNums.index(i) + 1
                    answer.append(currentIndex)
                    answer.append(currentIndex + offset)
                if len(answer) == 2:
                    return answer
            currentIndex += 1
        
                
        