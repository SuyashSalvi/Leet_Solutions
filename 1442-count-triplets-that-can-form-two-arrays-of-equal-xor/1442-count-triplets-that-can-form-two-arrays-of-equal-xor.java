class Solution {
    public int countTriplets(int[] arr) {
        int count = 0, n = arr.length;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int a = 0;
                for(int l = i;l<j;l++){
                    a ^= arr[l];
                }
                
                int b = 0;
                for(int k=j;k<n;k++){
                    b ^= arr[k];
                    if(a==b){
                        count++;
                    }
                }
            }
        }
        return count;
    }
}