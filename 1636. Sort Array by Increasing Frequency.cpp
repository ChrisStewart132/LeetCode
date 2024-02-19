/*
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.
*/
class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        for(const int& num : nums){
            map[num]++;
        }
        // Step 1: Convert the vector into a max-heap
        std::make_heap(nums.begin(), nums.end(), [this](int a, int b) { return compare(a, b); });
        // Step 2: Perform heapsort
        std::sort_heap(nums.begin(), nums.end(), [this](int a, int b) { return compare(a, b); });
        return nums;
    }
private:
    std::unordered_map<int, int> map;
    bool compare(int a, int b){
        return map[a] < map[b] || (map[a] == map[b] && a > b);
    }
};