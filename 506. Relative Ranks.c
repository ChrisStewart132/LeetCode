/*
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

    The 1st place athlete's rank is "Gold Medal".
    The 2nd place athlete's rank is "Silver Medal".
    The 3rd place athlete's rank is "Bronze Medal".
    For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.
*/
int search(int* nums, int numsSize, int target) {
    int l = 0;
    int r = numsSize-1;
    while(l <= r){
        int m = (l+r)/2;
        if(nums[m] == target){
            return m;
        }else if(nums[m] < target){
            r=m-1;
        }else{
            l=m+1;
        }
    }
    return l;
}
int compare(const void *a, const void *b) {
    return (*(int*)b) - (*(int*)a);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findRelativeRanks(int* score, int scoreSize, int* returnSize) {
    // create sorted copy of score
    int* sorted_score = malloc(sizeof(int)*scoreSize);
    memcpy(sorted_score, score, sizeof(int)*scoreSize);
    qsort(sorted_score, scoreSize, sizeof(int), compare);

    // alloc and calcualte output arr
    *returnSize = scoreSize;
    char** output = malloc(sizeof(char*)*returnSize[0]);
    const char* medals[] = {"Gold Medal", "Silver Medal", "Bronze Medal"};
    for(int i = 0; i < scoreSize; i++){
        int s = score[i];
        int idx = search(sorted_score, scoreSize, s);
        if(idx < 3){
            output[i] = strdup(medals[idx]);
        }else{
            asprintf(&output[i], "%d", idx + 1); // Convert rank to string
        }
    }

    free(sorted_score);
    return output;
}