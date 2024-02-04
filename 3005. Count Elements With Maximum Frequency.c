/*
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
*/
int maxFrequencyElements(int* nums, int numsSize) {
    int cache[101];
    memset(cache, 0, sizeof(int)*101);
    for(int i = 0; i < numsSize; i++){
        cache[nums[i]]++;
    }
    int largest = cache[0];
    for(int i = 1; i < 101; i++){
        largest = largest < cache[i] ? cache[i] : largest;
    }
    int count = 0;
    for(int i = 1; i < 101; i++){
        count = largest == cache[i] ? count+1 : count;
    }
    return count*largest;
}