class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int):
        self.hashmap.setdefault(key, []).append((timestamp, value))
    
    def get(self, key: str, timestamp: int):
        if key not in self.hashmap:
            return ""
        my_list = self.hashmap[key]
        for time, value in reversed(my_list):
            if time <= timestamp:
                return value
        return ""
