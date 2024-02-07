/*
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
*/
int maxIndex(int* arr, int size){
    int index = 0;
    for(int i = 1; i < size; i++){
        if(arr[i] > arr[index]){
            index = i;
        }
    }
    return index;
}

void countingSort(char* nums, int numsSize, char min, char max){
    int bufferSize = (max-min+1);// min element indexes to 0 with inclusive maximum value at the tail
    int* buffer = (int*)calloc(bufferSize, sizeof(int));
    for(int i = 0;i < numsSize; i++){
        buffer[nums[i]-min] += 1;
    }

    int j = 0;// index to sort in place the original arr
    while(j < numsSize){
        // select maximum frequency 
        int i = maxIndex(buffer, bufferSize);
        while(buffer[i] > 0){
            nums[j++] = (char)(min+i);
            buffer[i]--;
        }
    }
    free(buffer);
}

char* frequencySort(char* s) {
    /*
    >>> ord('a')
    97
    >>> ord('z')
    122
    >>> ord('A')
    65
    >>> ord('Z')
    90
    >>> 
    */
    // using counting sort buffer to count the frequencies of characters
    // processing similar to selection sort, selecting the largest frequenceis and sorting in place
    countingSort(s, strlen(s), 0, 127);// tests included more chars than expected
    return s;
}