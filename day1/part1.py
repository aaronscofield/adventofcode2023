sum = 0

with open('input.txt', 'r') as input:
    for line in input:
        firstnum = None
        lastnum = None
        for char in line:
            try: 
                num = int(char)
                if firstnum is None:
                    firstnum = num
                lastnum = num
            except:
                continue

        constructed = f"{firstnum}{lastnum}"
        sum += int(constructed)
    
print(sum)

