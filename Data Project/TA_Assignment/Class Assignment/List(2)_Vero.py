word_list = ["and", "append", "attend"]
ans = "a*t"
temp =""
rite = False
list = []
count = 0

for i in word_list:
    idx = 0
    idx1 = 0
    while idx1<len(i) and idx<len(ans):
        if ans[0] == "*" and len(ans)==1:
            list.append(i)
            break
        print(idx1, len(i)-1, ans[idx], i[idx1])
        if idx1!=len(i)-1:
            if ans[idx]=="*":
                if idx<len(ans)-1:
                    idx+=1
                temp = "*"
                print(1)
                # continue
            if ans[idx] != i[idx1] and temp =="*":
                rite = True
                if idx1<len(i)-1:
                    idx1+=1
                print(3)
                # continue
            elif ans[idx] != i[idx1]:
                rite = False
                if idx1<len(i)-1:
                    idx1+=1
                print(3)
                break
            elif ans[idx] == i[idx1]:
                rite = True
                temp = ans[idx]
                if idx < len(ans) - 1:
                    idx+=1
                if idx1<len(i)-1:
                    idx1+=1
                print(2)
                # continue
            else:
                if idx<len(ans)-1:
                    idx-=1
                    print("masuk")
                else:
                    rite = False
                    print(4)
                    break
        else:
            if ans[idx] == "*":
                list.append(i)
                break
            elif ans[idx]!="*":
                if ans[idx]!=i[idx1]:
                    rite = False
                    print(ans[idx])
                    break
                else:
                    rite = True
                    if idx1<len(i)-1:
                        idx1+=1
                    print(idx1, len(i))
                    if idx1==len(i)-1:
                        list.append(i)
                    break
            else:
                rite = True
                if idx1<len(ans)-1:
                    idx1+=1
                if idx1==len(i):
                    list.append(i)
                break

    print("DONE", rite, idx1, len(i))
print(list)
