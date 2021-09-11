string = input()

output = ''
for ch in string:
    ascii_ch = ord(ch)
    needed_ch = ascii_ch + 3
    output += chr(needed_ch)

print(output)