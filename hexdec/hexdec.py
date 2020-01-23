import numba

@njit
def read(file):
    b = 0
    byte = file.read(1)
    while byte: #actually EOF means that byte is "" and python automatically evaluates to false, so it will work
        if b%2 == 0:
            print(" ")
        print(str(byte))
        if b%10 == 0:
            print("\n")
with open("mem", "rb") as file:
    read(file);