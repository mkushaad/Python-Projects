n = int(input("Enter n: "))
num = n ** 2
magicsquare = [[0 for x in range(n)]
                   for y in range(n)]
print("Array initially: ")
for i in range(n):
    for j in range(n):
        print(magicsquare[i][j], end=' ')
    print(" ")
i = n // 2
j = n - 1
count = 1
while count <= num:
    if i == -1 and j == n:
        j = n-2
        i = 0
    else:
        if j == n:
            j = 0

        if i < 0:
            i = n-1
    #if magicsquare[int(i)][int(j)] != 0:
    #    j -= 2
    #    i += 1
    #    continue
    if magicsquare[int(i)][int(j)] != 0:  # 2nd condition
            j = j - 2
            i = i + 1
            continue
    else:
        magicsquare[int(i)][int(j)] = count
        count = count + 1
    i -= 1
    j += 1

for i in range(n):
    for j in range(n):
        print(magicsquare[i][j],end = " ")
    print(" ")
print("Sum of each row, column and diagonal: ",n*((n**2)-1)//2) #it should be 15 not 12


