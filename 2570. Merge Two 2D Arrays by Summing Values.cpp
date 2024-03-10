/*
You are given two 2D integer arrays nums1 and nums2.

    nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

    Only ids that appear in at least one of the two arrays should be included in the resulting array.
    Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be 0.

Return the resulting array. The returned array must be sorted in ascending order by id.
*/
class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        // merge and total both id,val pairs keeping id's unique
        std::unordered_map<int, int> dict;
        for(const vector<int>& pair : nums1){
            dict[pair[0]] += pair[1];
        }
        for(const vector<int>& pair : nums2){
            dict[pair[0]] += pair[1];
        }
        // add the merged pairs to output
        std::vector<vector<int>> output;
        for (auto it = dict.begin(); it != dict.end(); it++) {
            std::vector<int> pair(2);
            pair[0] = it->first;
            pair[1] = it->second;
            output.push_back(pair);
        }
        // sort the merged pairs by id (using lambda [](var a, var b){return a<b}) and return
        std::sort(output.begin(), output.end(), [](vector<int> a, vector<int> b){
            return a[0] < b[0];
        });
        return output;
    }
};