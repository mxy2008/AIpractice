"""
Author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput
from collections import deque

def problem23_3():
    input = sys.stdin.read()
    text = input.splitlines()
    row = len(text)
    column = len(text[0].split(','))
    lines = []
    for j in range(0,row):
        li = [int(x.strip()) for x in text[j].split(', ')]
        lines.append(li)

    #vacumm location not valid
    if len(lines[row-1]) == 2:
        if (int(lines[row-1][0]) not in range(0,row-1)) or (int(lines[row-1][1]) not in range(0,column)):
            return 'invalid input: last line'
    else:
        return 'invalid input: last line'

    for i in range(0,row-1):
        # Initial state not valid
        for k in range(0, column):
            if lines[i][k] not in [0,1]:
                return 'invalid input'
                

    # Whether the state is a goal state
    count = 0
    for i in range(0, row-1):
        for j in range(0, column):
            if (lines[i][j] is 0):
                count += 1
            else:
                break
    # Check if they are all zeros
    if count == (row-1)*column:
        return ''



    #Problem23_2 DFS
    frontier = [lines]
    visited = []
    path = {}
    path[id(lines)] = ''
    action = 'SDRUL'

    while len(frontier) != 0:
        node = frontier.pop()
        room = list(node[row-1])
        visited.append(node)
        
        #check goal state
        count = 0
        for i in range(0, row-1):
            for j in range(0, column):
                if (node[i][j] is 0):
                    count += 1
                else:
                    break
        # Check if they are all zeros
        if count == (row-1)*column:
            return path[id(node)]

        #run DFS
        step = path[id(node)]


        for act in action:
            temp = []
            for item in node:
                temp.append(list(item))
            
            if act == 'S':
                temp[room[0]][room[1]] = 0
                if temp in visited:
                    continue
                else:
                    frontier.append(temp)
                    path[id(temp)]=step+act


            elif act == 'D':
                temp[row-1][0] = room[0]+1
                if temp in visited:
                    continue
                elif temp[row-1][0] <= row-2:
                    frontier.append(temp)
                    path[id(temp)] = step+act

            elif act == 'R':
                temp[row-1][1] = (room[1])+1
                if temp in visited:
                    continue
                elif temp[row-1][1] <= column-1:
                    frontier.append(temp)
                    path[id(temp)] = step+act

            elif act == 'U':
                temp[row-1][0] = room[0]-1
                if temp in visited:
                    continue
                elif temp[row-1][0] >= 0:
                    frontier.append(temp)
                    path[id(temp)] = step+act


            elif act == 'L':
                temp[row-1][1] = (room[1])-1
                if temp in visited:
                    continue
                elif temp[row-1][1] >= 0:
                    frontier.append(temp)
                    path[id(temp)] = step+act


print(problem23_3())