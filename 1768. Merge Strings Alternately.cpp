/*
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
*/
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::string output;
        int i = 0;
        while(i < word1.size() + word2.size() && i/2 < word1.size() && i/2 < word2.size()){
            if(i % 2 == 0){
                output += word1[i/2];
            } else {
                output += word2[i/2];
            }
            i++;
        }
        while(i/2 < word1.size()){
            output += word1[i/2];
            i+=2;
        }
        while(i/2 < word2.size()){
            output += word2[i/2];
            i+=2;
        }
        return output;
    }
};