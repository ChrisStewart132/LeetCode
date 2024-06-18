/*
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
*/
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        for(int i = 0; i < nums1.length; i++){
            set1.add(nums1[i]);
        }
        Set<Integer> set2 = new HashSet<>();
        for(int i = 0; i < nums2.length; i++){
            set2.add(nums2[i]);
        }
        set1.retainAll(set2);// intersection saved in set1

        int[] output = new int[set1.size()];
        int i = 0;
        for (int num : set1) {
            output[i++] = num;
        }
        return output;
    }
}