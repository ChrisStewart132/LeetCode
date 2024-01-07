/*
Given an array of strings words and a string s, determine if s is an acronym of words.

The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].

Return true if s is an acronym of words, and false otherwise. 
*/
bool isAcronym(char ** words, int wordsSize, char * s){
    for(int i = 0; i < wordsSize; i++){
        if(s == '\0' || words[i][0] != s[i]){
            return false;
        }
    }
    return s[wordsSize] == '\0';
}