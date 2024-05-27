class Solution {
    public int minimumSplits(int[] nums) {
        int n = nums.length;
        
        int cur = 0, res = 1;
        for(int i=0;i<n;i++){
            cur = gcd(cur, nums[i]);
            if(cur == 1){
                cur = nums[i];
                res++;
            }
        }
        return res;
    }
    
    public static int gcd(int x, int y){
            while(y!=0){
                int temp = y;
                y = x%y;
                x = temp;
            }
            return x;
        }
}