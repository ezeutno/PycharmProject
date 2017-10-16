#This program print how many distinct number of modulo 42
def main():
    y = []
    m = 42
    for i in range(10):
        x = int(input())
        y.append(x%m)
    print(len(set(y)))
main()