from random import randint
from time import time
def domath(number):
    d = pow(number, 5)
    i = pow(d, 5)
    print(d,i)
def main():
    r = time()
    i = 0
    while(i < 5000000):
        n = randint(1, 10000000)
        domath(n)
        i += 1
    ert = time()
    est = ert - r
    print(est, 's')
if __name__ == "__main__":
    main()
