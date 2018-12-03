def main():
    file = open("../input.txt", "r")
    strings = []
    singleChars = []
    counts = []
    list = []
    
    two = 0
    three = 0
    
    for line in file:
        strings.append(line)
    
    for string in strings:
        for char in string:
            for i in range(1, len(string)):
                if char == string[i]:
                    new = string[:i] + string[i+1:]
        singleChars.append(new)
        
    print(singleChars)
    
    for full in strings:
        for char in singleChars:
            list.append(full.count(char))
        counts.append(list)
        list.clear()
        
    for c in counts:
        if c.count('2') > 0:
            two += 1
        if c.count('3') > 0:
            three += 1
            
    print(checkSum(two, three))

def checkSum(two, three):
    return two * three
    
main()