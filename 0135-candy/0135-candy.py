from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Single‐pass O(n) time, O(1) extra space:
        We keep track of the current rising‐slope length (up), 
        falling‐slope length (down), and the previous slope (prev).
        We accumulate candies into `total` as we go.
        """
        n = len(ratings)
        if n <= 1:
            return n

        total = 1    # give the first child 1 candy
        up = 0       # length of current strictly rising run
        down = 0     # length of current strictly falling run
        prev = 0     # previous slope: +1 (rising), 0 (flat), -1 (falling)

        for i in range(1, n):
            # determine the new slope
            if ratings[i] > ratings[i-1]:
                curr = 1
            elif ratings[i] < ratings[i-1]:
                curr = -1
            else:
                curr = 0

            # if we just finished a falling run (prev<0) and now flat/rise,
            # or we just finished a rising run (prev>0) and now flat,
            # reset up/down counters
            if (prev < 0 and curr >= 0) or (prev > 0 and curr == 0):
                up = down = 0

            # extend the current run and add candies appropriately
            if curr > 0:           # rising
                up += 1
                total += up + 1    # we need (up+1) candies at this point
            elif curr < 0:         # falling
                down += 1
                # if the falling run overtakes the previous rising run,
                # the peak needs one extra candy
                if down > up:
                    total += down + 1
                else:
                    total += down
            else:                  # flat
                total += 1         # just one candy

            prev = curr

        return total