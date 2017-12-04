#!/usr/bin/env python3

# Read in my input:

first = True
first_num = None
previous = None
sum = 0

nums = []
carets = []
with open('input.txt', 'r') as f:
    while True:
        char = f.read(1)
        nums.append(char)
        carets.append('.')
#        import pdb; pdb.set_trace()
        if char.isdigit():
            digit = int(char)
            if first:
                first_num = int(char)
                first = False
            
            if previous:
                if previous == digit:
                    sum += digit
                    carets[-1] = '*'
            previous = digit
        elif char == '':
            break
if previous == first_num:
    carets[-1] == '*'
    sum += previous

print(''.join(nums))
print(''.join(carets))
print('sum is {}'.format(sum))

