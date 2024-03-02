/*
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
*/
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int l = 0;
        int r = nums.size()-1;
        int i = nums.size()-1;
        std::vector<int> output(nums.size());
        for(int i = nums.size()-1; i > -1; i--){
            if(abs(nums[l]) > abs(nums[r])){
                output[i] = (nums[l]*nums[l]);
                l++;
            }else{
                output[i] = (nums[r]*nums[r]);
                r--;
            }
        }
        return output;
    }
};