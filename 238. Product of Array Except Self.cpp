/*
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
*/
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int left[nums.size()];
        left[0] = nums[0];
        for(int i = 1; i < nums.size(); i++){
            left[i] = left[i-1] * nums[i];
        }

        int right[nums.size()];
        right[nums.size()-1] = nums[nums.size()-1];
        for(int i = nums.size()-2; i > -1; i--){
            right[i] = right[i+1] * nums[i];
        }

        nums[0] = right[1];
        nums[nums.size()-1] = left[nums.size()-2];
        for(int i = 1; i < nums.size()-1; i++){
            nums[i] = left[i-1] * right[i+1];
        }
        return nums;
    }
};