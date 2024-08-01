class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        ans=[0]
        m=k
        while True:
            if (ans[-1]+m)%n not in ans:
                ans.append((ans[-1]+m)%n)
                m=m+k

            else:
                break


        return [i+1 for i in range(n) if i not in ans]            