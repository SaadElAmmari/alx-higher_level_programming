#!/usr/bin/python3
from sys import argv

d, iax = 1, 0

if __name__ == '__main__':
    while d < len(argv):
        iax += int(argv[d])
        d += 1
    print(iax)
