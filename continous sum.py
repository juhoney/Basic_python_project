n = int(input())
li = list(map(int, input().split()))
sum = [li[0]]
for i in range(n - 1):
    sum.append(max(sum[i] + li[i + 1], li[i + 1]))
print(max(sum))