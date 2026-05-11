from collections import deque

class TimeMap:

    def __init__(self):
        self.map = defaultdict(deque)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].appendleft((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        for key, time in self.map[key]:
            if time <= timestamp:
                return key
        return ""