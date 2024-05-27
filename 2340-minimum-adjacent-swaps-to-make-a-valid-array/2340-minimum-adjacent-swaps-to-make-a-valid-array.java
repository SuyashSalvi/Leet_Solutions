class Solution {
    public int minimumSwaps(int[] nums) {
        int n = nums.length, minInd = 0, maxInd = 0;
    
        for(int i=0;i < n; i++){
            if(nums[i]<nums[minInd]){
                minInd = i;
            }
            if(nums[i]>=nums[maxInd]){
                maxInd = i;
            }
        }
        if(minInd < maxInd){
            return minInd + n - 1 - maxInd;
        }else if(minInd > maxInd){
            return minInd + n - 2 - maxInd;
        }
        return 0;
    }
}
