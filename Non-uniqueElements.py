#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
 Created on 2018-07-27 12:27:04
@author: cshen
'''
def checkio(data):
    tmp = data.copy()
    for x in data:
        if tmp.count(x) == 1:
            tmp.remove(x)
    return tmp

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")