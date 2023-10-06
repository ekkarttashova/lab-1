#задача 4
f = open('sequence.txt')
sum_1=0
sum_2=0
s = [i for i in f.read().split('\n')]
for i in range(len(s)):
    s[i]=str(s[i]).replace('-', '-', 1)
for j in range(125):
    sum_1+=float(s[j])
for k in range(len(s)-125, len(s)):
    sum_2+=float(s[k])
GREY = "\033[47m"
END = "\033[0m"
print(f'{GREY}{" " * round(sum_1+0.7 * abs(sum_2))}{END}', 'cумма первых 125 членов:', sum_1)
print(f'{GREY}{" " * round(0.7 * abs(sum_2))}{END}', 'cумма вторых 125 членов:', sum_2)