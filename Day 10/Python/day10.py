import re
from graphics import *

def main():
    file = open("../input.txt", "r")
    raw_data = []
    values = []
    circles = []
    
    win = GraphWin("teste", 1000, 1000)
    
    for line in file:
        raw_data.append(re.findall(r"[-\w]+", line))
    
    for item in raw_data:
        list = []
        list.append(int(item[1]))
        list.append(int(item[2]))
        list.append(int(item[4]))
        list.append(int(item[5]))
        values.append(list)
    
    #IDK but "item[0] < 0 and item[0] > 1000" is not working
    # for item in values:
    #     for i in range(2000):
    #         if item[0] > 1000:
    #             item[0] += int(item[2])
    #         if item[0] < 0:
    #             item[0] += int(item[2])
    #         
    #         if item[1] > 1000:
    #             item[1] += int(item[3])
    #         if item[1] < 0:
    #             item[1] += int(item[3])
            
    for item in values:
        p = Point(item[0], item[1])
        p.setFill("red")
        p.draw(win)
        circles.append(p)

    #Its hardcoded... I know... I actually got the number in 4 tries... after thinking... idk im bad...
    idx = 0
    while(idx < 10932):
        for i in range(len(values)):
            circles[i].move(values[i][2], values[i][3])
        idx += 1
        
    win.getMouse()
    win.close()
    
main()