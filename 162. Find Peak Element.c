/*
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
*/
int findPeakElement(int* nums, int numsSize) {
    // base edge cases
    if (numsSize == 1) {
        return 0;
    }
    if (nums[0] > nums[1]) {
        return 0;
    }
    if (nums[numsSize - 1] > nums[numsSize - 2]) {
        return numsSize - 1;
    }

    unsigned int l = 0;
    unsigned int r = numsSize - 1;
    
    while (l < r) {
        unsigned int m = l + (r - l) / 2;

        if (nums[m] < nums[m + 1]) {
            l = m + 1;
        } else if (nums[m] > nums[m + 1]) {
            r = m;
        } else {
            // The peak can be on either side, move towards the larger element
            if (nums[l] > nums[r]) {
                r = m;
            } else {
                l = m + 1;
            }
        }
    }

    return l;
}
