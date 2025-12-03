with open(r"E:\VS Code\Advent_2025\Day 3\input.text") as f:
    Banks = f.read().split('\n')

Banks = [j for j in Banks if j.strip() != ""]

total = 0
max_jolts = 12


for joltage in Banks:
    jolts = [int(j) for j in joltage]
    n = len(jolts)
    start = 0

    joltage_list = []

    for remaining_jolts in range(max_jolts, 0, -1):
        end = n - remaining_jolts
        digits = jolts[start:end + 1]
        max_digit = max(digits)
        max_index = jolts.index(max_digit, start, end + 1)

        joltage_list.append(max_digit)
        start = max_index + 1

    convert_joltage = int(''.join(str(j) for j in joltage_list))
    total += convert_joltage

print(total)