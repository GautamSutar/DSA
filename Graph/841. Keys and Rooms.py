from collections import deque
from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        q = deque([0])
        while q:
            room = q.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)

        return len(visited) == len(rooms)
