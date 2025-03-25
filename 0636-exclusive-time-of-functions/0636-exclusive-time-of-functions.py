from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n         # Initialize the result array for n functions
        stack = []            # Stack to keep track of function IDs currently running
        
        # Process the first log separately.
        first_log = logs[0].split(":")
        stack.append(int(first_log[0]))
        prev = int(first_log[2])
        
        # Process remaining logs
        for log in logs[1:]:
            parts = log.split(":")
            func_id = int(parts[0])
            typ = parts[1]
            timestamp = int(parts[2])
            
            if typ == "start":
                # If a new function starts, then the current function (top of stack)
                # was running from 'prev' until now.
                if stack:
                    res[stack[-1]] += timestamp - prev
                # Push the new function onto the stack
                stack.append(func_id)
                # Update the prev pointer to the current timestamp.
                prev = timestamp
            else:  # typ == "end"
                # The function on top of the stack ends, so add the time it ran.
                # We add 1 because the end timestamp is inclusive.
                res[stack[-1]] += timestamp - prev + 1
                # Pop the finished function.
                stack.pop()
                # Update 'prev' to the next timestamp after the current end.
                prev = timestamp + 1
        
        return res