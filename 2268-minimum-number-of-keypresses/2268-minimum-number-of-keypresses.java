class Solution {
    public int minimumKeypresses(String s) {
        // Step 1: Create a dictionary to count each character of s
        Map<Character, Integer> charCount = new HashMap<>();
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        
        // Step 2: Arrange the characters in descending order of their values
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        pq.addAll(charCount.values());
        
        // Step 3: Calculate the minimum keypresses
        int res = 0;
        int[] multiplier = {1, 2, 3}; // Multiplier for adding values
        int keys = 0;
        while (!pq.isEmpty()) {
            int count = pq.poll(); // Get the count of the most frequent character
            int presses = count * multiplier[Math.min(keys / 9, 2)]; // Calculate keypresses for this count
            res += presses; // Add keypresses to result
            keys++; // Increment keys pressed
        }
        
        return res;

    }
}