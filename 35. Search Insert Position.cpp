/*
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
*/
class Solution {
public:
    int searchInsert(vector<int>& nums, int target, int low=0, int high=-1) {
        /*recursive binary search, returns index*/
        if(high == -1){
            high = nums.size()-1;
        }
        int mid = (int)((low+high) / 2);

        if(nums[mid] == target) {// found target
            return mid;
        }
        else if(low == high){// 
            if(nums[mid] < target) {
                return low+1;
            }else {
                return low;
            }
        }
        else if(nums[mid] < target) {
            return searchInsert(nums, target, mid+1, high);
        }else {
            return searchInsert(nums, target, low, mid);
        }
        return mid;
    }
};