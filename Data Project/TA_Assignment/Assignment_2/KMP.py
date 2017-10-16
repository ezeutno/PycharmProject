#This program simplfied to acronym
def main():
    x = input().upper().split('-')
    for i in range(len(x)):
        print(x[i][0],end = '')
main()
