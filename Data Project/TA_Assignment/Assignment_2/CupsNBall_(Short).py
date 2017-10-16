x=1
y=0
z=0
moves=input().upper()
for i in moves:
    if i == 'A':


    elif i == 'B':
        y ^= z
    elif i =='C':
        z ^= x
    print(x,y,z)