def main():
    file = open("../input.txt", "r")
    values = []
    past_values = []
    total = 0
    found = False
    
    for line in file:
        values.append(line)
    
    while not found:
        for val in values:
            if val[0] == '+':
                total += int(val[1:-1])
            else:
                total -= int(val[1:-1])
                
            for past in past_values:
                if(total == past):
                    found = True
                    #break
                    
            if found:
                break
                
            past_values.append(total)
    print(total)
    
main()