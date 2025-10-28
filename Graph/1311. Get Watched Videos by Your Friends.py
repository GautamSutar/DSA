from collections import deque, Counter
from typing import List


class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        id: int,
        level: int,
    ) -> List[str]:
        visited = set([id])
        q = deque([id])
        current_level = 0

        while q and current_level < level:
            for _ in range(len(q)):
                person = q.popleft()
                for f in friends[person]:
                    if f not in visited:
                        visited.add(f)
                        q.append(f)
            current_level += 1

        videos = []
        for person in q:
            videos.extend(watchedVideos[person])

        count = Counter(videos)
        result = sorted(count.keys(), key=lambda x: (count[x], x))
        return result
