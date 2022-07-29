import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for i in range(T) :

    a, b, c = list(map(int, input().split()))

    if a == b :
        d = c

    elif a == c : 
        d = b

    else :
        d = a
    
    print(f'#{i+1} {d}')