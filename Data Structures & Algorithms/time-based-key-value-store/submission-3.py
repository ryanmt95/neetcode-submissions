import bisect

class TimeMap:

    def __init__(self):
        self.keyMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyMap:
            self.keyMap[key] = list()
        self.keyMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.keyMap:
            return ""
        index = bisect.bisect_right(self.keyMap[key], timestamp, key=lambda x: x[0]) - 1

        if index == -1:
            return ""
        return self.keyMap[key][index][1] 
        
