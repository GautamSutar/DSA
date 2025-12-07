from collections import defaultdict, deque


class Solution:
    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n

        group_graph = [[] for _ in range(m)]
        group_indegree = [0] * m

        for i in range(n):
            for prev in beforeItems[i]:
                if group[prev] == group[i]:
                    item_graph[prev].append(i)
                    item_indegree[i] += 1
                else:
                    group_graph[group[prev]].append(group[i])
                    group_indegree[group[i]] += 1

        def topo_sort(graph, indegree, size):
            q = deque([i for i in range(size) if indegree[i] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nxt in graph[node]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        q.append(nxt)
            return order if len(order) == size else []

        group_order = topo_sort(group_graph, group_indegree, m)
        if not group_order:
            return []

        item_order = topo_sort(item_graph, item_indegree, n)
        if not item_order:
            return []

        items_in_group = defaultdict(list)
        for item in item_order:
            items_in_group[group[item]].append(item)

        res = []
        for g in group_order:
            res.extend(items_in_group[g])

        return res
