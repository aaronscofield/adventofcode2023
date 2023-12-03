sum = 0

with open('input.txt', 'r') as input:
    for index, line in enumerate(input):
        line_split = line.split(": ")[1].replace(";", ",").split(", ")
        accepted = None

        for item in line_split:
            number = int(item.split(" ")[0])
            if "red" in item:
                if number > 12:
                    accepted = False
            elif "green" in item:
                if number > 13:
                    accepted = False
            elif "blue" in item:
                if number > 14:
                    accepted = False

        if accepted is not False:
            sum += (index + 1)
    
    print(sum)