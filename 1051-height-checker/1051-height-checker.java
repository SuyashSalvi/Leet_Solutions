class Solution {
    public int heightChecker(int[] heights) {
        int n = heights.length, res = 0;
        int[] newH = new int[n];
        for(int i=0;i<n;i++){
            newH[i] = heights[i]; 
        }
        Arrays.sort(newH);
        for(int i=0;i<n;i++){
            if(newH[i] != heights[i]){
                res += 1;
            }
        }
        return res;
    }
}