/*
You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
*/
class Solution {
public:
    int xorOperation(int n, int start) {
        int output = start;
        for(int i = 1; i < n; i++){
            start += 2;
            output ^= start; 
        }
        return output;
    }
};