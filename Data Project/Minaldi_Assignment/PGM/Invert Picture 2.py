def main():
    SteveJobs = open('stevejobs.pgm', 'br')
    SteveJobs2 = open('stevejobs2.pgm','bw')
    x = list(SteveJobs.read())
    for i in range (14,len(x)):
        x[i] = 255 - x[i]
    SteveJobs2.write(bytes(x))
    SteveJobs2.close()
    SteveJobs.close()
main()
