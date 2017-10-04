def main():
    DepecheMode = open('DepecheMode.pgm', 'br')
    DepecheMode2 = open('DepecheMode2.pgm','bw')
    x = list(DepecheMode.read())
    for i in range (14,len(x)):
        x[i] = 255 - x[i]
    DepecheMode2.write(bytes(x))
    DepecheMode2.close()
    DepecheMode.close()
main()
