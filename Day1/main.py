pos = 50
res = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # Process each line here
        direction = line[0]
        value = int(line[1:])
        print(f"Direction: {direction}, Value: {value}")
        if direction == 'R':
            pos += value
        elif direction == 'L':
            pos -= value
        while pos < 0:
            pos = 100 + pos
        while pos >= 100:
            pos = pos - 100
        if pos == 0:
            res += 1
print(res)


pos = 50
res = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # Process each line here
        direction = line[0]
        value = int(line[1:])
        while value > 0:
            if direction == 'R':
                pos += 1
            elif direction == 'L':
                pos -= 1
            value -= 1
            while pos < 0:
                pos = 100 + pos
            while pos >= 100:
                pos = pos - 100
            if pos == 0:
                res += 1
print(res)