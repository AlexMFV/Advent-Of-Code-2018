## Day 3

import re
from random import *
from graphics import *
import time
import numpy as np

def separateLine(line):
    values = re.findall(r"['\w']+", line)
    list = []
    
    for i in range(len(values)):
        if i == len(values)-1:
            list.append(values[i].split("x")[0])
            list.append(values[i].split("x")[1])
        else:
            list.append(values[i])
    return list
    
def main():
    ##Part 1
    
    #win = GraphWin("AoC Day 3 - Visual", 500, 500)
    start = time.perf_counter()
    file = open("../input.txt", "r")
    values = []
    
    for line in file:
        values.append(separateLine(line))
        
    values2 = values.copy()
        
    total = 0
    fabric = np.zeros((1000, 1000))
        
    for value in values:
        x = int(value[1])
        y = int(value[2])
        width = int(value[3])
        height = int(value[4])
        
        for i in range(height):
            for j in range(width):
                fabric[y+i][x+j] += 1
                
    for y in range(len(fabric)):
        for x in range(len(fabric[y])):
            if fabric[y][x] >= 2:
                total += 1
            
    ##Part 2
    
    isAlone = False
    id = 0
    
    for value in values2:
        aux = 0
        x = int(value[1])
        y = int(value[2])
        width = int(value[3])
        height = int(value[4])
        
        area = width * height
        
        for i in range(height):
            for j in range(width):
                if fabric[y+i][x+j] != 1:
                    break
                else:
                    aux += 1
                    
            if fabric[y+i][x+j] != 1:
                break
                
        if aux == area:
            id = value[0]
            break
                
    end = time.perf_counter() - start
    print("Time to complete:", end)
    print("Part 1:", total)
    print("Part 2:", id)


main()