input = input()
location = [0, int(input[1])]
move = [[2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2]]
print(ord(input[0])-ord('a')+1)
if input[0]=='a':
    location[0]=1
elif input[0] =='b':
    location[0] = 2
elif input[0]=='c':
    location[0]=3
elif input[0]=='d':
    location[0]=4
elif input[0]=='e':
    location[0]=5
elif input[0]=='f':
    location[0]=6
elif input[0]=='g':
    location[0]=7
elif input[0]=='h':
    location[0]=8

cnt = 0
# print(location[0]+move[0][0])#가 1보다 크고 8보다 작음
# print(location[1]+move[0][1])
for m in move:
    if location[0]+m[0]>=1 and location[0]+m[0]<=8 and location[1]+m[1]>=1 and location[1]+m[1]<=8:
        cnt+=1
print(cnt)