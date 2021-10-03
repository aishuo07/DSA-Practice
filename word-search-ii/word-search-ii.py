class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        root = {}
        for i in words:
            trie = root
            for j in i:
                if j in trie:
                    trie= trie[j]
                else:
                    trie[j] = {}
                    trie= trie[j]
            trie['end'] = True
        print(root)
        vis = [[0]*m for _ in range(n)]
        ans = set()
        def rec(i, j, trie, temp):
            if 'end' in trie:
                ans.add(temp)
            vis[i][j] = 1
            for l in [[0, 1], [0,-1], [1, 0], [-1, 0]]:
                if 0<=i+l[0]<n and 0<=j+l[1]<m and board[i+l[0]][j+l[1]] in trie and vis[i+l[0]][j+l[1]] == 0:
                    rec(i+l[0], j+l[1], trie[board[i+l[0]][j+l[1]]], temp +board[i+l[0]][j+l[1]])
            vis[i][j] = 0
        
        for i in range(n):
            for j in range(m):
                if board[i][j] in root:
                    rec(i, j, root[board[i][j]], board[i][j])
                
        return list(ans)