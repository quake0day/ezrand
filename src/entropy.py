import math

FILENAME = "../data/w001day1-raw.bin"

def entropy(data):
    if not data:
        return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x))) / len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x,2)
    return entropy


def get_data(FILENAME):
    data = open(FILENAME,'r').read()
    print entropy(data)

#get_data("./1.txt")
get_data(FILENAME)

#print entropy("asdfasdfa")
