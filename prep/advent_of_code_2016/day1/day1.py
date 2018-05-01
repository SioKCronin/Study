# Day 1 - 2016

import numpy as np
import operator

def transform_data(data):
    return [(x[0], int(x[1:])) for x in data.strip().split(', ')]

def next_direction(current_direction, instruction):
    return {
        'N': {'R': 'E', 'L': 'W'},
        'S': {'R': 'W', 'L': 'E'},
        'E': {'R': 'S', 'L': 'N'},
        'W': {'R': 'N', 'L': 'S'}
    }[current_direction][instruction]

def blocks_from_instructions(instructions):
    dirs = {
        'N': np.array([0, 1]),
        'S': np.array([0, -1]),
        'E': np.array([1, 0]),
        'W': np.array([-1, 0])
    }
    coords = np.array([0, 0])
    historic_coords = np.array([0,0])
    current_direction = 'N'
    for instruction in instructions:
        current_direction = next_direction(current_direction, instruction[0]) 
        coords = coords + (dirs[current_direction] * instruction[1])
    return abs(coords[0]) + abs(coords[1])

with open('day1.txt') as f:
    data = transform_data(f.read())

def visited_twice(instructions):
    dirs = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    coords = (0,0)
    current_direction = 'N'
    historic_coords = [(0,0)]
    for instruction in instructions:
        current_direction = next_direction(current_direction, instruction[0])
        new_coords = tuple(map(operator.add, coords,
            tuple([z * instruction[1] for z in dirs[current_direction]])))
        if current_direction == 'N':
            for y in range(coords[1]+1, new_coords[1]+1):
                if (coords[0], y) in historic_coords:
                    print("Found it", (coords[0], y))
                    return abs(coords[0]) + abs(y)
                else:
                    historic_coords.append((new_coords[0], y))
            coords = new_coords
        if current_direction == 'E':
            for x in range(coords[0]+1, new_coords[0]+1):
                if (x, coords[1]) in historic_coords:
                    print("Found it", (x, coords[1]))
                    return abs(x) + abs(coords[1])
                else:
                    historic_coords.append((x,new_coords[1]))
            coords = new_coords
        if current_direction == 'W':
            for x in range(coords[0]-1, new_coords[0]-1, -1):
                if (x, coords[1]) in historic_coords:
                    print("Found it", (x, coords[1]))
                    return abs(x) + abs(coords[1])
                else:
                    historic_coords.append((x,new_coords[1]))
            coords = new_coords
        if current_direction == 'S':
            for y in range(coords[1]-1, new_coords[1]-1, -1):
                if (coords[0], y) in historic_coords:
                    print("Found it", (coords[0], y))
                    return abs(coords[0]) + abs(y)
                else:
                    historic_coords.append((new_coords[0], y))
            coords = new_coords
        print(historic_coords)

# print blocks_from_instructions([('R',2),('L',3)])
# print blocks_from_instructions([('R', 2), ('R', 2), ('R', 2)])
# print blocks_from_instructions(data)

print(visited_twice(data))
