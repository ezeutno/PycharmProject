z = ['and', 'attend', 'append','apair']
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z']
y = []
test = 0
x = input()
count = 0
for i in range(len(x)):
    if x[i].lower() in c:
        for a in range(len(z[i])):
            if x[i] == z[i][a]:
                y.append(z[i])
                print(y)
print(y)
