/*
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
*/
bool isIsomorphic(char* s, char* t) {
    int length = strlen(s);
    int cache[256] = {0};
    for(int i = 0; i < length; i++){
        const char a = s[i];
        const char b = t[i];
        for(int j = i; j < length && cache[a] == 0; j++){
            if((s[j] == a && t[j] != b) || (t[j] == b && s[j] != a)){
                return false;
            }
        }
        cache[a] = 1;
    }
    return true;
}