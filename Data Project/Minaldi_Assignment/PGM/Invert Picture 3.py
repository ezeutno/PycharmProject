def main():
    RobertSmith = open('robertsmith.pgm', 'br')
    RobertSmith2 = open('robertsmith2.pgm','bw')
    x = list(RobertSmith.read())
    for i in range (14,len(x)):
        x[i] = 255 - x[i]
    RobertSmith2.write(bytes(x))
    RobertSmith2.close()
    RobertSmith.close()
main()
