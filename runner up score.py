n = int(input())
arr = list(map(int, input().split()))
maximum=max(arr)
for k in range(n):
    for i in arr:
        if i ==maximum:
            arr.remove(i)
runnerup= max(arr)
print(runnerup)
