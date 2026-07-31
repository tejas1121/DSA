class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def help(res):
            st = []

            for i in range(len(res)):
                if res[i] == '#':
                    if st:
                        st.pop()
                else:
                    st.append(res[i])

            return st

        res1 = help(s)
        res2 = help(t)

        if len(res1) != len(res2):
            return False

        for i in range(len(res1)):
            if res1[i] != res2[i]:
                return False

        return True