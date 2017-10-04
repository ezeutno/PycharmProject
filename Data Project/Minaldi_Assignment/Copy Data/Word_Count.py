def main():
    file_original = open("Original.txt", 'r')
    print(len(file_original.read().split(' ')))
    file_original.close()
main()