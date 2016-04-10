"""
    Given a rod, find the optimal cost
    obtained by slicing/cutting the rod.

    r = max(pi, n - i)

    where:

        1 =< i <= K (K in this case is n, i.e. no cut at all)

    input:

        array p containing the revenue for each i
        rod's length (n)

    output:

        maximum revenue obtainable for n

    Reference: CLRS (Introduction to Algorithms)
"""

#Import python 3.x's print function
from __future__ import print_function


""" Top-Down Approach with memoization (RECURSIVE) """
def cut_rod_memoization(p,n):

    #Create array r for memoization
    r = [None] * (n + 1)

    #Assign sentinel values to array r
    for x in range(n+1):
        r[x] = -99999

    #Call computation procedure
    return cut_rod_memoization_aux(p,n,r)

#Compute recursively with memoization
def cut_rod_memoization_aux(p,n,r):

    #Recall already computerd sub-problem
    if r[n] >= 0:
        return r[n]

    #Base case
    elif n == 0:
        q = 0

    else:
        #Sentinel value
        q = -99999

        #Compute max recursively
        for i in range(1, n+1):
            q = max(q, p[i-1] + cut_rod_memoization_aux(p,n-i,r))

    r[n] = q
    return q

# #Test for Top-Bottom
# p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# n = 9
# print("Top-Down: " + str(cut_rod_memoization(p,n)) + "\n")


""" Bottom-Up Approach with memoization """
def bottom_up_cut_rod(p,n):

    #Create array r for memoization
    r = [None] * (n + 1)
    r[0] = 0

    #Compute optimal solution
    for j in range(1, n+1):
        #Sentinel value
        q = -9999
        for i in range(1, j+1):
            q = max(q, p[i-1] + r[j-i])

        #Assign sub-problem to its array position
        r[j] = q

    return r[n]

# #Test for Bottom-Up
# p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# n = 5
# print("Bottom-Up: " + str(bottom_up_cut_rod(p,n)))
