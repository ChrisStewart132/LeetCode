'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}   
        def _jump(i=0):
            if i in cache:# Check if the result is already memoized
                return cache[i]
            elif i == len(nums)-1:# Success
                self.solution_found = True
                return 0

            costs = [len(nums)]
            #for j in range(i+1, min(i+nums[i]+1, len(nums))):# jump 1->...->nums[i] ahead within nums
            for j in range(min(i+nums[i], len(nums)-1), i, -1):# jump nums[i]->...->1 back within nums
                if j not in cache:
                    cache[j] = 1 + _jump(j)
                costs.append(cache[j])

            return min(costs)

        return _jump()


                



