import sys
inputs = iter(sys.stdin.readlines())
cases = int(next(inputs))
for case in range(cases):
    num1, num2 = map(int, next(inputs).split())
    if num1 < num2:
        print('<')
    elif num1 == num2:
        print('=')
    elif num1 < num2:
        print('>')
