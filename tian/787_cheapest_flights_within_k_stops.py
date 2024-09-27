class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # 1 create and populate adj list
        adj = [[] for _ in range(n)]
        for from_i, to_i, price_i in flights:
            adj[from_i].append([to_i, price_i])

        # 2 init dist and min_heap
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0
        heap = [(0, 0, src)] # stops, c_price, node

        # 3 run heap
        while heap:
            stops, c_price, node = heapq.heappop(heap)
            # 4 update neighbor
            for neighbor, d_price in adj[node]:
                new_price = c_price + d_price
                if neighbor == dst:
                    if stops <= k and new_price < dist[dst]:
                        dist[dst] = new_price
                else:
                    if stops < k and new_price < dist[neighbor]:
                        dist[neighbor] = new_price
                        heapq.heappush(heap, (stops + 1, new_price, neighbor))
        return - 1 if dist[dst] == float("inf") else dist[dst]

        