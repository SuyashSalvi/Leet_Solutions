class Solution {
    public int minimumKeypresses(String s) {
        Integer[] count = new Integer[26];
        Arrays.fill(count,0);
        for(int i=0; i<s.length();i++){
            count[s.charAt(i)-'a'] += 1;
        }
        Arrays.sort(count,(a,b)->b-a);
        int ans = 0;
        for(int i=0;i<26;i++){
            if(i<9){
                ans += count[i];
            }else if(i<18){
                ans += 2 * count[i];
            }else{
                ans += 3 * count[i];
            }
        }
        return ans;
    }
}