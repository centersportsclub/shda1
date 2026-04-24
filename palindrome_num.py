
"""N = int(input())
A = list(map(int, input().split()))
is_palindrome = True
for i in range(N//2):
    if A[i] != A[N-1-i]:
        is_palindrome = False
        break

print("Yes" if is_palindrome else "No")"""
N = int(input())
A = list(map(int, input().split()))
#print(f"List: {A}")
#print(f"Reverse List: {A[::-1]})
if A == A[::-1]:
    print("YES")
else:
    print("NO")