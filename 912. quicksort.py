class Solution(object):
    def sortArray(self, nums):
        return self.quickSortArray(nums)

    def quickSortArray(self, nums):
        if len(nums) <= 1:
            return nums
        i, j = 0, len(nums)-1
        # median of 3 pivot
        pivot_indices = [0, len(nums)//2, -1]
        pivots = [nums[0], nums[len(nums)//2], nums[-1]]
        smallest = min(pivots)
        pivot_index = pivot_indices[pivots.index(smallest)]
        nums[pivot_index], nums[-1] = nums[-1], nums[pivot_index]
        while i < j:
            while i < j and nums[i] <= nums[-1]:# move i before or = to j
                i += 1
            while j > i and nums[j] >= nums[-1]:# if i < j move j closer or equal to i
                j -= 1
            # swap
            nums[i], nums[j] = nums[j], nums[i]

        nums[i], nums[-1] = nums[-1], nums[i]# swap pivot with middle
        # quick sort both partitions and combine them later
        return self.quickSortArray(nums[:i]) + [nums[i]] + self.quickSortArray(nums[i+1:])