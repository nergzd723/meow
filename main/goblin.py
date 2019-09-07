from random import randint
from time import time
def domath(number):
    d = pow(number, 20)
    i = pow(d, 20)
def main():
    r = time()
    i = 0
    while(i < 50000000):
        n = randint(1, 10000000)
        domath(n)
        i += 1
        print(i)
    ert = time()
    est = ert - r
    print(est, 's')
if __name__ == "__main__":
    main()
