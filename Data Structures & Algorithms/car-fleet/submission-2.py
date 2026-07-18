class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []

        combined = list(zip(position, speed))
        combined.sort()
        position[:], speed[:] = zip(*combined)

        times.append((target-position[-1])//speed[-1])

        if len(position) == 1:
            return 1

        for i in range(len(position)-2,-1,-1):
            time = (target-position[i])/speed[i]

            if time > times[-1]:
                times.append(time)

        return len(times)