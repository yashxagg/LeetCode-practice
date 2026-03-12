class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def check(threshold):
            parent = list(range(n))
            def find(i):
                if parent[i] != i: parent[i] = find(parent[i])
                return parent[i]
            
            def union(i, j):
                root_i, root_j = find(i), find(j)
                if root_i != root_j:
                    parent[root_i] = root_j
                    return True
                return False

            components = n
            edges_count = 0
            
            # 1. Mandatory Edges: Must not form a cycle and must meet threshold
            for u, v, s, must in edges:
                if must == 1:
                    if s < threshold: return False
                    if not union(u, v): return False # Cycle detected with a 'must' edge
                    components -= 1
                    edges_count += 1
            
            # 2. Optional Edges (No upgrade)
            for u, v, s, must in edges:
                if must == 0 and s >= threshold:
                    if edges_count < n - 1 and union(u, v):
                        components -= 1
                        edges_count += 1
            
            # 3. Optional Edges (With upgrade)
            upgrades = 0
            for u, v, s, must in edges:
                if must == 0 and s < threshold <= 2 * s and upgrades < k:
                    if edges_count < n - 1 and union(u, v):
                        components -= 1
                        edges_count += 1
                        upgrades += 1
            
            # Final validation: Must be connected AND have exactly n-1 edges
            return components == 1 and edges_count == n - 1

        low, high, ans = 0, 2 * 10**9, -1
        if not edges: return -1
        high = max(e[2] for e in edges) * 2

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans, low = mid, mid + 1
            else:
                high = mid - 1
        return ans

        