class Solution {
    public int longestPalindrome(String s) {
        HashSet<Character> hs = new HashSet<>();
        int ans = 0;
        
        for(char c: s.toCharArray()){
            if(hs.contains(c)){
                hs.remove(c);
                ans += 2;
            } else{
                hs.add(c);
            }
        }
        if(!hs.isEmpty()){
            ans += 1;
        }
        
        return ans;
    }
}