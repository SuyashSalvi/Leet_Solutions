class Solution {
    public int numSteps(String s) {
        int steps = 0;
        int carry = 0;
        for (int i = s.length() - 1; i > 0; i--) {
            // it means the bit was 0 and we added 1 (carry was 1) or the bit was 1 and no carry: Increment steps by 2 (one step for the addition, and one for the division). Set carry to 1 because adding 1 to an odd number results in an even number with a carry.
            if (s.charAt(i) - '0' + carry == 1) {
                carry = 1;
                steps += 2; 
            } else {
                steps += 1;
            }
        }
        return steps + carry;
    }
}