/*
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
*/
class Solution {
public:
    bool isPalindrome(string word){
        for(int i = 0; i < word.size()/2; i++){
            if(word[i] != word[word.size()-1-i]){
                return false;
            }
        }
        return true;
    }
    string firstPalindrome(vector<string>& words) {
        string output;
        for(const string& word: words){
            if(isPalindrome(word)){
                output = word;
                break;
            }
        }
        return output;
    }
};