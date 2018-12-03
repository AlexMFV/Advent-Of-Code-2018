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

def checkSum(two, three):
    return two * three

main()
