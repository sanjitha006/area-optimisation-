
input_file = open("output.txt", "r")
g = []
r = []
inputdim = open("input.txt", "r")
input_file.readline()
while True:
    y = input_file.readline().split()
    x = inputdim.readline().split()
    if len(y) == 0:
        break
    r.append([int(x[1]), int(x[2])])
    g.append([int(y[0][1::]),int(y[1]), int(y[2])])

overlap_count = 0
g=sorted(g)
for i in range(len(g)):
    for j in range(i + 1, len(g)):
        if(g[j][1]==g[i][1] and g[j][2]==g[i][2] and ((g[j][1]+r[j][0])==(g[i][1]+r[i][0])) and  ((g[j][2]+r[j][1])==(g[i][2]+r[i][1]))):
            overlap_count+=1
        if (g[j][1] < (g[i][1] + r[i][0]) and (g[j][1] + r[j][0]) > g[i][1] and  g[j][2] < (g[i][2] + r[i][1]) and (g[j][2] + r[j][1]) > g[i][2]):
            print(i,j)
            overlap_count += 1

print(overlap_count)

