z = ['and', 'attend', 'append']
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z']
y = []
m = []
w = []
final = []
x = input()
count = 0
for i in range(len(x)):
    if x[i].lower() in c:
        y.append(x[i])
    elif x[i] == '*':
        m.append(int(i))
    else:
        z = []
for i in range(len(z)):
    for c in range(len(y)):
        if y[c] in z[i]:
            count += 1
    if count >= len(y):
        w.append(z[i])
    count = 0
for i in range(len(w)):
    if x[0] == w[i][0] or x[0] == '*':
        final.append(w[i])
    if len(x) > 1:
        if x[1] == w[i][0]:
            final.pop(0)
print(final)