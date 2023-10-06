#задача 1
RED = "\033[41m"
GREEN = "\033[42m"
END = "\033[0m"

for i in range(6):
    if i<3:
        print(f'{GREEN}{" " * (8-i)}{RED}{" " * i}{RED}{" " * i}{GREEN}{" " * (8-i)}{END}')
    else:
        print(f'{GREEN}{" " * (i+3)}{RED}{" " * (5-i)}{RED}{" " * (5-i)}{GREEN}{" " * (i+3)}{END}')