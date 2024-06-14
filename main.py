import math

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [
            [-1 for _ in range(len(stations) + 1)]
            for _ in range(len(stations) + 1)
        ]
        for allow_station in range(len(stations) + 1):
            for exactly_used_stops in range(len(stations) + 1):
                if exactly_used_stops == 0:
                    dp[allow_station][exactly_used_stops] = startFuel
                elif allow_station == 0:
                    dp[allow_station][exactly_used_stops] = -math.inf
                elif exactly_used_stops > allow_station:
                    dp[allow_station][exactly_used_stops] = -math.inf
                elif stations[allow_station - 1][0] <= dp[allow_station][exactly_used_stops - 1]:
                    dp[allow_station][exactly_used_stops] = max(
                        dp[allow_station - 1][exactly_used_stops],
                        dp[allow_station - 1][exactly_used_stops - 1] + stations[allow_station - 1][1]
                    )
                else:
                    dp[allow_station][exactly_used_stops] = max(
                        dp[allow_station - 1][exactly_used_stops],
                        dp[allow_station][exactly_used_stops - 1]
                    )
        for stops, reachable in enumerate(dp[-1]):
            if reachable >= target:
                return stops
        return -1
