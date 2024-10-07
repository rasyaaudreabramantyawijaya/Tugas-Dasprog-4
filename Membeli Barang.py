N, M = map(int,input().split())
P = list(map(int,input().split()))
C = list(map(int,input().split()))
harga = 0
beli = 0

for i in P:
    if i > 0:
        harga += i
if harga == 0:
    harga = max(P)

for j in C:
    if j < 0:
        beli += j
if beli == 0:
    harga = min(P)

total = beli - harga
print(total)