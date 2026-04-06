'''
OPT(i,j) = {
    0 if i == 0
    0 if j == 0
    max(OPT(i-1,j), OPT(i,j-1)) if A[i-1] != B[j-1]
    max(OPT(i-1,j), 
        OPT(i,j-1), 
        v[A[i-1]] + OPT(i-1,j-1)) otherwise
}
'''

class CS:
    def __init__(self, A: str, B: str, K: int, v: dict[str, int]):
        self.A = A
        self.B = B
        self.K = K
        self.v = v
        self.R = len(A)
        self.C = len(B)

    def topDown(self) -> int:
        memo: dict[tuple[int, int], int] = {}

        def OPT(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if self.A[i - 1] != self.B[j - 1]:
                memo[(i, j)] = max(OPT(i - 1, j), OPT(i, j - 1))
            else:
                memo[(i, j)] = max(
                    OPT(i - 1, j),
                    OPT(i, j - 1),
                    self.v[self.A[i - 1]] + OPT(i - 1, j - 1),
                )
            return memo[(i, j)]

        return OPT(self.R, self.C)

    def bottomUp(self) -> tuple[int, str]:
        M = [[0] * (self.C + 1) for _ in range(self.R + 1)]
        for i in range(1, self.R + 1):
            for j in range(1, self.C + 1):
                if self.A[i - 1] != self.B[j - 1]:
                    M[i][j] = max(M[i - 1][j], M[i][j - 1])
                else:
                    M[i][j] = max(
                        M[i - 1][j],
                        M[i][j - 1],
                        self.v[self.A[i - 1]] + M[i - 1][j - 1],
                    )

        max_value = M[self.R][self.C]
        subsequence = self.backTrack(M)
        return max_value, subsequence

    def backTrack(self, M: list[list[int]]) -> str:
        i = self.R
        j = self.C
        res: list[str] = []

        while i > 0 and j > 0:
            if (
                self.A[i - 1] == self.B[j - 1]
                and M[i][j] == self.v[self.A[i - 1]] + M[i - 1][j - 1]
            ):
                res.append(self.A[i - 1])
                i -= 1
                j -= 1
            elif M[i][j] == M[i - 1][j]:
                i -= 1
            else:
                j -= 1

        return "".join(reversed(res))




