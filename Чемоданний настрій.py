n = int(input())
a = []
for i in range(n):
    f = list(map(int, input().split()))
    f.sort()
    a.append(f)
a.sort(key = lambda x: (x[0], x[1], x[2])) 
dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i][0] >= a[j][0] and a[i][1] >= a[j][1] and a[i][2] >= a[j][2] and \
           a[i][0] - a[j][0] <= min(a[i][1], a[j][1]) and \
           a[i][1] - a[j][1] <= min(a[i][0], a[j][0]) and \
           a[i][0] - a[j][0] <= min(a[i][2], a[j][2]) and \
           a[i][2] - a[j][2] <= min(a[i][0], a[j][0]) and \
           a[i][1] - a[j][1] <= min(a[i][2], a[j][2]) and \
           a[i][2] - a[j][2] <= min(a[i][1], a[j][1]):
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
