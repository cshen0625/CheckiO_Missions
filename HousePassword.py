#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
 Created on 2018-07-26 18:20:10
@author: cshen
'''

def checkio(data):
 
    length = (len(data) >= 10)
    isdigit = any(x.isdigit() for x in data)
    isupper = any(x.isupper() for x in data)
    islower = any(x.islower() for x in data)
    if length and isdigit and isupper and islower:
        return True
    else:
        return False
#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")