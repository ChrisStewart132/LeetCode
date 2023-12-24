/*
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
*/
int maxScore(char* s) {
    int nOnes = 0;
    int l = 0;
    for(int i = 0; s[i]; i++){
        if(s[i] == '1'){
            nOnes++;
        }
        l++;
    }
    int score = 0;
    int prev = s[0] == '0'? 1:-1;
    score = prev + nOnes;
    for(int i = 1; i < l-1; i++){// calc from left
        int curr = s[i] == '0'? 1:-1;
        prev = curr + prev;
        if(prev + nOnes > score){
            score = prev + nOnes;
        }
    }
    return score;
}