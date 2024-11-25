class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        state = ''.join(str(num) for row in board for num in row)
        visited = {}
        directions = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [3, 5, 1],
            [4, 2],
        ]

        def swap(s,i,j):
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return "".join(s)

        def dfs(state, zero_pos, moves):
            if state in visited and visited[state] <= moves:
                return 
            visited[state] = moves
            for next_pos in directions[zero_pos]:
                new_state = swap(state,zero_pos,next_pos)
                dfs(new_state,next_pos,moves+1)


        dfs(state,state.index('0'),0)

        return visited.get('123450',-1)