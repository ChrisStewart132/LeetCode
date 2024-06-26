/*
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
*/
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        std::vector<int> cache(nums.size()+1);
        int i = 0;
        for(; i < nums.size(); i++){
            cache[nums[i]] = 1;
        }
        for(i = 0; i < nums.size(); i++){
            if(cache[i] == 0){
                break;
            }
        }
        return i;
    }
};