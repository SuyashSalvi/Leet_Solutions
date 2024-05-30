class Solution {
    public long countPairs(int[] nums1, int[] nums2) {
        // 0  6  5 -3 -> -3 0 5 6
        int n = nums1.length;
        int[] diff = new int[n];
        for(int i=0;i<n;i++){
            diff[i] = nums1[i] - nums2[i];
        }
        
        Arrays.sort(diff);
        int last = diff.length - 1;
        int first = 0;
        long ans = 0;

        while (last > first){

            while (last > first && diff[last] + diff[first] <= 0){
                first++;
            }

            if (last == first){
                break;
            } else {
                ans = ans + last - first;
                last--;
            }

        }

        return ans;
    }
} 