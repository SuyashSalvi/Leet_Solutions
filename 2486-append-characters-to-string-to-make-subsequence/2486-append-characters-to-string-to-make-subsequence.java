class Solution {
    public int appendCharacters(String s, String t) {
        int j = 0, ans = Integer.MAX_VALUE, n = s.length(), m = t.length();
        for(int i = 0;i<n;i++){
            if(s.charAt(i) == t.charAt(j)){
                j++;
                ans = Math.min(ans, m-j);
            }
            if(j>=m){
                    break;
                }
        }
        if(ans==2147483647){
            return m;
        } else{
            return ans;
        }
    }
}