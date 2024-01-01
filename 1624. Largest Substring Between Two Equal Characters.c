/*
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.
*/
int max(int a, int b){
    return a > b? a : b;
}

int _maxLengthBetweenEqualCharacters(char* s, int l, int r, int** dp) {
    if(l == r){
        return -1;
    } else if(s[l] == s[r]){
        return r-l-1;
    }
    if (dp[l][r] != -1) {
        return dp[l][r];
    }

    dp[l][r] = max(_maxLengthBetweenEqualCharacters(s, l + 1, r, dp),
                   _maxLengthBetweenEqualCharacters(s, l, r - 1, dp));

    return dp[l][r];
}

int maxLengthBetweenEqualCharacters(char* s) {
    int n = strlen(s);
    
    int** dp = (int**)malloc(sizeof(int*) * n);
    for (int i = 0; i < n; ++i) {
        dp[i] = (int*)malloc(sizeof(int) * n);
        memset(dp[i], -1, sizeof(int) * n);
    }

    int r = n - 1;
    int l = 0;
    int output = _maxLengthBetweenEqualCharacters(s, l, r, dp);

    for (int i = 0; i < n; ++i) {
        free(dp[i]);
    }
    free(dp);

    return output;
}