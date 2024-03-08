/*
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
*/
class Solution {
public:
    int* countingBuffer(string s, int min, int max, int* returnSize){
        *returnSize = max - min + 1;
        int* buffer = new int[*returnSize];
        // Initialize buffer elements to zero
        for (int i = 0; i < *returnSize; i++) {
            buffer[i] = 0;
        }
        // key=n-min and buffer[key] = count of n in nums
        for(int i = 0; i < s.size(); i++){
            buffer[(int)s[i] - min] += 1;
        }
        return buffer;
    }

    string frequencySort(string s) {
        int bufferSize;
        int* buffer = countingBuffer(s, 0, 127, &bufferSize);
        string output;
        for(int i = 0; i < bufferSize; i++){
            int largestIndex = 0;
            for(int j = 0; j < bufferSize; j++){
                if(buffer[largestIndex] < buffer[j]){
                    largestIndex = j;
                }
            }
            while(buffer[largestIndex] > 0){
                buffer[largestIndex]--;
                output.push_back((char)largestIndex);
            }
        }
        delete[] buffer;
        return output;
    }
};