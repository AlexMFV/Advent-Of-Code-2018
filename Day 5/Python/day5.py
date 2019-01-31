
def main():
    file = open("../input.txt", "r")

    dataOG = file.read()
    hasExited = False
    edited = False
    abc = "abcdefghijklmnopqrstuvyxwz"
    count = 0
    letter = ' '

    for a in range(len(abc)):
        data = dataOG
        data = data.replace(abc[a], '')
        data = data.replace(abc[a].upper(), '')
        hasExited = False
        while not hasExited:
            for i in range(len(data)-1):
                if i < len(data)-1:
                    if data[i].upper() == data[i+1] and data[i+1].lower() == data[i] or data[i].lower() == data[i+1] and data[i+1].upper() == data[i]:
                        data = data[:i] + data[i+2:]
                        edited = True

                if edited == True:
                    break;

            if edited == False:
                hasExited = True

                if a == 0:
                    count = len(data)
                    letter = 'a'
                elif count > len(data):
                    count = len(data)
                    letter = abc[a]

            else:
                edited = False

    #print(len(data))
    print(count)
    print(letter)

main()
