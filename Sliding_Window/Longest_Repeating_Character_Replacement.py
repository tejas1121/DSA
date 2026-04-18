from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        maxFreq = 0
        i = 0
        res = 0

        for j in range(len(s)):
            freqs[s[j]] += 1
            maxFreq = max(maxFreq, freqs[s[j]])

            if (j - i + 1) - maxFreq > k:
                freqs[s[i]] -= 1
                i += 1

            res = max(res, j - i + 1)

        return res