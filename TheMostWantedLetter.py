#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
 Created on 2018-07-26 20:21:07
@author: cshen
'''

def checkio(text):
    count = 0
    char_list = list(text.lower())
    char_list.sort()
    for x in char_list:
        if x >= 'a' and x <= 'z':
            if char_list.count(x) > count:
                count = char_list.count(x)
                ch = x

    #replace this for solution
    return ch

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")