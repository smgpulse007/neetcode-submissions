class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ct = Counter(t)
        cs = Counter(s)
        return ct==cs