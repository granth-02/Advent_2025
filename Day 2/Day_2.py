

with open("E:\VS Code\Advent_2025\Day 2\input.txt") as f:
    ID = f.read().split(',')

invalid_ID = 0
invalid_ID_2 = 0


for ranges in ID:
    halves = ranges.split("-")
    fId = int(halves[0])
    lId = int(halves[1])

    for numb in range (fId, lId + 1):
        numb_str = str(numb)
        half_len = len(numb_str) // 2
        if numb_str[:half_len] == numb_str[half_len:]:
            invalid_ID += numb

        for segment in range(1, half_len + 1):
            if len(numb_str) % segment == 0:
                pattern = numb_str[:segment]
                reps = len(numb_str) // segment
                
                if pattern * reps == numb_str:
                    invalid_ID_2 += numb
                    break

print(invalid_ID_2)