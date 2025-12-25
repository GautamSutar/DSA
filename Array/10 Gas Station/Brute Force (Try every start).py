class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for start in range(n):
            fuel = 0
            completed = True

            for k in range(n):
                i = (start + k) % n
                fuel += gas[i]
                fuel -= cost[i]
                if fuel < 0:
                    completed = False
                    break

            if completed:
                return start

        return -1



# ⏱ Complexity

# Time: O(n²) ❌
# Space: O(1)

# ✔️ Correct
# ❌ TLE for large n