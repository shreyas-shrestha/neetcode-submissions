class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int):
        self.hashmap.setdefault(key, []).append((timestamp, value))
    
    def get(self, key: str, timestamp: int):
        if key not in self.hashmap:
            return ""
        my_list = self.hashmap[key]
        to_return = self.binaryfind(my_list, timestamp, 0, len(my_list)-1)
        if to_return == -1:
            return ""
        else:
            return my_list[to_return][1]
    
    def binaryfind(self, my_list, timestamp: int, L: int, R: int):
        mid = (L + R) // 2
        if R < L:
            if R < 0:
                return -1
            else:
                return R
        if my_list[mid][0] < timestamp:
            return self.binaryfind(my_list, timestamp, mid+1, R)
        elif my_list[mid][0] > timestamp:
            return self.binaryfind(my_list, timestamp, L, mid-1)
        else:
            return mid








