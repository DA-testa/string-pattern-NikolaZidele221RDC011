# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    letter = input()
    if "I" in letter:
        aa = input()
        bb = input()
        return aa.rstrip(), bb.rstrip()
    elif "F" in letter:
        file = input()
        with open("./tests/06", mode='r') as fails:
            vis = fails.read()
            dal = vis.splitlines()
            aa = dal[0]
            bb = dal[1]
            return aa.rstrip(), bb.rstrip()

    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 

    # return both lines in one return

    # this is the sample return, notice the rstrip function
    # return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    rezultats = []
    a = 0
    for i in reversed(pattern):
        a = (a * 263 + ord(i)) % 1610612741
    garums = len(pattern)
    b = [None] * (len(text) - garums + 1)
    c = text[len(text) - garums:]
    b[len(text) - garums] = 0
    for i in reversed(c):
        b[len(text) - garums] = (b[len(text) - garums] * 263 + ord(i)) % 1610612741

    i1 = 0
    d = 1
    while i1 < garums:
        d = (d * 263) % 1610612741
        i1 = i1 + 1

    i2 = len(text) - garums - 1
    while i2 >= 0:
        b[i2] = (263 * b[i2 + 1] + ord(text[i2]) - d * ord(text[i2 + garums])) % 1610612741
        i2 = i2 - 1

    i3 = 0
    while i3 < len(text) - len(pattern) + 1:
        if (a == b[i3]) and (text[i3:i3 + len(pattern)] == pattern):
            rezultats.append(i3)
        i3 = i3 + 1
    # and return an iterable variable
    return rezultats


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
