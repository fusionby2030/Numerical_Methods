
"""
Evaluatte bits of fractional part up to 2nd repeating block



Convert decimal fraction to binary.

Process:

Split number into frac and not frac

what is int part mod by 2 and stick remainder into array
and divide by 2 repeat

"""

decimal_fract = 34/5  #float
fraction = decimal_fract - int(decimal_fract) #float
binary_list = []
while True:
    if len(binary_list) > 4 and  binary_list[:4] == binary_list[4:]:
        break
    mod = int(fraction*2)
    binary_list.append(str(mod))
    fraction = fraction*2 - mod
print(''.join([str(i) for i in binary_list]))
