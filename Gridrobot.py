
def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
    x = startPos[0]
    y = startPos[1]
    i = 0
    l = []
    d = {'L': 1, 'R': -1, 'U': -1, 'D': -1}
    while bool(s):
        j = 0

        while j < len(s):
            if s[j] in ('U', 'D') and x + d[s[j]] != -1 and x + d[s[j]] != n:
                x += d[s[j]]

            elif s[j] in ('L', 'R') and y + d[s[j]] != -1 and y + d[s[j]] != n:
                y += d[s[j]]
            else:
                # edit list
                break
            j += 1

        i += 1
        s = s[i:]
        x = startPos[0]
        y = startPos[1]
    return l


tl = executeInstructions(33, 3, [0, 1], "RRDDLU")
print(tl)
