import os, sys

file_name = 'input.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    datastream = list(f.read())

i = 4
x = datastream[:i]
while len(set(x)) < 4:
    i += 1
    x.pop(0)
    x += datastream[i-1]
ans1 = i
print(f'answer to first puzzle of day {day} is: {ans1}')

i = 14
x = datastream[:i]
while len(set(x)) < 14:
    i += 1
    x.pop(0)
    x += datastream[i-1]
ans2 = i
print(f'answer to second puzzle of day {day} is: {ans2}')