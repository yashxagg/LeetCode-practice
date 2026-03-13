import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_reduce(time_limit):
            total_reduction = 0
            for w in workerTimes:
                x = int((-1+math.sqrt(1+(8*time_limit)//w))//2)
                total_reduction += x
                if total_reduction >= mountainHeight:
                    return True
            return total_reduction >= mountainHeight
        
        low = 1
        max_w = max(workerTimes)
        high = max_w * mountainHeight * (mountainHeight+1)//2

        ans = high
        while low <= high:
            mid = (low+high)//2
            if can_reduce(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
        