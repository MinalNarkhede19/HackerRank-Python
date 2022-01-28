import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if (n%2==0):
    if (20>=n>=6):
        print ("Weird");
    elif (5>n>2):
        print("Not Weird");
    elif (n>=20):
        print("Not Weird");
else:
    print("Weird");
