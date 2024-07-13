#User function Template for python3
from typing import List
import heapq
from collections import defaultdict
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        graph = defaultdict(list)
        for a, b, w in edges:
            graph[a].append((w, b))
            graph[b].append((w, a))
        
        # Dijkstra's algorithm initialization
        min_heap = [(0, 1)]  # (weight, node)
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[1] = 0
        previous_nodes = {i: None for i in range(1, n + 1)}
        
        while min_heap:
            current_weight, current_node = heapq.heappop(min_heap)
            
            if current_weight > distances[current_node]:
                continue
            
            for edge_weight, neighbor in graph[current_node]:
                distance = current_weight + edge_weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(min_heap, (distance, neighbor))
        
        # Reconstruct the path from 1 to n
        if distances[n] == float('inf'):
            return [-1]
        
        path = []
        current_node = n
        while current_node:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        
        path.reverse()
        return [distances[n]] + path

        


#{ 
 # Driver Code Starts
from collections import defaultdict


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)

# } Driver Code Ends