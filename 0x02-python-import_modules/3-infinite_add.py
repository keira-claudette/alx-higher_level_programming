#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    summation = 0
    for i in range(1, len(sys.argv)):
        summation += int(sys.argv[i])
    print("{:d}".format(summation))
