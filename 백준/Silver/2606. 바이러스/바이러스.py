import sys
input = sys.stdin.readline

computers = int(input())
linked = int(input())
link = []
links = []
answer = [1]
for _ in range(linked):
    link = list(map(int,input().split()))
    links += [link]
a = 1
n = len(links)
for i in range(n):
    for i in links:
        if i[0] in answer:
            answer.append(i[1])
            links.remove(i)

            break
        elif i[1] in answer:
            answer.append(i[0])
            links.remove(i)
            break
        else:
            continue
answer = list(set(answer))
print(len(answer)-1)