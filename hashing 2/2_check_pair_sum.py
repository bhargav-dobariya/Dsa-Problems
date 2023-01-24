# Given an Array of integers B, and a target sum A.
# Check if there exists a pair (i,j) such that Bi + Bj = A and i!=j.
# Return an integer value 1 if there exists such pair, else return 0.   

#Approach:- first create hashset after check and array value if exist then return 1 or 0

A = 8   
B = [3, 5, 1, 2, 1, 2]
  
def solve(A, B):
    ans = set()
    for i in range (len(B)):                
        if A - B[i] in ans:
            return 1
        ans.add(B[i])
    return 0

print(solve(A,B))
