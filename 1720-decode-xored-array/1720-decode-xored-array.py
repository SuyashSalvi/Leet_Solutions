class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for n in encoded:
            ans.append(n^ans[-1])
        print(ans)
        return ans