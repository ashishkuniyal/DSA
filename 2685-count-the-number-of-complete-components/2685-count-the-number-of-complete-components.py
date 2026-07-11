from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            vertices.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                vertices = []
                dfs(i)

                # Count edges in this component
                edge_count = 0
                for node in vertices:
                    edge_count += len(graph[node])

                edge_count //= 2   # every edge counted twice

                k = len(vertices)

                if edge_count == k * (k - 1) // 2:
                    ans += 1

        return ans