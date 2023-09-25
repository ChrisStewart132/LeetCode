/*
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
*/

bool isSubsequence(char * s, char * t){
    for(; *t != '\0'; t++){// iterate the string t until null termination reached
        if(*t == *s){// if current char t == current char s, increment s ptr
            s++;
        }
    }
    return *s == '\0';// s should point to the end/null if all chars were found within t
}