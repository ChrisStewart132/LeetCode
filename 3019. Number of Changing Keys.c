/*
You are given a 0-indexed string s typed by a user.
Changing a key is defined as using a key different from the last used key.
For example, s = "ab" has a change of a key while s = "bBBb" does not have any.

Return the number of times the user had to change the key.

Note: Modifiers like shift or caps lock won't be counted in changing the key that
 is if a user typed the letter 'a' and then the letter 'A' then it will not be 
 considered as a changing of key.
*/
int countKeyChanges(char* s) {
    int output = 0;
    for(char* c = s+1; *c != '\0'; c++){
        if(*c != *s && abs((int)c[0] - (int)s[0]) != 32){
            output++;
        }
        s++;
    }
    return output;
}