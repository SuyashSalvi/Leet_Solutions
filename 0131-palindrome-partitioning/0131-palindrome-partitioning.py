class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pali(s):
            return s == s[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
            for end in range(start, len(s)):
                if is_pali(s[start:end+1]):
                    backtrack(end+1,path+[s[start:end+1]])
        
        res = []
        backtrack(0,[])
        return res