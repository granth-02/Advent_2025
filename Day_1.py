rotations = []

with open('E:\VS Code\Advent\Advent_2025\input.txt') as f:
    for strings in f:
        rotations.append(strings.strip())

position = 50
password = 0


for seq in rotations:
    direction = seq[0]
    movement = int(seq[1:])

    match direction:
        case 'R':
            for _ in range(movement):
                position = (position + 1) % 100
                if position == 0:
                    password += 1
        
        case 'L':
            for _ in range(movement):
                position = (position - 1) % 100
                if position == 0:
                    password += 1
    
    
            
    
print(password)


