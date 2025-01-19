class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # Initialize the number of operations with the first element of target
        operations = target[0]
        
        # Iterate through the target array and calculate the difference
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                # Add the positive difference to operations
                operations += target[i] - target[i - 1]
        
        return operations
