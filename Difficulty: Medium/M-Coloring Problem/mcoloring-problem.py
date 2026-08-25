class Solution:
    def isSafe(self, node, c, color, adj):
        for neighbour in adj[node]:
            if color[neighbour] == c: # c ka matlab wo color jo pehle se assign hai
                return False
        return True
        
    def solve(self, node, v, color, adj, m):
        # base case
        if node == v:
            return True
        
        # assigning colors
        for c in range(1, m+1):
            if self.isSafe(node, c, color, adj):
                color[node] = c
                
                if self.solve(node +1, v, color, adj, m):
                    return True
                
                color[node] = 0  # backtrack
        
        return False
            
    def graphColoring(self, v, edges, m):
        adj = [[] for _ in range(v)]
        for u, w in edges:
            adj[u].append(w)
            adj[w].append(u)
        
        color = [0] * v  # color array 0 ka matlab uncolored
        
        return self.solve(0, v, color, adj, m)
        
        