
/*
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.
*/
int lengthOfLastWord(char* s) {
    // base case
    if(*s == '\0'){
        return 0;
    }

    //lstrip(' ')
    while(*s == ' '){
        s++;
    }

    // count the length of the current string
    int length = 0;
    while(*s != ' ' && *s != '\0'){
        length++;
        s++;
    }

    int right = lengthOfLastWord(s);
    length = right <= 0 ? length : right;
    return length;

}