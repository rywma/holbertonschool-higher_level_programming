#!/usr/bin/python3
for i in range(25, -1, -1):
    if (25 - i) % 2 == 0:
        print("{}".format(chr(ord('z') - (25 - i))), end="")
    else:
        print("{}".format(chr(ord('Z') - (25 - i))), end="")
