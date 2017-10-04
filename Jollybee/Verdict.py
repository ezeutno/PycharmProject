x = int(input())
data = []
print_data = []
for i in range(0,x):
    for w in range(0,6):
        data.insert(w,input())
    if data[1] >= data[0]:
        y = "TIME LIMIT EXCEEDED / TIMELIMIT"
    elif data[3] >= data[2]:
        y = "MEMORY LIMIT EXCEEDED"
    elif data[5] != data[4]:
        y = "WRONG-ANSWER"
    else:
        y = "ACCEPTED / CORRECT"
    print_data.append("Kasus #"+str(i+1)+" "+y)
for i in range(x):
    print(print_data[i])