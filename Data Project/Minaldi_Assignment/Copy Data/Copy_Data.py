def main():
    file_original = open("Original.txt", 'r')
    file_fake = open("Fake.txt", 'a')
    file_fake.write(file_original.read(),'\n')
    file_original.close()
    file_fake.close()
main()
