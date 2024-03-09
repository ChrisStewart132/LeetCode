/*
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
*/
int getCommon(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int l=0, r=0;
    while(l < nums1Size && r < nums2Size){
        if(nums1[l] == nums2[r]){
            return nums1[l];
        }else if(nums1[l] < nums2[r]){
            l++;
        }else{
            r++;
        }
    }
    return -1;
}