class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:

            skip = 0

            # Find next valid character in s
            while i >= 0:
                if s[i] == '#':
                    skip += 1
                    i -= 1
                elif skip > 0:
                    skip -= 1
                    i -= 1
                else:
                    break

            skip = 0

            # Find next valid character in t
            while j >= 0:
                if t[j] == '#':
                    skip += 1
                    j -= 1
                elif skip > 0:
                    skip -= 1
                    j -= 1
                else:
                    break

            # Both point to valid characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False

            # One string finished before the other
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True