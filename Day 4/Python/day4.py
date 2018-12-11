import re
import numpy as np

def main():
    #First get the ID of the guard that sleeps the most
    #Get the minute he sleeps the most
    #Multiply those values and TADA
    
    file = open("../input.txt", "r")
    raw_data = []
    guards = []
    shifts = []
    
    #Fill with raw data
    for line in file:
        raw_data.append(re.findall(r"['\w']+", line))
    raw_data.sort()
      
    #Work the raw data to values
    for item in raw_data:
        list = []
        
        type = item[5]
        if type == "Guard":
            id = item[6]
        else:
            id = '-1'
        
        list.append(id)
        list.append(type)
        list.append(item[0])
        list.append(item[1])
        list.append(item[2])
        list.append(item[3])
        list.append(item[4])
        guards.append(list)
    
    #Add initial shifts
    exists = False
    for guard in guards:
        list = []
        for i in range(len(shifts)):
            if guard[0] != '-1':
                if shifts[i].count(guard[0]) != 0:
                    exists = True
                    
        if guard[0] != '-1' and not exists:
            list.append(guard[0]) #id
            list.append(np.zeros((60)))
            shifts.append(list)
        else:
            exists = False
    
    #Fill shifts with minutes asleep
    for shift in shifts:
        start = -1
        end = -1
        id = shift[0]
        for guard in guards:
            type = guard[1]
            if guard[0] != '-1':
                auxID = guard[0]
            
            if id == auxID:
                if type == "falls":
                    start = int(guard[6])
                elif type == "wakes":
                    end = int(guard[6])
                    
            if start != -1 and end != -1:
                for i in range(start, end):
                    shift[1][i] += 1
                start = -1
                end = -1
                
    asleep = []     
    for shift in shifts:
        list = []
        total = 0
        for i in range(len(shift[1])):
            total += shift[1][i]
        list.append(shift[0])
        list.append(total)
        asleep.append(list)
        
    sleepiestID = -1
    aux = 0
    for sleep in asleep:
        if sleep[1] >= aux:
            sleepiestID = sleep[0]
            aux = sleep[1]
            
    goldenMin = 0
    aux = 0
    for shift in shifts:
        if shift[0] == sleepiestID:
            for i in range(len(shift[1])):
                if shift[1][i] > aux:
                    aux = shift[1][i]
                    goldenMin = i
                    
    list = ['', 0]
    aux = 1
    for shift in shifts:
        for i in range(len(shift[1])):
            if shift[1][i] > list[1]:
                list = [shift[0], i]
    
    print("Part 1:", int(sleepiestID) * int(goldenMin))
    print("Part 2:", int(list[0]) * (int(list[1])+1))
    
    ##VERY BAD CODING RIGHT HERE, BUT IT'S DONE :P
    
main()