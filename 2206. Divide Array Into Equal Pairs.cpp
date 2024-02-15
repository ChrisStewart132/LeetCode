/*
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

    Each element belongs to exactly one pair.
    The elements present in a pair are equal.

Return true if nums can be divided into n pairs, otherwise return false.
*/
class Solution {
public:
    bool divideArray(vector<int>& nums) {
        std::unordered_map<int, int> frequencyMap;
        for (const int& num : nums) {
            frequencyMap[num]++;
        }
        for(const pair<int, int>& kv : frequencyMap){
            if(kv.second % 2 == 1){
                return false;
            }
        }
        return true;
    }
};