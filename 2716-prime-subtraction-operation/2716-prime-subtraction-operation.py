class Solution:
    def isPrime(self, x):
        for i in range(2,int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i-1]

            if bound <= 0:
                return False

            largest_prime = 0
            for j in range(bound-1,1,-1):
                if self.isPrime(j):
                    largest_prime = j
                    break
            
            nums[i] -= largest_prime
        return True
                