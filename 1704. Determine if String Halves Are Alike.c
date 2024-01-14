/*
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
*/
bool in(int* arr, int size, char target){
    int l = 0;
    int r = size;
    while(l <= r){
        int m = l + (r-l)/2;
        if(arr[m] == (int)target){
            return true;
        }else if(arr[m] < (int)target){
            l = m+1;
        }else{
            r = m-1;
        }
    }
    return false;
}

bool is_vowel(char v){
    // a=97,e=101,i=105,o=111,u=117
    // A=65,E=69,I=73,O=79,U=85
    if(v < 65 || v > 117){
        return false;
    }
    int vowels[10] = {65, 69, 73, 79, 85, 97, 101, 105, 111, 117};
    return in(vowels, sizeof(vowels)/sizeof(vowels[0]), v);// bin search
}

bool halvesAreAlike(char* s) {
    // calc the even length of the string
    int length = 0;
    for(char* c = s; *c != '\0'; c++){
        length++;
    }

    // create a ptr for the 2nd half of the string
    char* s2 = s;
    length /= 2;
    while(length > 0){
        s2++;
        length--;
    }

    // iterate both strings adding and subtracting the vowel count
    int vowelCount = 0;
    while(*s2 != '\0'){
        if(is_vowel(*s2)){
            vowelCount--;
        }
        if(is_vowel(*s)){
            vowelCount++;
        }
        s++;
        s2++;
    }
    return vowelCount == 0;
}