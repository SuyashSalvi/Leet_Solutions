class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 1. create adjacency list of the emails
        # 2. run dfs on all the subgraphs and merge them

        adjacent = defaultdict(list)
        visited = set()

        def dfs(email, mergeAccount):
            visited.add(email)
            mergeAccount.append(email)
            if email not in adjacent:
                return
            for neigh in adjacent[email]:
                if neigh not in visited:
                    dfs(neigh, mergeAccount)

        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[2:]:
                adjacent[first_email].append(email)
                adjacent[email].append(first_email)
        
        merged_accounts = []
        for acc in accounts:
            name = acc[0]
           
            first_email = acc[1]
            if first_email not in visited:
                mergeAccount = [name]
                dfs(first_email, mergeAccount)
                merged_accounts.append([name] + sorted(mergeAccount[1:]))
        return merged_accounts