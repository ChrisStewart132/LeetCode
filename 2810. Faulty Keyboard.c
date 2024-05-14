/*
our laptop keyboard is faulty, and whenever you type a character 'i' on it, 
it reverses the string that you have written. Typing other characters works as expected.

You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.

Return the final string that will be present on your laptop screen.
*/
void reverseString(char* s, int length){
    for(int i = 0; i < length/2; i++){
        char temp = s[i];
        s[i] = s[length-1-i];
        s[length-1-i] = temp;
    }
}
char* finalString(char* s) {
    int length = strlen(s);
    char* output = calloc(length+1, sizeof(char));
    int j = 0;
    for(int i = 0; i < length; i++){
        if(s[i] == 'i'){
            reverseString(output, j);
        }else{
            output[j++] = s[i];
        }
    }
    return output;
}