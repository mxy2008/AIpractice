"""
Author:
Yijun Zhang yiz160@ucsd.edu
Xinyi Ma   xim002@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""
import sys
import fileinput

count = 0
for line in fileinput.input():
    count += 1

# more than 1 line
if count > 1:
    sys.exit('invalid input')
    
for line in fileinput.input():

    try:
        arrangement = [int(x.strip()) for x in line.split(',')]

    except:
        sys.exit('invalid input')

    # more than 3 numbers in the same line
    if len(arrangement) > 3:
        sys.exit('invalid input')

    # initial state not valid
    for k in range(0, 3):
        if arrangement[k] not in [0, 1]:
            sys.exit('invalid input')

    # determine whether the state is a goal state
    if arrangement[0] is 0 and arrangement[1] is 0:
        print 'True'
    else:
        print 'False'

    sys.exit()
