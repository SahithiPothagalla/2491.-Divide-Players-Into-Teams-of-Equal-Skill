class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        t, c, r = 2 * sum(skill) // len(skill), Counter(skill), 0
        for x, y in c.items():
            if y != c[t - x]: return -1
            r += x * (t - x) * y
        return r // 2
