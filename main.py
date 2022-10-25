f = open('input.txt')
prove = 1

rA, cA = map(int, f.readline().split())
MA = [[0 for i in range(rA)] for j in range(cA)]
mA = list(map(int, f.readline().split()))
k = 0
for i in range(rA):
    for j in range(cA):
        MA[i][j] += float(mA[k])
        k += 1
# print(MA)

rB, cB = map(int, f.readline().split())
MB = [[0 for i in range(rB)] for j in range(cB)]
mB = list(map(int, f.readline().split()))
k = 0
for i in range(rB):
    for j in range(cB):
        MB[i][j] += float(mB[k])
        k += 1
# print(MB)

rC, cC = map(int, f.readline().split())
MC = [[0 for i in range(rC)] for j in range(cC)]
mC = list(map(int, f.readline().split()))
k = 0
for i in range(rC):
    for j in range(cC):
        MC[j][i] += float(mC[k])  # транспонирование
        k += 1
# print(MC)

n = float(f.readline())

if rB == rC and cB == cC:
    for i in range(rB):
        for j in range(cB):
            MB[i][j] *= n
            MB[i][j] += MC[i][j]
else:
    prove = 0
print(MB)

MBt=[[0 for i in range (rB)] for j in range (cB)]
for i in range (rB):
    for j in range (cB):
        MBt[j][i]=MB[i][j]
print(MBt)
if cA == rB:
    MR = [[0 for a in range(cB) for b in range(rA)]]
    for i in range(rA):
        for j in range(cA):
            for k in range(cB):
                MR[i][i] = MA[i][j] * MBt[j][k]
else:
    prove = 0

    # for i in range()
