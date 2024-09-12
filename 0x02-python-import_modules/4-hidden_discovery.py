#!/usr/bin/python3
import hidden_4

o = 0

if __name__ == '__main__':
    mylist = dir(hidden_4)
    newlist = sorted(mylist)
    while o < len(newlist):
        if newlist[o][0] != '_':
            print(newlist[o])
        o += 1
