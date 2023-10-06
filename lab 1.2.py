#задача 2
GREY = "\033[47m"
BLACK = "\033[49m"
END = "\033[0m"
k=9
print(k*(f'{GREY}{" " * 8}{BLACK}{" " * 10}{END}'))
print(k*(f'{GREY}{" " * 2}{BLACK}{" " * 4}{GREY}{" " * 2}{BLACK}{" " * 10}{END}'))
print(k*(f'{GREY}{" " * 2}{BLACK}{" " * 2}{GREY}{" " * 4}{BLACK}{" " * 10}{END}'))
print(k*(f'{GREY}{" " * 2}{BLACK}{" " * 2}{GREY}{" " * 2}{BLACK}{" " * 12}{END}'))
print(k*(f'{GREY}{" " * 2}{BLACK}{" " * 2}{GREY}{" " * 10}{BLACK}{" " * 4}{END}'))