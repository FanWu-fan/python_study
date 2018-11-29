#! usr/bin python
# -*- coding:UTF-8 -*-
# x = 'eller rabbit'
# if x == 'roger':
#     print('1')
# elif x == 'bugs':
#     print('2')
# else:
#     print('3')
#-----------------------------------------------------
choice = 'ss'
branch = {'spam':1.25,
        'ham':1.99,
        'eggs':0.99}
print(branch.get(choice,'bad choice'))