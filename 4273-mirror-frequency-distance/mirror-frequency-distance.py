from collections import Counter
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        f = Counter(s)
        ans = 0
        for i in range(13):
            a = chr(ord('a') + i)
            b = chr(ord('z') - i)
            ans += abs(f[a] - f[b])
        for i in range(5):
            a = chr(ord('0') + i)
            b = chr(ord('9') - i)
            ans += abs(f[a] - f[b])
        return ans