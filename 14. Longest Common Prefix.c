/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
*/
char * longestCommonPrefix(char ** strs, int strsSize){
    if (strsSize == 1) {// base case of single str
        return strs[0];
    }

    int length = 0;// obtain the length of the prefix
    bool escape = false;// flag to stop searching for a prefix when the minimum length string is found
    for(size_t i = 0;i < 200; i++){// iterate char index (max possible strlen is 200)
        char c = strs[0][i];// tail char of the current prefix
        for(size_t j = 0;j < strsSize; j++){// iterate each string confirming the ith char is consistent
            char* str = strs[j];
            if(str[i] != c || str[i] == '\0'){// prefix not consistent or end of a string encountered
                escape = true;
                break;
            }
        }
        length = i;
        if(escape){// minimum length string found exiting
            break;
        }
    }
    //printf("%d\n", length);
    char* str = (char*)malloc((length+1)*sizeof(char));// alloc the output str
    for(size_t i = 0;i < length; i++){// iterate the prefix characters out of the first string
        str[i] = strs[0][i];// assign the prefix char's
    }
    str[length] = '\0';// null terminate the str
    return str;
}