sum = 0

with open('input.txt', 'r') as input:
    for index, line in enumerate(input):
        line_split = line.split(": ")[1].replace(";", ",").split(", ")
        highest_red = None
        highest_green = None
        highest_blue = None

        for item in line_split:
            number = int(item.split(" ")[0])
            if "red" in item:
                if highest_red is None:
                    highest_red = number
                elif number > highest_red:
                    highest_red = number
            elif "green" in item:
                if highest_green is None:
                    highest_green = number
                elif number > highest_green:
                    highest_green = number
            elif "blue" in item:
                if highest_blue is None:
                    highest_blue = number
                elif number > highest_blue:
                    highest_blue = number

        power = highest_blue * highest_green * highest_red
        sum += power
    
    print(sum)