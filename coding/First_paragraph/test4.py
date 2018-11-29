#! /usr/bin python
# -*- coding:UTF-8 -*-
def main():
    with open('D:/Code/temp/coding/1.txt','w') as f:
        for m in range(10):
            f.write('This is a new:\n')
            f.write(str(m)+'\n')

main()