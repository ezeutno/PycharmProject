z = ['and', 'attend', 'append']
x = input().split('*')
print(x)
count = 0
for i in range (len(z)):
    for b in range(len(x)):
        if x[b] in z[i]:
            count +=1
    if count>=len(x):
        print("0",z[i])
    count = 0