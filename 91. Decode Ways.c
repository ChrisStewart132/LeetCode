/*
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
*/
#include <string.h>//strlen
int _numDecodings(char* s, int l, int r, int* dp){
    if(dp[l] != -1){
        return dp[l];
    }
    if(s[l] == '0'){
        return 0;
    }
    if(l >= r){// valid decoding
        return 1;
    }
    int output = 0;
    if(r-l > 1 && (s[l] == '1' || s[l] == '2')){
        if(s[l+1] == '0'){
            dp[l+2] = _numDecodings(s, l+2, r, dp);// 10,20
            return dp[l+2];
        }else if(s[l] == '2' && s[l+1] < '7'){
            dp[l+2] = _numDecodings(s, l+2, r, dp);// 21-26
            output += dp[l+2];
        }else if(s[l] == '1'){
            dp[l+2] = _numDecodings(s, l+2, r, dp);// 11-19
            output += dp[l+2];
        }
    }
    dp[l+1] = _numDecodings(s, l+1, r, dp);// 1-9
    output += dp[l+1];
    return output;
}

int numDecodings(char* s) {
    if(*s == '0'){
        return 0;
    }
    int r = strlen(s);
    int dp[r+1];
    memset(dp, -1, sizeof(dp));
    int output = _numDecodings(s, 0, r, dp);
    return output;
}