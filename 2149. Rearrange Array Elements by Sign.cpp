/*
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
*/
class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> positive(nums.size()/2);
        vector<int> negative(nums.size()/2);
        for(int i = nums.size()-1; i > -1; i--){
            if(nums[i] < 0){
                negative.push_back(nums[i]);
            }else{
                positive.push_back(nums[i]);
            }
        }
        for(int i = 0; i < nums.size(); i+=2){
            nums[i] = positive.back();
            positive.pop_back();
            nums[i+1] = negative.back();
            negative.pop_back();
        }
        return nums;
    }
};