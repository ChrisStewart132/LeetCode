/*
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int min(int a, int b){
    return a<b?a:b;
}
int* distributeCandies(int candies, int num_people, int* returnSize) {
    // sum = (n*(n+1))/2
    *returnSize = num_people;
    int* output = calloc(returnSize[0], sizeof(int));
    int i = 1;
    int j = 0;
    while(candies > 0){
        output[j++ % num_people] += min(i, candies);
        candies -= i++;
    }
    return output;
}