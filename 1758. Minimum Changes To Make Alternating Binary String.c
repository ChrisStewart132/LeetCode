/*
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
*/
#include <string.h>

int minOperations(char* s) {
    int l = strlen(s);
    char* copy = malloc(sizeof(char)*(l+1));
    strcpy(copy, s);

    copy[l] = '\0';
    int a = s[0] == '1'? 0:1;
    copy[0] = '1';
    for(char* c = copy+1; *(c) != '\0'; c++){
        if(*(c-1) == *c){
            *c = *c == '0'? '1':'0';
            a++;
        }
    }
    free(copy);

    int b = s[0] == '0'? 0:1;
    s[0] = '0';
    for(char* c = s+1; *(c) != '\0'; c++){
        if(*(c-1) == *c){
            *c = *c == '0'? '1':'0';
            b++;
        }
    }
    return a < b? a:b;
}