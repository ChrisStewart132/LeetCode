/*
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
*/
class Solution {
public:
    string customSortString(string order, string s) {
        std::unordered_map<char, int> map;
        for(int i = 0; i < order.size(); i++){
            map[order[i]] = i;
        }

        // sort using compare that utulizes the map
        std::sort(s.begin(), s.end(),
         [&map](char a, char b){
             return map[a] < map[b];
         });

         return s;
    }

};