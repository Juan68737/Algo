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

#TODO: Make CS class and add all 3 functions into it, call it (not topDown) into main.py
def topDown(A: str, B: str, K: int, v: dict[str,int]):
    
    R = len(A)
    C = len(B)
    memo = {}
    res = 0
    def OPT(i,j):
        if i == 0 or j == 0:
            return 0

        if (i,j) in memo:
            return memo[(i,j)]

        if A[i-1] != B[j-1]:
            memo[(i,j)] = max(OPT(i-1,j),
                              OPT(i,j-1))
        else:
            memo[(i,j)] = max(OPT(i-1,j),
                              OPT(i,j-1),
                              v[A[i-1]] + OPT(i-1,j-1))
        return memo[(i,j)]
    res = OPT(R,C)

    print(f"The common subsequence for {A} and {B} is: {res}")


def bottomUp(A: str, B: str, K: int, v: dict[str,int]):
    R = len(A)
    C = len(B)
    res = 0
    M = [[0] * (C+1) for _ in range(R+1)]
    for i in range(1,R+1):
        for j in range(1,C+1):

            if A[i-1] != B[j-1]:
                M[i][j] = max(M[i-1][j], M[i][j-1])
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1], v[A[i-1]] + M[i-1][j-1])
    res = M[R][C]

    bt = backTrack(A, B, M,v)
    print(f"The common subsequence for {A} and {B} is: {res} with the backtrack results of {bt}")


def backTrack(A:str, B:str, M, v):
    i = len(A)
    j = len(B)
    res = []

    while i > 0 and j > 0:
        if A[i-1] == B[j-1] and M[i][j] == v[A[i-1]] + M[i-1][j-1]:

            #or B[j-1], doesnt really matter
            res.append(A[i-1])
            i -= 1
            j -= 1
        #the order of elif and else doesnt matter
        elif M[i][j] == M[i][j-1]:
            i -= 1
        else:
            j -= 1
    return res[::-1]

d = {
    'a': 3,
    'b': 4,
    'c': 10,
    'd': 1
}
bottomUp("aab", "ab",2, d)




