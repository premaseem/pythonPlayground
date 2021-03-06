# Given two sorted arrays, A and B, determine their intersection. What elements are common to A and B?
A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(set(A).intersection(B))

# brute force
s=set()
for e in A:
    if e in B:
        s.add(e)
print(s)

# Set conversion
s=set()
s1 = set(A)
for e in B:
    if e in s1:
        s.add(e)
print(s)

# double pointer logic

def inter(A,B):
    s=set()
    i=j=0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            s.add(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return s

print(inter(A,B))
