def long_repeat(line):
    count = 0
    c = 0
    tmp = []
    for idx in range(len(line)):
        tmp.append(line[idx])
        c = len(tmp)
        if idx + 1 < len(line) and line[idx+1] is not line[idx]:
            tmp = []
        if c > count:
            count = c
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat('aa') == 2, "Empty"
    print('"Run" is good. How is "Check"?')