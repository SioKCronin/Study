# Day 2 - 2015

def transform_data(data):
    return [[y for y in x.strip().split('x')] for x in data.strip().split()]

with open('day2.txt') as f:
    data = transform_data(f.read())

total_paper = 0

for present in data:
    l = int(present[0])
    w = int(present[1])
    h = int(present[2])
    lw = (l*w)
    wh = (w*h)
    lh = (l*h)
    extra = min(x for x in [lw, wh, lh])
    total_paper += (2*lw) + (2*wh) + (2*lh) + extra

print(total_paper)

