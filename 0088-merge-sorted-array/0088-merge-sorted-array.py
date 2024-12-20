class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1[:]
        i = 0
        j = 0
        k = 0
        while m and n:
            if tmp[i] > nums2[j]:
                nums1[k] = nums2[j]
                k += 1
                j += 1
                n -= 1
            else:
                nums1[k] = tmp[i]
                k += 1
                i += 1
                m -= 1
        while m > 0:
            nums1[k] = tmp[i]
            k += 1
            i += 1
            m -= 1
        while n > 0:
            nums1[k] = nums2[j]
            k += 1
            j += 1
            n -= 1
            



        