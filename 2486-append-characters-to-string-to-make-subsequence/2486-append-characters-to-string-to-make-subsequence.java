class Solution {
    public int appendCharacters(String s, String t) {
        int j = 0, n = s.length(), m = t.length();
        for(int i = 0;i<n;i++){
            if(s.charAt(i) == t.charAt(j)){
                j++;
            }
            if(j>=m){
                    break;
                }
        }
        return m-j;
    }
}