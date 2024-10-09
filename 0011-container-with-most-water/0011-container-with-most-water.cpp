class Solution {
public:
    int maxArea(const vector<int>& height) {
        int i = 0; // Initialize left pointer
        int j = height.size() - 1; // Initialize right pointer
        int ans = 0; // Variable to store the maximum area

        while (i <= j) {
            // Calculate the maximum area possible at this point
            ans = max(ans, (j - i) * min(height[i], height[j]));

            // Move the pointer pointing to the shorter line
            if (height[j] < height[i]) {
                j--; // Move the right pointer leftward
            } else {
                i++; // Move the left pointer rightward
            }
        }

        return ans;
    }
};