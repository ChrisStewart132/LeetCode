/*
You are given a string s. The score of a string is defined as the sum of the absolute
 difference between the ASCII values of adjacent characters.

Return the score of s.
*/
int scoreOfString(char* s) {
    int output = 0;
    for(char* i = s; i[1] != '\0'; i++){
        output += abs(i[1]-i[0]);
    }
    return output;
}