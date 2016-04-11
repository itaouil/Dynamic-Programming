"""
    Matrix-Chain Optimisation Problem.

    Input:

        p: array containing sizes of the chain matrices (p = n + 1)

    Output:

        m: table containing parenthesazation

    Reference: Introduction to Algorithms (CLRS)
"""

#Import from future module python 3.x
#print function print(obj, sep, endl)
from __future__ import print_function

def matrix_chain(p):

    #Length of the chain
    n = len(p) - 1

    #Arrays/Tables m
    m = [ [None for x in range(n)] for x in range(n) ]

    #Array/Table s
    s = [ [None for x in range(0,n-1)] for x in range(1,n) ]
    for x in range(len(s)):
        print(s[x])

    #Assign m[i,i] = 0 as stated by recurrence relation
    for x in range(n):
        m[x][x] = 0

    #Compute optimal parenthesazing
    for l in range(2, n+1):
        for i in range(1, n-l+2): #Diagonal spaces to compute
            j = i + l - 1
            m[i-1][j-1] = 9999999
            for k in range(i, j):
                q = m[i-1][k-1] + m[k][j-1] + p[i-1] * p[k] * p[j]
                if q < m[i-1][j-1]:
                    m[i-1][j-1] = q
                    s[i-1][j-2] = k

    return m,s

#Test
# m,s = matrix_chain([4,10,3,12])
#
# for x in range(len(m)):
#     print(m[x])
#
# for x in range(len(s)):
#     print(s[x])
