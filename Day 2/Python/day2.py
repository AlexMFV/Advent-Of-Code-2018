def main():
    file = open("../input.txt", "r")
    countLists = []
    chars = []
    counts = []

    exists = False

    two = 0
    three = 0

    for line in file:
        for char in line:
            for i in range(len(chars)):
                if chars[i] == char:
                    exists = True
                    break
            if not exists:
                chars.append(char)
                counts.append(line.count(char))
            exists = False
        countLists.append(counts.copy())
        counts.clear()
        chars.clear()

    for val in countLists:
        if val.count(2) > 0:
            two += 1

        if val.count(3) > 0:
            three += 1
            
    print(checkSum(two, three))
    
##  Part 2

    file = open("../input.txt", "r")
    
    isEqual = False
    idx = 0 
    
    for line in file:
        file2 = open("../input.txt", "r")
        for line2 in file2:
            if line != line2:
                idx, isEqual = getDifference(line, line2)
                
            if isEqual:
                break
                
        if isEqual:
            line = line[:idx] + line[idx+1:]
            print(line)
            break
                
def getDifference(line, line2):
    for i in range(len(line)):
        if line[i] != line2[i]:
            line = line[:i] + line[i+1:]
            line2 = line2[:i] + line2[i+1:]
            
            if line == line2:
                return i, True
            else:
                return i, False
                
    return i, False

def checkSum(two, three):
    return two * three

main()
