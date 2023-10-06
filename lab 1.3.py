#задача 3
print('y = 2x + 3')
GREY = "\033[47m"
BLACK = "\033[49m"
END = "\033[0m"
for i in range(10, -1, -1):
    print(f'{BLACK}{"  " * i}{GREY}{"  "}{END}', i+3)

print(' 0   1   2   3   4   5')