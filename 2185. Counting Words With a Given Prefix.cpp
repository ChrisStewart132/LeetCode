/*
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.
*/
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int output = 0;
        for(const string& word: words){
            if(word.find(pref) == 0){
                output++;
            }
        }
        return output; 
    }
};
