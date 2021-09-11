text = input().split('\\')

needed_string = text[-1].split('.')
print(f'File name: {needed_string[0]}')
print(f'File extension: {needed_string[1]}')