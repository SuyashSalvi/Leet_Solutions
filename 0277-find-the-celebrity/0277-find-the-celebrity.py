# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celeb_candidate = 0
        for i in range(1,n):
            if knows(celeb_candidate,i):
                celeb_candidate = i
        if self.is_celeb(celeb_candidate):
            return celeb_candidate
        return -1

    def is_celeb(self,i):
        for j in range(self.n):
            if i == j: continue
            if knows(i,j) or not knows(j,i):
                return False
        return True