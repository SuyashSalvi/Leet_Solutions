class Solution {
    public int minProductSum(int[] nums1, int[] nums2) {
        int[] nums1count = new int[101];
        int[] nums2count = new int[101];
        int m = nums1.length;
        int n = nums1count.length;
        
        for(int i=0; i<m; i++){
            nums1count[nums1[i]] += 1;
            nums2count[nums2[i]] += 1;
        }
        
        int l = 0, r = n-1, productSum = 0;
        
        while(r>0 && l<n){
            if(nums1count[l]==0){
                l += 1;
            }
            if(nums2count[r]==0){
                r -= 1;
            }
            if(r>0 && l<n && nums1count[l] > 0 && nums2count[r]>0){
                int min_ = Math.min(nums1count[l],nums2count[r]);
                productSum += l*r*min_;
                nums1count[l] -= min_;
                nums2count[r] -= min_;
            }
        }
        return productSum;
    }
}