/*
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
*/
#include <algorithm>    // std::make_heap, std::pop_heap, std::push_heap
#include <vector>       // std::vector

class Solution {
public:
    static bool compare(std::pair<int, int>& a, std::pair<int, int>& b) {
        return a.second < b.second;  
    }
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // map the num->freq
        std::unordered_map<int, int> map;
        for(const int& num: nums){
            if(map.contains(num)){
                map[num]++;
            }else{
                map[num] = 1;
            }
        }

        // make an arr of pairs (num, freq) from the map
        std::vector<std::pair<int, int>> heap;
        for(const std::pair<int, int>& kv : map){
            heap.push_back(kv);
        }

        // heapify the pairs O(n)
        std::make_heap(heap.begin(), heap.end(), compare);
        
        std::vector<int> output;
        // Pop the k most frequent elements (klogN)
        for (int i = 0; i < k; i++) {
            std::pop_heap(heap.begin(), heap.end(), compare);
            output.push_back(heap.back().first);
            heap.pop_back();
        }

        return output;
    }
};