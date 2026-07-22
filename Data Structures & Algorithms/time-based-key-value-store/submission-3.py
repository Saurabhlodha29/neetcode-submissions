class TimeMap:

    def __init__(self):
        self.hashset = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashset:
            self.hashset[key].append([timestamp,value])
        else:
            self.hashset[key] = [[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashset:
            targetlist = self.hashset[key]
            left,right = 0, len(targetlist)-1
            while left <= right:
                mid = (left+right)//2
                if targetlist[mid][0] < timestamp:
                    left = mid+1
                elif targetlist[mid][0] > timestamp:
                    right = mid-1
                elif targetlist[mid][0] == timestamp:
                    return targetlist[mid][1]

            if right >= 0:
                return targetlist[right][1]
            return ""

        return ""
