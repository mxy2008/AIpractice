"""
Author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput
from collections import deque
#Problem21_1
for line in fileinput.input():

    try:
        arrangement = [int(x.strip()) for x in line.split(',')]
        length=len(arrangement)
        #print arrangement

    except:
        sys.exit('invalid input')

    # more than 3 numbers in the same line
    #if len(arrangement) > 3:
    #    sys.exit('invalid input')

    # initial state not valid
    for k in range(0, length-1):
        if arrangement[k] not in [0, 1]:
            sys.exit('invalid input')
    if arrangement[length-1]>=length-1:
        sys.exit('invalid input')

    # determine whether the state is a goal state
    count=0
    for k in range(0, length-1):
        #print arrangement[k]
        if arrangement[k] is 0:
            count+=1
        else:
            break
    if count==length-1:
        sys.exit('')

#Problem21_2  BFS
    frontier=deque([arrangement])
    visited=[arrangement]
    path={}
    path[tuple(arrangement)]=''
    action='LRS'

    while len(frontier)!=0:
        #print len(frontier)
        node=frontier.popleft()
        #print 'This is node: '
        #print node
        #print 'path: '+path[tuple(node)]
        room=node[length-1]
        
        #find goal state
        count=0
        for k in range(0, length-1):
            if node[k] is 0:
                count+=1
            else:
                break
        if count==length-1:
            print path[tuple(node)]
            sys.exit()
        
        #run BFS
        step=path[tuple(node)]

        for act in action:
            #print act
            if act=='L':
                temp=list(node)
                temp[length-1]=room-1
                if temp in visited:
                    continue
                elif temp[length-1]>=0:
                    frontier.append(temp)
                    visited.append(temp)
                    path[tuple(temp)]=step+act

            elif act=='R':
                temp=list(node)
                temp[length-1]=room+1
                if temp in visited:
                    continue
                elif temp[length-1]<=length-1:
                    frontier.append(temp)
                    visited.append(temp)
                    path[tuple(temp)]=step+act

            elif act=='S':
                temp=list(node)
                temp[room]=0
                if temp in visited:
                    continue
                else:
                    frontier.append(temp)
                    visited.append(temp)
                    path[tuple(temp)]=step+act

            #print frontier











