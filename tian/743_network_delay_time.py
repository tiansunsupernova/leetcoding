class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #1 build adjacency list and init dist list
        adj = [[] for _ in range(n)]
        for u,v,w in times:
            adj[u - 1].append([v - 1, w])

        #2 init dist and minheap
        dist = [float('inf')] *  n
        dist[k - 1] = 0
        heap = [(0, k - 1)] # time, node

        while heap:
            time, node = heapq.heappop(heap)

            if time > dist[node]: continue
            
            #3 explore neighbor nodes
            for neighbor, d_time in adj[node]:
                n_time = time + d_time

                #4 update and push to heap when finding a shorter path to a node
                if n_time < dist[neighbor]:
                    dist[neighbor] = n_time
                    heapq.heappush(heap, (n_time, neighbor))

        max_time = max(dist)
        return -1 if max_time == float('inf') else max_time