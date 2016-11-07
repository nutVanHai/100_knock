#!/usr/bin/env python
# _*_ coding: utf-8 _*_

word = "stressed"
reverse = ""
temp = ""

for c in word:
    temp = c + reverse
    reverse = temp

print(reverse)
