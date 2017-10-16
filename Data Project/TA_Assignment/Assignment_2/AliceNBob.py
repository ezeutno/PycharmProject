#input == remaining stone odd = alice even = bob
def main():
    w = int(input ())
    if w%2 != 0 :
        print('Alice')
    else :
        print('Bob')
main()