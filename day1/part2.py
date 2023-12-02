import re

digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 
          'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

sum = 0
with open('input.txt', 'r') as input:
    lines = input.read().splitlines()
    for line in lines:
        firstnum, firstnumindex = None, None
        lastnum, lastnumindex = None, None
        for index, char in enumerate(line):
            try: 
                num = int(char)
                if firstnum is None:
                    firstnum = num
                    firstnumindex = index
                lastnum = num
                lastnumindex = index
            except:
                continue
            
        for letter in digits.keys():
            if letter in line:
                locs = [m.start() for m in re.finditer(letter, line)]
                for loc in locs:
                    if loc < firstnumindex:
                        firstnumindex = loc
                        firstnum = digits[letter]
                    elif loc > lastnumindex:
                        lastnumindex = loc
                        lastnum = digits[letter]

        constructed = f"{firstnum}{lastnum}"
        sum += int(constructed)

print(sum)
