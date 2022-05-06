import os

def get_str(x):
    lines = []
    with open(x, 'r') as f:
        for line in f:
            lines.append(str(line))
    print(lines)

get_str('base64.txt')
